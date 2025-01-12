## EMPLOYEE PORTAL
from customtkinter import *
from PIL import Image
import tkinter as tk
from tkinter import ttk,messagebox
from customtkinter import CTkRadioButton

from customtkinter import CTkLabel
from tkinter import Tk, PhotoImage
from tkinter import IntVar
import datab
# FUNCTION PART

def exit(): #used to exit window directly
   if messagebox.askyesno("Confirm Exit", "Are you sure you want to exit?"):
       window.destroy()
   
def delete_all(): #used to delete all the records from database
   result=messagebox.askyesno('Confirm','Do you really want to delete all the records?')
   if result:
      datab.deleteall_records()
   else:
      pass

def show_all(): #used to activate the showall button 
   treeview_data()
   searchEntry.delete(0,END)
   searchbox.set('Search By')
   
def search_employee(): #used to activate the search button
   if searchEntry.get()== "":
      messagebox.showerror("Error","Please enter value to search")
   elif searchbox.get()=='Search By':
      messagebox.showerror("Error","Please select search option")
   else:
      searched_data=datab.search(searchbox.get(),searchEntry.get())
      #print(searched_data)
      tree.delete(*tree.get_children())  #this line for clear prevoius data
   for employee in searched_data:
      tree.insert('', END, values=(employee['Id'], employee['Name'], employee['Phone'], employee['Role'], employee['Gender'], employee['Experenice']))

def delete_employee(): # used to delete the selected data from the table
   selected_item=tree.selection()
   if not selected_item:
      messagebox.showerror("Error","Select an row to delete")
   else:
      datab.delete(idEntry.get())
      treeview_data()
      clear()
      messagebox.showerror('Error','Selected item is deleted')

def update_employee(): # used to update the selected data
   selected_item=tree.selection()
   if not selected_item:
      messagebox.showerror("Error","Select an row to update")
   else:
      id = idEntry.get()
      name = nameEntry.get()
      phone = phoneEntry.get()
      role = rolebox.get()
      gender = gen.get()
      experience = expComboBox.get()
      
      #print(f"Updating employee: ID={id}, Name={name}, Phone={phone}, Role={role}, Gender={gender}, Experience={experience}")
      datab.update(idEntry.get(), nameEntry.get(), phoneEntry.get(), rolebox.get(), gen.get(), expComboBox.get())
      treeview_data() #used to react update actions in tree view table
      clear()
      messagebox.showinfo("Success","Data is update successfully")

def selection(event):
   selected_item=tree.selection()
   #print(selected_item)
   if selected_item:
      row=tree.item(selected_item)['values']
      clear()
      idEntry.insert(0,row[0])
      nameEntry.insert(0,row[1])
      phoneEntry.insert(0,row[2])
      rolebox.set(row[3])
      gen.set(row[4])
      expComboBox.set(row[5])
      #print(row)
def clear(value=False):
   if value:
      tree.selection_remove(tree.focus())
   idEntry.delete(0,END)
   nameEntry.delete(0,END)
   phoneEntry.delete(0,END)
   rolebox.set('Marketing')
   gen.set(0)
   expComboBox.set('0')
def treeview_data(): # used to display the sql database table in the GUI
   employees=datab.fetch_employees()
   tree.delete(*tree.get_children())
   for employee in employees:
      tree.insert('', END, values=(employee['Id'], employee['Name'], employee['Phone'], employee['Role'], employee['Gender'], employee['Experenice']))
def add_employee():
   if idEntry.get() ==' ' or nameEntry.get() =='' or phoneEntry.get() =='' :
      messagebox.showerror('Error','All fileds are required')

   elif datab.id_exist(idEntry.get()):
     messagebox.showerror('Error','Employee ID already exists') 

   elif not idEntry.get().startswith('EMP'):
      messagebox.showerror('Error','Employee ID should start with EMP')

   else:
      result = datab.insert(idEntry.get(),nameEntry.get(),phoneEntry.get(),rolebox.get(),gen.get(),expComboBox.get())
      treeview_data()  # Call to update the Treeview with new data
      clear()
      messagebox.showinfo('Success','Data is added')
      

