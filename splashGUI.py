def getChoice(): #Defining a getChoice() function
    
    from tkinter import Tk, Button #Tk is for root window; Button is for GUI buttons
    
    root = Tk()  #Initializing and naming a root window
    root.maxsize(800, 600)  #Specifying the max size it can expand to
    root.config(bg="white") #Specifying its color
    root.title("Topic Mapper")  #Specifying its title

    class getChoice_class: #Defining a getChoice class; it takes no inputs, and consists of the constructor + 5 methods
        def __init__(self): #Constructor; automatically called when creating a new instance
            self.value = '' #Initializing value attribute when creating a new object (although it's still empty); this is required for the subsequent methods to actually "fill in" the value attribute
        def listGUI(self): #Method 1
            self.value = 'List' #Method 1 sets the instance's value attribute as 'List'
            root.destroy() #Method 1 then closes the root window and child widgets, thus stopping the main event loop
        def corpusGUI(self): #Other methods do the same thing
            self.value = 'Corpus'
            root.destroy()
        def processGUI(self):
            self.value = 'Process'
            root.destroy()
        def removeGUI(self):
            self.value = 'Remove'
            root.destroy()
        def searchGUI(self):
            self.value = 'Search'
            root.destroy()
        def dictGUI(self):
            self.value='Dictionary'
            root.destroy()
        def paramsGUI(self):
            self.value='Parameters'
            root.destroy()
        def modellingGUI(self):
            self.value = 'Topic'
            root.destroy()
        def modellingGUI2(self):
            self.value = 'Topic2'
            root.destroy()
    returnChoice = getChoice_class() #Calling/storing an instance of the getChoice class
    
    button0 = Button(root, width=50, height=2, text="Get file list", command=returnChoice.listGUI).grid(row=0) #Defining the root window's button 1, including its width, text/label, associated command, and position within the window's grid. The command is defined as a method/function from the returnChoice object/istance of the getChoice class. As such, the command sets the instance's value attribute as 'List' and closes the root window
    button1 = Button(root, width=50, height=2, text="Create raw corpus", command=returnChoice.corpusGUI).grid(row=1) #Other buttons do the same thing
    button2 = Button(root, width=50, height=2, text="Process corpus", command=returnChoice.processGUI).grid(row=2)
    button3 = Button(root, width=50, height=2, text="Remove specific words", command=returnChoice.removeGUI).grid(row=3)
    button4 = Button(root, width=50, height=2, text="Search corpus", command=returnChoice.searchGUI).grid(row=4)
    button5 = Button(root, width=50, height=2, text="Get Params for LDA for Bayesian Optimisation", command=returnChoice.paramsGUI).grid(row=5)
    button6 = Button(root, width=50, height=2, text="Create Dictionary", command=returnChoice.dictGUI).grid(row=6)
    button7 = Button(root, width=50, height=2, text="LDA", command=returnChoice.modellingGUI).grid(row=7)
    button8 = Button(root, width=50, height=2, text="HDP", command=returnChoice.modellingGUI2).grid(row=8)
    
    root.mainloop() #Starts main loop; keeps window open; handles user-triggered events
    
    return returnChoice #Returns the stored istance of the getChoice class

#In summary, this script defines a getChoice() function which defines a getChoice class and a returnChoice object, starts a GUI which enables the change of the returnChoice object (particularly, its value attribute), and returns the returnChoice object