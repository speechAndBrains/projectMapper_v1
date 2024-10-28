def getFolder(): #To prompt user to select a directory
    from tkinter import filedialog
    directoryPath = filedialog.askdirectory(title='Select directory where the files are located') 
    print(f"Directory path: {directoryPath}")
    return directoryPath


def getFiles(chosenPath): #To get file paths in directory
    import os
    chosenFiles = os.listdir(chosenPath);
    print(f"First file in directory path: {chosenFiles[0]}")
    return chosenFiles


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


def writeToExcel(filesPlusPath, slash): #To prompt user to select a directory and write excel to it
    from tkinter import filedialog
    directoryForExcel = filedialog.askdirectory(title='Select directory to write Excel to') 
    print(f"Directory for Excel: {directoryForExcel}")
    import pandas as pd
    df = pd.DataFrame(filesPlusPath, columns = ["pathToFiles"])
    df.to_excel(directoryForExcel + slash + "ToBeLoadedFiles.xlsx", index=False)
    print("Output file path:")
    print(directoryForExcel + slash + "ToBeLoadedFiles.xlsx")


def runList(): #To do everything in sequence
    directoryPath = getFolder()
    chosenFiles = getFiles(directoryPath)
    slash = getSlash(directoryPath)
    filesPlusPath = []
    for i in chosenFiles:
        filesPlusPath.append(directoryPath + slash + i)
    writeToExcel(filesPlusPath, slash)