# GUI PART
window = CTk()
window.title("Employment Management System")
window.geometry('1350x700+100+100')
window.resizable(0,0) # used to off the resizable box
window.configure(fg_color="#400080")

# IMAGE
logo = CTkImage(Image.open('po.jpg'),size=(1350,300)) #pip intall pillow
logoLabel = CTkLabel(window,image=logo, text=" ")
logoLabel.grid(row=0,column=1,columnspan=2)

# FRAME-LEFT
leftFrame=CTkFrame(window,fg_color='#400080')
leftFrame.grid(row=2,column=1)
   # ID LABEL
idLabel = CTkLabel(leftFrame,text='ID',font=('arial',18,'bold'),text_color='white')
#padx used to horzin give space before (0,20)& after the label between entry, pady are used in vertical
idLabel.grid(row=0,column=0,padx=(20),pady=(15),sticky='W') 
   # ID ENTRY
idEntry = CTkEntry(leftFrame,placeholder_text='Enter your id',font=('arial',15),width=180,fg_color="#400080",text_color="white")  
idEntry.grid(row=0,column=1)
   # NAME LABEL
nameLabel = CTkLabel(leftFrame,text='NAME',font=('arial',18,'bold'),text_color='white')
nameLabel.grid(row=1,column=0,padx=(20),pady=(15),sticky='W') 
   # NAME ENTRY
nameEntry = CTkEntry(leftFrame,placeholder_text='Enter your name',font=('arial',15),width=180,fg_color="#400080",text_color="white")
nameEntry.grid(row=1,column=1)
   # PHONE LABEL
phoneLabel = CTkLabel(leftFrame,text='PHONE NUMBER',font=('arial',18,'bold'),text_color='white')
phoneLabel.grid(row=2,column=0,padx=(20),pady=(15),sticky='W') 
   # PHONE ENTRY
phoneEntry = CTkEntry(leftFrame,placeholder_text='Enter your phone number',font=('arial',15),width=180,fg_color="#400080",text_color="white")
phoneEntry.grid(row=2,column=1)

# BUTTON
   # RADIO BUTTON
gen = IntVar()
radioLabel = CTkLabel(leftFrame,text='GENDER',font=('arial',18,'bold'),text_color='white')
radioLabel.grid(row=3,column=0,padx=(20),pady=(15),sticky='W')
malebutton = CTkRadioButton(leftFrame,text = 'MALE',variable=gen,value=1,font=('arial',18,'bold'),text_color="white")
malebutton.grid(row=3,column=1)
femalebutton = CTkRadioButton(leftFrame,text = 'FEMALE',variable=gen,value=2,font=('arial',18,'bold'),text_color="white")
femalebutton.grid(row=3,column=2)

# COMBO BOX
  # ROLE BOX
roleLabel = CTkLabel(leftFrame,text='ROLE',font=('arial',18,'bold'),text_color='white')
roleLabel.grid(row=4,column=0,padx=(20),pady=(15),sticky='W') 
role_options = ['Marketing','HR','Sales','Back-end Developer','Front-end Developer','Admin','Front office',
                'Business Analyst','Cloud Architect','Data Scientist','Data Engineer','Deveops','Network Engineer']
rolebox = CTkComboBox(leftFrame,values=role_options,font=('arial',15),width=180,fg_color="#400080",text_color="white")
rolebox.grid(row=4,column=1)
 
# Label for experience selection
Lb = CTkLabel(leftFrame, text="EXPERENICE", font=('arial', 18, 'bold'),text_color='white')
Lb.grid(row=5, column=0, padx=(20), pady=(15),sticky='W')

# Dropdown options for experience selection
exp_options = ["0", "1", "2","3","4","5","6","7+","8+","9+"]
expComboBox = CTkComboBox(leftFrame, values=exp_options, font=('arial', 15),width=180,fg_color="#400080",text_color="white")
expComboBox.grid(row=5, column=1)

# FRAME-RIGHT
rightFrame=CTkFrame(window)
rightFrame.grid(row=2,column=2)

