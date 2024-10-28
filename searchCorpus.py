def my_searcher(data, input_text_form):
    
    import numpy as np
    
    n_docs = len(data)
    n_inputs = len(input_text_form)
    import removeWords
    phrases1, _, largest_n = removeWords.maxPhrase(input_text_form, '')
    search_ind = [[[] for _ in range(n_inputs)] for _ in range(n_docs)]
    
    for i in range(n_docs):
        
        curr_doc = data[i] #Current document
        n_words = len(curr_doc) #Current document's number of words
        
        for j in range(n_words):
            
            curr_word = curr_doc[j] #Current word
            #print(curr_word)
            for k in range(n_inputs):
                curr_input = input_text_form[k] #Current input word/phrase
                if curr_word == curr_input:
                    search_ind[i][k].append(j)
            
            curr_seq = '' #Current sequence
            for n in range(1, largest_n):
                curr_seq = " ".join(curr_doc[j:(j+n+1)])
                #print(curr_seq)
                for k in range(n_inputs):
                    curr_input = input_text_form[k] #Current input word/phrase
                    if curr_seq == curr_input:
                        search_ind[i][k].append(j)
                
    
    search_occurences = np.zeros((n_docs, n_inputs))
    search_occurences = [[0 for _ in range(n_inputs)] for _ in range(n_docs)]
    for i in range(n_docs):
        for k in range (n_inputs):
            search_occurences[i][k] = len(search_ind[i][k])
    
    return(search_occurences, search_ind)



def saveSearchOutput(search_occurences, search_ind, input_text1_form, save_json):
    
    from tkinter import filedialog as fd
    import json
    directoryPath = fd.askdirectory(title='Select directory to write searchWord outputs to')
    import makeList
    slash = makeList.getSlash(directoryPath)
    
    import pandas as pd
    df_occ = pd.DataFrame(search_occurences)
    df_ind = pd.DataFrame(search_ind)
    
    def remove_brackets(cell):
        if isinstance(cell, list):
            cell = ', '.join(map(str, cell))
        return cell
    df_occ_clean = df_occ.applymap(remove_brackets)
    df_ind_clean = df_ind.applymap(remove_brackets)
    
    #df_occ_clean.index = [f"Doc {i+1}" for i in range(df_occ_clean.shape[0])]
    #df_ind_clean.index = [f"Doc {i+1}" for i in range(df_occ_clean.shape[0])]
    #df_occ_clean.columns = [f"Term {i+1}: {input_text1_form[i]}" for i in range(df_occ_clean.shape[1])]
    #df_ind_clean.columns = [f"Term {i+1}: {input_text1_form[i]}" for i in range(df_occ_clean.shape[1])]
    row_labels = [f"Doc {i+1}" for i in range(df_occ_clean.shape[0])]
    column_labels = [f"Term {i+1}: {input_text1_form[i]}" for i in range(df_occ_clean.shape[1])]
    df_occ_clean.index = row_labels
    df_ind_clean.index = row_labels
    df_occ_clean.columns = column_labels
    df_ind_clean.columns = column_labels
    
    df_occ_clean.to_excel(directoryPath + slash + 'searchOccurences.xlsx')
    df_ind_clean.to_excel(directoryPath + slash + 'searchIndices.xlsx') 
    
    if save_json == True:
        
        outFile = open(directoryPath + slash + 'searchOccurences.json','w')
        json.dump(search_occurences, outFile)
        
        other_outFile = open(directoryPath + slash + 'searchIndices.json','w')
        json.dump(search_ind, other_outFile)
    
    return(search_occurences, search_ind)



def runSearch():
    
    import removeWords
    jsonToRead = removeWords.getFile()
    import processCorpus
    data = processCorpus.readJson(jsonToRead)
    
    import searchCorpusGUI
    input_text1, save_json = searchCorpusGUI.getSearchPhrases()
    #input_text2 = '' #Keeping it empty since this GUI will only have one input
    
    input_text1_form, _ = removeWords.formatStrings(input_text1, '')

    search_occurences, search_ind = my_searcher(data, input_text1_form)
    
    saveSearchOutput(search_occurences, search_ind, input_text1_form, save_json)
    
    return(search_occurences, search_ind)

#Inputs for testing: limit, clerk maxwel, psychiatri psycholog, colleg