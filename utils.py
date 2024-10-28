# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 10:45:58 2024

@author: k2258346
"""

#general function for identifying slash for different platforms
def getSlash(directoryPath):
    path = str(directoryPath)
    
    num_forw = []
    num_back = []
    for i in range (len(path)):
        character = path[i]
        #print(character)
        if character == '/':
            #print("YES")
            num_forw.append(i)
        if character == '\\':
            #print("YES")
            num_back.append(i)
        #else:
            #print("NO")

    if len(num_forw) == len(num_back):
        import platform
        operatingSystem = platform.system()
        if operatingSystem == 'Windows':
            #print('Windows')
            slash = '/'
        else:
            #print('Non-windows')
            slash = '\\'
    
    if len(num_forw) > len(num_back):
        slash = '/'
    if len(num_forw) < len(num_back):
        slash = '\\'

    return(slash)

#general routine for saving json files
def saveJSON(params,fname,slash,directoryPath): 
    
    import json
    
    outFile = open(directoryPath + slash + fname + '.json', 'w')
    json.dump(params, outFile)

#general routine to identify directory    
def selectDir():
    from tkinter import filedialog as fd
    
    directoryPath = fd.askdirectory(title='Select directory to write to')
    
    return directoryPath

#general routine to save
def saveJson(params,fname,slash,directoryPath):
    
    import json
    
    outFile = open(directoryPath + slash + fname + '.json','w+') #Creating a new file; first argument is file path; second argument is mode, meaning that the file is openned in writing mode with reading capability (file can be both written and read (???))
    
    json.dump(params, outFile)
    
#general function for reading in json saved files
def readJson(message):
    from tkinter import filedialog as fd
    import json
    jsonToRead = fd.askopenfilename(title = message) #SHOULDN'T THIS BE "LOCATE JSON FILE"?
   
    jsonIn = open(jsonToRead,'r') #Opening file in "reading" mode (?)
    data = json.load(jsonIn)
    
    return data

    