# SEARCH 
search_options = ['ID','NAME','PHONE','ROLE','GENDER','EXPERENICE']
searchbox = CTkComboBox(rightFrame,values=search_options,state='readonly',font=('arial',15),width=180,fg_color="#400080",text_color="white")
searchbox.grid(row=0,column=0)
searchbox.set('Search By')
   # ENTRY
searchEntry = CTkEntry(rightFrame)
searchEntry.grid(row=0,column=1)
   # BUTTON
searchbutton = CTkButton(rightFrame,text='SEARCH',width=100,font=('arial',15),fg_color="#400080",text_color="white",command=search_employee).grid(row=0,column=2)
showallbutton = CTkButton(rightFrame,text='SHOW ALL',width=100,font=('arial',15),fg_color="#400080",text_color="white",command=show_all).grid(row=0,column=3)

tree = ttk.Treeview(rightFrame,height=13)
tree.grid(row=1,column=0,columnspan=4) 

tree['columns']=('Id','Name','Phone','Role','Gender','Experenice')
tree.heading('Id',text='ID')
tree.heading('Name',text='NAME')
tree.heading('Phone',text='PHONE')
tree.heading('Role',text='ROLE')
tree.heading('Gender',text='GENDER')
tree.heading('Experenice',text='EXPERENICE')

tree.config(show='headings') # only show the headings
tree.column('Id',width=100)
tree.column('Name',width=160)
tree.column('Phone',width=180)
tree.column('Role',width=150)
tree.column('Gender',width=110)
tree.column('Experenice',width=140)

# STYLE THE FONT
style=ttk.Style()
style.configure('Treeview.Heading',font=('arial',14,'bold'))
style.configure('Treeview',font=('arial',12),rowheight=30,fg_color='#400080',text_color='white')

scrollbar = ttk.Scrollbar(rightFrame,orient=VERTICAL,command=tree.yview)
scrollbar.grid(row=1,column=4,sticky='ns')
# NEW FRAME FOR BUTTONS
buttonFrame=CTkFrame(window,fg_color='#400080')
buttonFrame.grid(row=3,column=1,columnspan=2)
   # NEW EMPLOYEE  
newButton = CTkButton(buttonFrame,text='NEW EMPLOYEE',font=('arial',12,'bold'),width=140,corner_radius=15,fg_color='#400080',text_color='white',command=lambda: clear(True)) #lam func used to only called when we click new
newButton.grid(row=0,column=0,pady=5)
   # ADD EMPLOYEE 
addButton = CTkButton(buttonFrame,text='ADD EMPLOYEE',font=('arial',12,'bold'),width=140,corner_radius=15,fg_color='#400080',text_color='white',command=add_employee)
addButton.grid(row=0,column=1,padx=5,pady=5)
   # UPDATE EMPLOYEE BUTTON
updateButton = CTkButton(buttonFrame,text='UPDATE EMPLOYEE',font=('arial',12,'bold'),width=140,corner_radius=15,fg_color='#400080',text_color='white',command=update_employee)
updateButton.grid(row=0,column=2,padx=5,pady=5)
   # DELETE EMPLOYEE BUTTON
deleteButton = CTkButton(buttonFrame,text='DELETE EMPLOYEE',font=('arial',12,'bold'),width=140,corner_radius=15,fg_color='#400080',text_color='white',command=delete_employee)
deleteButton.grid(row=0,column=3,padx=5,pady=5)
   # DELETE ALL EMPLOYEE BUTTON
deleteallButton = CTkButton(buttonFrame,text='DELETE ALL',font=('arial',12,'bold'),width=140,corner_radius=15,fg_color='#400080',text_color='white',command=delete_all)
deleteallButton.grid(row=0,column=4,padx=5,pady=5)

ExitButton = CTkButton(buttonFrame,text='EXIT',font=('arial',12,'bold'),width=140,corner_radius=15,fg_color='#400080',text_color='white',command=exit)
ExitButton.grid(row=0,column=5,padx=5,pady=5)

treeview_data()

window.bind('<ButtonRelease>',selection)

window.mainloop()
