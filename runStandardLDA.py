# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 13:38:47 2024

@author: k2258346
"""

def runLDA():
    
    def runLDAOpt(nt, alpha, eta):
        from gensim.models import LdaModel 
        from gensim.models.coherencemodel import CoherenceModel

        assert type(nt) == int
        
        num_topics=int(nt)
        
        model = LdaModel(doc_term_matrix, num_topics=num_topics, id2word = dictionary, alpha=alpha, eta=eta, iterations=1000)  # train model
        coherencemodel = CoherenceModel(model=model, texts=texts, dictionary=dictionary, coherence='u_mass')
        print('calculate done')
        coherence_value=coherencemodel.get_coherence()
        return -1*coherence_value

    
    def discrete_params(num_topics, alpha, eta):
        nt=int(num_topics)
        return runLDAOpt(nt, alpha, eta)
        
    
    import utils
    message='Select bayesParams'
    bayesParams = utils.readJson(message)  
    pbounds={'num_topics': (bayesParams['minTop'], bayesParams['maxTop']),'alpha': (bayesParams['minAlp'], bayesParams['maxAlp']), 'eta': (bayesParams['minEta'], bayesParams['maxEta'])}
    
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
    
    print('start optimisation')
    from bayes_opt import BayesianOptimization
    optimizer = BayesianOptimization(f=discrete_params, pbounds=pbounds, verbose=2, random_state=1)
    
    nIter=int(bayesParams['nIter'])
    iterPoints=int(bayesParams['iterPoints'])
    
    optimizer.maximize(init_points=iterPoints,n_iter=nIter)
    
    print(optimizer.max)
    
    
    final_model = runfinalLDAmodel(doc_term_matrix,dictionary, texts,optimizer.max['params'])
    
    import pyLDAvis.gensim
    import utils
    topicMap = pyLDAvis.gensim.prepare(final_model, doc_term_matrix, dictionary)
    directoryPath=utils.selectDir()
    pyLDAvis.save_html(topicMap, directoryPath + '/LDAvis.html')
    
    
def runfinalLDAmodel(doc_term_matrix,dictionary, texts,opt_params):
    from gensim.models import LdaModel 
    from gensim.models.coherencemodel import CoherenceModel
    
    print('make model')
    final_model = LdaModel(doc_term_matrix, num_topics=round(opt_params['num_topics'],0), id2word = dictionary, alpha=opt_params['alpha'], eta=opt_params['eta'], iterations=1000)  # train model
    print('calculate coherence')
    coherencemodel = CoherenceModel(model=final_model, texts=texts, dictionary=dictionary, coherence='u_mass')
    coherence_value=coherencemodel.get_coherence()    
    
    print(coherence_value)
    
    return final_model
    
    