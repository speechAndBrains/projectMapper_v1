# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 15:11:47 2024

@author: k2258346
"""

def runDictionary():
    
    bayesParams=loadBayesParams()
    processedCorpus=loadProcessedCorpus()
    
    dictionary, doc_term_matrix=makeDictionary(bayesParams, processedCorpus)
    
    import utils
    directoryPath=utils.selectDir()
    slash = utils.getSlash(directoryPath)
    fname='dictionaryGensim'
    
    #special saving function for this object type from gensim
    dictionary.save_as_text(directoryPath + slash + fname)

    fname='docTermGensim'
    utils.saveJson(doc_term_matrix,fname,slash,directoryPath)
    
def loadBayesParams():
    import utils
    message='Load Bayes params'
    bayesParams = utils.readJson(message)
    return bayesParams

def loadProcessedCorpus():
    import utils
    message='Load Processed Corpus'
    processedCorpus = utils.readJson(message)
    return processedCorpus

def makeDictionary(bayesParams, processedCorpus):
    
    from gensim import corpora
    
    print('dictionary start')
    dictionary = corpora.Dictionary(processedCorpus)
    dictionary.filter_extremes(bayesParams['nwords']) #Keeping words that appear in least this number of docs
    
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in processedCorpus]
    print('dictionary complete')
    return dictionary, doc_term_matrix
    
    
