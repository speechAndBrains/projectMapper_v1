# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 09:50:17 2024

@author: k2258346
"""

import gensim as gensim

texts = [['human', 'interface', 'computer'],
         ['survey', 'user', 'computer', 'system', 'response', 'time'],
         ['eps', 'user', 'interface', 'system'],
         ['system', 'human', 'system', 'eps'],
         ['user', 'response', 'time'],
         ['trees'],
         ['graph', 'trees'],
         ['graph', 'minors', 'trees'],
         ['graph', 'minors', 'survey']]

# Create Dictionary
id2word = gensim.corpora.Dictionary(texts)

# Create Corpus: Term Document Frequency
corpus = [id2word.doc2bow(text) for text in texts]

# Create lda model
Lda = gensim.models.ldamodel.LdaModel
ldamodel = Lda(corpus, num_topics=2, id2word = id2word, iterations=50)

# Create coherence model
cm = gensim.models.coherencemodel.CoherenceModel(model=ldamodel, texts=texts, dictionary=id2word, coherence='c_v')

#get coherence - code gets hung up here
print('start get coh')
result = cm.get_coherence()
print('end coh')