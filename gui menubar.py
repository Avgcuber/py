##to create menu bar
##from tkinter import *
##labelframe = Tk()
##labelframe.geometry('640x300')
##labelframe.title('Python GUI Menu Bar')
##menu_bar=Menu(labelframe)
##menu_bar.add_command(label='File')
##menu_bar.add_command(label='Help')
##labelframe.config(menu=menu_bar)
##mainloop()

#How to add menus to this menu bar

##from tkinter import *
##labelframe = Tk()
##labelframe.geometry('640x300')
##labelframe.title('Python GUI Menu Bar')
##menu_bar=Menu(labelframe)
##file = Menu(menu_bar,tearoff=0)
##file.add_command(label='New')
##menu_bar.add_cascade(label='File',menu = file)
##labelframe.config(menu=menu_bar)
##mainloop()

##add new quit

##from tkinter import *
##labelframe = Tk()
##labelframe.geometry('640x300')
##labelframe.title('Python GUI Menu Bar')
##def new():
##    labelframe1 = LabelFrame(labelframe, text="New File Editor Window")  
##    labelframe1.pack(fill="both", expand="yes")  
##    toplabel = Label(labelframe1, text="Content of file can be typed in here")  
##    toplabel.pack() 
##def close_window(): 
##    labelframe.destroy()
##menu_bar=Menu(labelframe)
##file = Menu(menu_bar,tearoff=0)
##file.add_command(label='New',command=new)
##file.add_separator()
##file.add_command(label="Quit",command=close_window)
##menu_bar.add_cascade(label='File',menu = file)
##labelframe.config(menu=menu_bar)
##mainloop()

##Adding widgets in the tabs, Example
##•	First Tab has a button color Red 
##•	second tab has a button color coral

##from tkinter import *
##from tkinter import ttk 
##labelframe = Tk()
##labelframe.geometry('640x300')
##labelframe.title('Python for SY')
##tabs = ttk.Notebook(labelframe)
##first = ttk.Frame(tabs) # A ttk.Frame is a simple rectangle widget that can hold other widgets.
##tabs.add(first, text='First')
##second = ttk.Frame(tabs)
##tabs.add(second, text='Second')
##a = Button(first, text='Hello There This is 1st Tab', bg='Red')
##a.pack()
##b = Button(second, text='Hello There This is 2nd Tab',bg = 'coral')
##b.pack()
##tabs.pack(expand=1, fill="both")
##mainloop()

