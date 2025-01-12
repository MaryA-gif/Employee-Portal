## LOGIN PAGE

from customtkinter import*
from PIL import Image #PIL Python Image Libary
from tkinter import messagebox
def login():
    username = usernameEntry.get()
    password = passwrdEntry.get()
    if usernameEntry.get()=='' or passwrdEntry.get()=='':
        messagebox.showerror('Error','All feilds are required :) THANK YOU')
    elif passwrdEntry.get()=='12&34':
        messagebox.showinfo('Success','WELCOME')
        root.destroy() # this method used for close
        import emsys
    else:
        messagebox.showerror('Error','Wrong password')
root = CTk()
root.geometry("930x600")

root.title("Welcome")
image = CTkImage(Image.open('log.jpg'),size=(930,600)) #pip intall pillow
imageLabel = CTkLabel(root,image=image,text=" ")
imageLabel.place(x=500,y=50)

img = CTkImage(Image.open('user.jpg'),size=(200,100))
imgLable = CTkLabel(root,image=img,text=' ').place(x=200,y=100)

#LABEL
headingLabel = CTkLabel(root,text="EMPLOYEE PORTAL",font=('Goudy Old Style',20,'bold'),text_color='dark blue')
headingLabel.place(x=100,y=200)

# ENTRY
usernameEntry = CTkEntry(root,placeholder_text ='Enter Your Username',width=180)
usernameEntry.place(x=200,y=250)
passwrdEntry = CTkEntry(root,placeholder_text="Enter Your Password",show='*',width=180)
passwrdEntry.place(x=200,y=300)

# BUTTON
loginbutton = CTkButton(root,text='LOGIN',bg_color='#0080c0',font=('Gloudy Old Style',14,'bold'),text_color='White',cursor='hand2',command=login)
loginbutton.place(x=220,y=350)

root.mainloop()
