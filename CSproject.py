#Tkinter
import tkinter

#window
wn= tkinter.Tk()
wn.geometry('450x450')
wn.configure(bg='green')
wn.title('CS Project')

#Game Menu

def doButton1():
    but1.configure(text='Start Game')
def doButton2():
    but2.configure(text='Credits')
def doButton3():
    but3.configure(text='Exit Game')
    

gametittle= tkinter.Label(wn, text='CS Project')
gametittle.place(relx=.5, rely=.15, anchor='c')   
but1= tkinter.Button(wn, text='Start Game', width=15, command=doButton1)
but1.place(relx=.5, rely=.5, anchor='c')
but2= tkinter.Button(wn, text='Credits', width=15,  command=doButton2)
but2.place(relx=.5, rely=.6, anchor='c')
but3= tkinter.Button(wn, text='Exit Game', width=15,  command=doButton3)
but3.place(relx=.5, rely=.7, anchor='c')


########
def opt1():
    option1.configure(text='Start Game')
def opt2():
    option2.configure(text='Credits')
    
if(doButton1):
    option1= tkinter.Button(wn, text='option 1', width=15, command=opt1)
    option1.place(relx=.9, rely=.85, anchor='c')
    option2= tkinter.Button(wn, text='option 2', width=15,  command=opt2)
    option2.place(relx=.1, rely=.85, anchor='c')










wn.mainloop()
