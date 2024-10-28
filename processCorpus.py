def getFile():
    from tkinter import filedialog as fd
    jsonToRead = fd.askopenfilename(title = 'Locate raw corpus json file') 
    return jsonToRead


def readJson(jsonToRead):
    import json
    jsonIn = open(jsonToRead,'r') #Opening file in "reading" mode (?)
    data = json.load(jsonIn) #Loading file's data (?)
    return data


def saveProcessText(docs): 
    from tkinter import filedialog as fd
    import json
    directoryPath = fd.askdirectory(title='Select directory to write processed corpus to')
    import makeList
    slash = makeList.getSlash(directoryPath)
    outFile = open(directoryPath + slash + 'processedCorpus.json','w')
    json.dump(docs, outFile)
    return(docs)


def runProcess():
    
    jsonToRead = getFile()
    data = readJson(jsonToRead)
    import processCorpusGUI
    lowerWords, stemWords, stopWords, removeWords = processCorpusGUI.processCorpus()
    
    
    #from nltk.tokenize import RegexpTokenizer
    #tokenizer = RegexpTokenizer(r'\w+')
    from nltk.tokenize import WhitespaceTokenizer
    tokenizer=WhitespaceTokenizer()
    
    if stemWords == 1:
        from nltk.stem.porter import PorterStemmer
        p_stemmer=PorterStemmer()
        
    if stopWords == 1:
        import nltk
        nltk.download('stopwords')
        from nltk.corpus import stopwords
        en_stop=set(stopwords.words('english'))
    
    processedData=[]
    n=0
    for docs in data:
        
        if lowerWords == 1:
            docs = docs.lower()
        
        #docs=tokenizer.tokenize(docs)
        docs=tokenizer.tokenize(docs)
        
        if stopWords == 1:
            docs=[i for i in docs if not i in en_stop]
        if stemWords==1:
            docs=[p_stemmer.stem(i) for i in docs]
        processedData.append(docs)
        n=n+1
        print("Finished a doc")
    
   
    
    saveProcessText(processedData)
    
    print("saved processed data")
    
      
    return processedData
    
    
    