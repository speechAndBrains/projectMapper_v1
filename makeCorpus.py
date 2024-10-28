def getExcelToLoad(): #To prompt user to select excel containing file paths, and load excel as data frame
    from tkinter import filedialog as fd
    import pandas as pd
    
    excelToOpen = fd.askopenfilename(title = 'Locate excel file')
    df = pd.read_excel(excelToOpen, header = 0)
    
    return df


def loadUpFiles(fileList): #To load files an join all their text; argument is a df (output from getExcelToLoad())
    import os
    #pip install docx2txt
    import docx2txt
    #pip install PyPDF2
    import PyPDF2
    
    getFileList = fileList["pathToFiles"]
    allText = []
    
    for f in getFileList:
        print(f"The current file is: {f}")
        splitFile = os.path.splitext(f); #Splits file path into file name and extension (e.g. .docx)
    
        if splitFile[1] == '.docx':
            print('Converting docx')
            wordDoc = docx2txt.process(f); #Extracts file content as string
            allText.append(wordDoc)
            del wordDoc #Deletes variable
    
        elif splitFile[1] == '.pdf':
            print('Converting pdf')
            pdfDoc = PyPDF2.PdfReader(f); #Similar to os.path.splitext(), but for pdf?
            pdfz = '' #WHY?
            for pageNum in range(0,len(pdfDoc.pages)): #Looping through pages
                page = pdfDoc.pages[pageNum] #Storing current page?
                nextPage = page.extract_text(0) #Extracting current page's content?
                pdfz = pdfz + nextPage #Adding a space right before the current page's content?
            allText.append(pdfz)
            del f, pdfDoc, pdfz, pageNum, page, nextPage
        
        else:
            print('ERROR: FILE IS NOT .docx OR .pdf')
    
    del splitFile
    return allText


def saveText(allText):
    from tkinter import filedialog
    import json
    
    directoryPath = filedialog.askdirectory(title = 'Select directory to write corpus to')
   
    import makeList
    slash = makeList.getSlash(directoryPath) #If first character is / or \, outputs / or \; if it's not either, stops code running
    outFile = open(directoryPath + slash + 'rawCorpus.json','w+') #Creating a new file; first argument is file path; second argument is mode, meaning that the file is openned in writing mode with reading capability (file can be both written and read (???))
    
    json.dump(allText, outFile) #"Serializes the allText Python object into a JSON formatted string and writes it to outFile, a file-like object"


def runCorpus():
    fileList = getExcelToLoad()
    allText = loadUpFiles(fileList)
    saveText(allText)
    