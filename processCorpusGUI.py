def processCorpus():
    
    from tkinter import IntVar, Tk, Checkbutton, Button
    
    class getChoice_class_:
        def __init__(self):
            self.value = ''
        def goExit(self):
            new_root.destroy()
    returnChoice = getChoice_class_()
    
    new_root = Tk()  #Creating root window
    new_root.maxsize(800, 600)
    new_root.title("Corpus Actions")
    new_root.config(bg = "white")
    
    #tok = IntVar()
    low = IntVar()
    stem = IntVar()
    sto = IntVar()
    excl = IntVar()
    #This chunk of code needs to come after Tk() (unsure as to exactly why)
    
    #Checkbutton(root, text="Tokenize", variable=tok, onvalue=1, offvalue=0).grid(row=0)
    Checkbutton(new_root, text="Lower case", variable=low, onvalue=1, offvalue=0).grid(row=0)
    Checkbutton(new_root, text="Stem words", variable=stem, onvalue=1, offvalue=0).grid(row=1)
    Checkbutton(new_root, text="Remove stop words", variable=sto, onvalue=1, offvalue=0).grid(row=2)
    #Checkbutton(new_root, text="Remove specific words", variable=excl, onvalue=1, offvalue=0).grid(row=3)
  
    button1 = Button(new_root, width=20, text="Go!", command=returnChoice.goExit).grid(row=4)

    new_root.mainloop()
    
    return low.get(), stem.get(), sto.get(), excl.get()