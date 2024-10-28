# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 20:09:43 2024

@author: k2258346
"""

def runHDP():
    
    import utils
    from gensim.models import HdpModel
    
    from gensim.models.coherencemodel import CoherenceModel
    
    #get doc term 
    message='Select doc term matrix'
    doc_term_matrix=utils.readJson(message)
    
    #load dictionary
    from gensim.corpora import Dictionary
    message = 'Select Dictionary'
    
    from tkinter import filedialog as fd
    objectToRead = fd.askopenfilename(title = message)
    
    dictionary = Dictionary.load_from_text(objectToRead)
    
    message = 'Select Processed Corpus File'
    texts = utils.readJson(message)
    ###
    
    final_model = HdpModel(corpus=doc_term_matrix,id2word=dictionary) 
    coherencemodel = CoherenceModel(texts=texts, dictionary=dictionary, model=final_model, coherence='u_mass')
    coherence_value=coherencemodel.get_coherence()
    print(coherence_value)
    
    import pyLDAvis.gensim
    import utils
   
    topicMap = pyLDAvis.gensim.prepare(final_model, doc_term_matrix, dictionary)
    directoryPath=utils.selectDir()
    pyLDAvis.save_html(topicMap, directoryPath + '/LDAvis.html')
    
    
