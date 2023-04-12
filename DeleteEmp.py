from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector

mypass = "root"
mydatabase="Project"

con = mysql.connector.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()
 
bookTable = "Emp"

def deleteBook():
    
    bid= bookInfo1.get()
    deleteSql = "delete from "+bookTable+" where Empno='"+bid+"'"
    try:
        cur.execute(deleteSql)
        con.commit()
        messagebox.showinfo('Success',"Employee Record Deleted Successfully")
    except Exception as e:
        print("Error","Please check Employee No!!")

    bookInfo1.delete(0, END)
    root.destroy()
    
def delete(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root
    
    root = Toplevel()
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
    
    Canvas1.create_image(600,450,image = img)      
    Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="DELETE EMPLOYEE RECORD", bg='black', fg='white',font=('Lucida Fax',20))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.25,rely=0.35,relwidth=0.5,relheight=0.2)   

    lb2 = Label(labelFrame,text="Enter the Employee No", bg='black', fg='white',font=('Lucida Fax',14))
    lb2.place(relx=0.33,rely=0.2)
        
    bookInfo1 = Entry(labelFrame,justify='center', font=('Lucida Fax',15))
    bookInfo1.place(relx=0.2,rely=0.5, relwidth=0.65,relheight=0.23)

    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteBook,font=('Lucida Fax',12))
    SubmitBtn.place(relx=0.28,rely=0.7, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy,font=('Lucida Fax',12))
    quitBtn.place(relx=0.53,rely=0.7, relwidth=0.18,relheight=0.08)
    
    root.mainloop()