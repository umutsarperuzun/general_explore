import tkinter

window = tkinter.Tk()
window.title("Python Tkinter")
window.minsize(450,300)


# #label
my_label = tkinter.Label(text = "this is a label")
my_label.config(bg="black",fg="white")
my_label.grid(row=0,column=0)


def click_button():
    user_input = my_entry.get()
    print("Button clicked!")
    print(user_input)


#button
my_button = tkinter.Button(text ="this is a button", command=click_button)
# my_button.place(x=225-44.5,y=150-13)
# my_button.update()
# print(my_button.winfo_height())
# print(my_button.winfo_width())
my_button.grid(row=1,column=1)


#entry
my_entry =tkinter.Entry(width = 50)
# my_entry.pack()
my_entry.grid(row=2,column=2)



window.mainloop()