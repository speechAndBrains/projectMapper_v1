# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 18:48:10 2024

@author: k2258346
"""

def getParams():
    
    from tkinter import Tk, Button, Label, Entry #Tk is for root window; Button is for GUI buttons
   
    root = Tk()  #Initializing and naming a root window
    root.maxsize(800, 600)  #Specifying the max size it can expand to
    root.config(bg="white") #Specifying its color
    root.title("Choose parameters of Bayesian Optimisation")  #Specifying its title
    
    class getChoice_class:
        def __init__(self): #Constructor; automatically called when creating a new instance
            self.value = 'Parameters for Bayes optimisation' #Initializing value attribute when creating a new object (although it's still empty); this is required for the subsequent methods to actually "fill in" the value attribute
        def goExit(self): #Method 1
            self.nwords = float(entry1.get()) #Method 1 sets the instance's value attribute as 'List'
            self.minTop = float(entry2.get())
            self.maxTop = float(entry3.get())
            self.minAlp = float(entry4.get()) #Method 1 sets the instance's value attribute as 'List'
            self.maxAlp = float(entry5.get())
            self.minEta = float(entry6.get())
            self.maxEta = float(entry7.get())
            self.iterPoints = float(entry8.get())
            self.nIter = float(entry9.get())
            
            root.destroy()
        def makeDict(self):
            params = {'nwords': self.nwords, 
                      'minTop' : self.minTop,
                      'maxTop' : self.maxTop,
                      'minAlp' : self.minAlp,
                      'maxAlp' : self.maxAlp,
                      'minEta' : self.minEta,
                      'maxEta' : self.maxEta,
                      'iterPoints' : self.iterPoints,
                      'nIter' : self.nIter}
            
            return params
            
    returnChoice = getChoice_class()
        
    # N word freq        
    label1 = Label(root, text='Keep words that appear in at least this number of documents:')
    label1.grid(row=0, column=0, padx=5, pady=5)
    entry1 = Entry(root, width=10)
    entry1.grid(row=0, column=1, padx=5, pady=5)
    
    ## N topics
    label2 = Label(root, text='Topic range (min & max):')
    label2.grid(row=1, column=0, padx=5, pady=5)
    entry2 = Entry(root, width=10)
    entry2.grid(row=1, column=1, padx=5, pady=5)    
    entry3 = Entry(root, width=10)
    entry3.grid(row=1, column=2, padx=5, pady=5)

    label3 = Label(root, text='Alpha (min & max):')
    label3.grid(row=2, column=0, padx=5, pady=5)
    entry4 = Entry(root, width=10)
    entry4.grid(row=2, column=1, padx=5, pady=5)
    entry5 = Entry(root, width=10)
    entry5.grid(row=2, column=2, padx=5, pady=5)

    label4 = Label(root, text='Eta (min & max):')
    label4.grid(row=3, column=0, padx=5, pady=5)
    entry6 = Entry(root, width=10)
    entry6.grid(row=3, column=1, padx=5, pady=5)
    entry7 = Entry(root, width=10)
    entry7.grid(row=3, column=2, padx=5, pady=5)
    
    label5 = Label(root, text='Iteration Points:')
    label5.grid(row=4, column=0, padx=5, pady=5)
    entry8 = Entry(root, width=10)
    entry8.grid(row=4, column=1, padx=5, pady=5)
    
    label6 = Label(root, text='Iteration N:')
    label6.grid(row=5, column=0, padx=5, pady=5)
    entry9 = Entry(root, width=10)
    entry9.grid(row=5, column=1, padx=5, pady=5)
    

    button0 = Button(root, width=50, height=2, text="Go!", command=returnChoice.goExit).grid(row=6)
    

    root.mainloop()
    
    return returnChoice
    