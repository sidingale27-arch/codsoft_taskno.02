from tkinter import *

def click(event):
    try:
        global value 
        text = event.widget.cget("text")
        if entry.get() == "Error Try Again":
            entry.delete(0,END)
        if text == "=":
            if value.get().isdigit():
                total = int(value.get())
            else:
                total = eval(entry.get())
                
            value.set(total)
            entry.update()
               
        elif text == "C":
            value.set("")
            entry.update()
            
        else:
            value.set(value.get() + text)
            entry.update()
    except Exception as e:
        entry.delete(0,END)
        entry.insert(0,"Error Try Again")
        return  
        
    
window = Tk()

# size of the window 
window.geometry("360x460")
window.resizable(0,0)# as calculator is floating the window does not resizable
window.title("Calculator by Siddhesh")
try:
    icon = PhotoImage(file="cal.png")
    window.iconphoto(True,icon)
except Exception as e:
    print("file not Found")


value = StringVar()
value.set("")
# create frame1 and frame2
frame1 = Frame(window,bg='#E3F2FD')
frame2 = Frame(window,bg='#E3F2FD')

# create entry and place using grid 
entry = Entry(frame1,textvar=value,fg="#0D1B2A",bg="#BBDEFB",relief='solid',font=("arial 15 bold"),bd=3)
entry.grid(row=1,column=1,sticky="SNEW")

list = ["9","8","7","/","6","5","4","*","3","2","1","-","C","0","=","+"]
for i in range(len(list)):
    list[i] = Button(frame2,text=list[i],
                    font=("arial 15 bold"),relief='solid',
                    fg='#0D1B2A',bg='#64B5F6',padx=15,pady=7,
                    activeforeground="#FFFFFF",activebackground="#1976D2")
    list[i].bind("<Button-1>",click)  

     
     
# Grid configuration for the all widgets 
window.columnconfigure(0,weight=1)
window.rowconfigure(0,weight=3)
window.rowconfigure(1,weight=4)

# grid placement of frame1 and frame2
frame1.grid(row=0,column=0,sticky="SNEW")
frame2.grid(row=1,column=0,sticky="SNEW")

# configure frame1 row and column
frame1.columnconfigure(0,weight=1)
frame1.columnconfigure(1,weight=6)
frame1.columnconfigure(2,weight=1)
frame1.rowconfigure(0,weight=1)
frame1.rowconfigure(1,weight=1)
frame1.rowconfigure(2,weight=1)

# loop to configure frame2 row and column
for i in range(0,6):
    frame2.columnconfigure(i,weight=1)
    frame2.rowconfigure(i,weight=1)
    
# grid placement to the each button in list 
count = 0;
for i in range(1,5,1):
    for j in range(1,5,1):
        list[count].grid(row=i,column=j)
        count+=1

# hold the window 
window.mainloop() 