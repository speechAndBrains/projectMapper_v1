import splashGUI
returnChoice = splashGUI.getChoice() #Getting user Choice 

if returnChoice.value == 'List': #If choise is makeList
    print('Make a file list')
    import makeList #Importing makeList
    makeList.runList() #Running routines
    
elif returnChoice.value == 'Corpus': #If choise is makeCorpus
    print('Load raw corpus')
    import makeCorpus #Importing makeCorpus
    makeCorpus.runCorpus() #Running routines

elif returnChoice.value == 'Process': #If choice is processCorpus
    print ('Process corpus')
    import processCorpus #Importing processCorpus
    dataOutput = processCorpus.runProcess() #Running routine and storing output
    print(dataOutput) #Priting output

elif returnChoice.value == 'Remove': #If choice is removeWords
    print('Remove specific words')
    import removeWords #Importing removeWords
    removeWords.runRemove() #Running routine

elif returnChoice.value == 'Search': #If choice is searchCorpus
    print('Search corpus')
    import searchCorpus #Importing searchCorpus
    searchCorpus.runSearch() #Running routine
       
elif returnChoice.value == 'Parameters':
    ## get Parameters for search and save out
    print('Parameters')
    import getParams
    response=getParams.runParams()
    
elif returnChoice.value == 'Dictionary':
    ## Load up processed corpus; make into gensim dictionary; save out
    print('Dictionary')
    import createDictionary
    createDictionary.runDictionary()
    
elif returnChoice.value == 'Topic': #If choice is LDA
    print('Run LDA')
    #run LDA with Bayesian Optimisation
    import runStandardLDA
    runStandardLDA.runLDA()

elif returnChoice.value == 'Topic2': #If choice is HDP
    print('Run HDP')
    import runHDPversion #Importing HDP
    runHDPversion.runHDP()

else: #If there's no choice (user closes GUI)
    print('Other option')