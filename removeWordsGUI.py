def getPhrases():
    
    import tkinter as tk
        
    root = tk.Tk()
    root.title("Remove Specific Words")
    
    label1 = tk.Label(root, text='Words/phrases to remove (separated by comma)')
    label1.pack(padx=5, pady=5)
    entry1 = tk.Entry(root, width=50)
    entry1.pack(padx=5, pady=5)
    label2 = tk.Label(root, text='Words/phrases to keep (separated by comma)\nThis overrides the previous entry')
    label2.pack(padx=5, pady=5)
    entry2 = tk.Entry(root, width=50)
    entry2.pack(padx=5, pady=5)

    def after_button_click():
        global input_text1, input_text2
        input_text1 = entry1.get()
        input_text2 = entry2.get()
        root.destroy()
        
    button = tk.Button(root, text="Go!", command=after_button_click)
    button.pack(padx=5, pady=5)
    
    root.mainloop()
    
    #print(f"Input 1: {input_text1}")
    #print(f"Input 2: {input_text2}")
    
    return input_text1, input_text2