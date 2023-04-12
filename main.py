import tkinter
from PIL import ImageTk,Image
import mysql.connector
from tkinter import messagebox
from AddEmp import *
from DeleteEmp import *
from ViewEmp import *
from UpdateEmp import *

def start():
    try:
        mypass = entry.get()
        mydatabase="Project"
        bookTable = "Emp"
        con = mysql.connector.connect(host="localhost",user="root",password=mypass,database=mydatabase)
        cur = con.cursor()
        root1.destroy()
    except Exception as e:
        messagebox.showinfo("Alert","Invalid Security Key")
    
    query="create table if not exists "+bookTable+"\
          (empno int primary key,\
          name char(30) not null,\
          job char(20),\
          basicsalary int,\
          DA float,\
          HRA float,\
          grosssalary float,\
          tax float,\
          netsalary float)"
    cur.execute(query)
    
    root = tkinter.Tk()
    root.title("Employee Managment System")
    root.minsize(width=400,height=400)
    
    # Take n greater than 0.25 and less than 5
    same=True
    n=1.00
    
    # Adding a background image
    background_image =Image.open("ABC.jpg")
    [imageSizeWidth, imageSizeHeight] = background_image.size
    
    newImageSizeWidth = int(imageSizeWidth*n)
    if same:
        newImageSizeHeight = int(imageSizeHeight*n) 
    else:
        newImageSizeHeight = int(imageSizeHeight/n) 
        
    background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(background_image)
    
    Canvas1 = Canvas(root)
    Canvas1.create_image(600,450,image=img)      
    Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)
    
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    
    headingLabel = Label(headingFrame1, text="Welcome to \n Employee Management Portal", bg='black', fg='white', font=('Lucida Fax',20))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    btn1 = Button(root,text="Add Employee Details",bg='black', fg='white', command=addEmp, font=('Lucida Fax',12))
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
        
    btn2 = Button(root,text="Delete Employee data",bg='black', fg='white', command=delete,font=('Lucida Fax',12))
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
        
    btn3 = Button(root,text="View Employee List",bg='black', fg='white', command=View,font=('Lucida Fax',12))
    btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
        
    btn4 = Button(root,text="Update Employee Data",bg='black', fg='white', command = update,font=('Lucida Fax',12))
    btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    
    btn5 = Button(root,text="Exit",bg='black', fg='white', command=root.destroy,font=('Lucida Fax',12))
    btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)
        
    root.mainloop()

global entry
root1 = tkinter.Tk()
root1.title("User Verification")

# Take n greater than 0.25 and less than 5
same=True
n=1.00

# Adding a background image
background_image =Image.open("Back.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root1)
    
Canvas1.create_image(600,450,image=img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root1,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.24,rely=0.2,relwidth=0.52,relheight=0.16)

lbl = Label(root1, text='*** PLEASE ENTER THE SECURITY KEY ***',  bg='black', fg='white', font=('Lucida Fax',20))
entry = Entry(root1, width=20,justify='center', font=('Lucida Fax',20),show="*") 
btn = Button(root1, text='Submit', bg='#f7f1e3', fg='black',font=('Lucida Fax',16) ,command=start)

lbl.place(relx=0.25,rely=0.21,relwidth=0.5,relheight=0.14)
entry.place(relx=0.3,rely=0.45,relwidth=0.4,relheight=0.09) 
btn.place(relx=0.4,rely=0.6, relwidth=0.18,relheight=0.08) 
entry.focus()

root1.mainloop()