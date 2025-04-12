from tkinter import *

window=Tk()
window.title("Exercises")
window.minsize(600,600)
window.config(bg="yellow",padx=20,pady=20)

label=Label(text="My label")
label.config(bg="red",padx=10,pady=10)
label.grid(row=0,column=2)





def button_clicked():
    entry_input = text.get("1.0",END)
    print(entry_input)
    print("button clicked")
    
button=Button(text="button" ,command =button_clicked)
button.grid(row=1,column=2)
button.config(padx=10,pady=10)


entry=Entry(width=20)
entry.grid(row=2,column=2)

text = Text(width=30,height=10)
text.focus()
text.grid(row=3,column=2)

def scale_selected(value):
    print(value)
scale=Scale(from_=0,to=50,command=scale_selected)
scale.grid(row=4,column=2)



def spinbox_selected():
    print(spinbox.get())
spinbox=Spinbox(from_=0,to=50,command=spinbox_selected)
spinbox.grid(row=5,column=2)


def checkbutton_selected():
    print(check_state.get())
    

check_state=IntVar()

checkbutton=Checkbutton(text="check",variable=check_state,command=checkbutton_selected)
checkbutton.grid(row=6,column=2)


window.mainloop()