from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def EmpRegister():
    
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = bookInfo4.get()
        
    if author.upper()=="OFFICER":
        mda=float(status)*0.5
        mhra=float(status)*0.35
        mtax=float(status)*0.2
    elif author.upper()=="MANAGER":
        mda=float(status)*0.45
        mhra=float(status)*0.30
        mtax=float(status)*0.15
    else:
        mda=float(status)*0.40
        mhra=float(status)*0.25
        mtax=float(status)*0.1
    #calculating gross salary
    mgross=float(status)+mda+mhra
    #calculating net salary
    mnet=mgross-mtax
    
    insertBooks = "insert into "+bookTable+" values("+str(bid)+",'"+\
                   str(title)+"','"+str(author)+"',"+str(status)+","+\
                       str(mda)+","+str(mhra)+","+str(mgross)+","+str(mtax)+","+str(mnet)+")"
    
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo("Success","Emp Information added successfully")
    except Exception as e:
        messagebox.showinfo("Error","Can't add data into Database")

    root.destroy()
    
def addEmp(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root
    
    root = Toplevel()
    root.title("Employee Managment System")
    root.minsize(width=400,height=400)

    mypass = "root"
    mydatabase="Project"

    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

    bookTable = "Emp"
    
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

    headingLabel = Label(headingFrame1, text="ADD EMPLOYEE PROFILE", bg='black', fg='white',font=('Lucida Fax',20))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.202,rely=0.4,relwidth=0.6,relheight=0.4)
        
    lb1 = Label(labelFrame,text="Employee No       :", bg='black', fg='white',font=('Lucida Fax',12))
    lb1.place(relx=0.08,rely=0.2, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame,font=('Lucida Fax',12))
    bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.6, relheight=0.08)
        
    lb2 = Label(labelFrame,text="Employee Name  :", bg='black', fg='white',font=('Lucida Fax',12))
    lb2.place(relx=0.08,rely=0.36, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame,font=('Lucida Fax',12))
    bookInfo2.place(relx=0.3,rely=0.36, relwidth=0.6, relheight=0.08)
        
    lb3 = Label(labelFrame,text="Job Post               :", bg='black', fg='white',font=('Lucida Fax',12))
    lb3.place(relx=0.08,rely=0.52, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame,font=('Lucida Fax',12))
    bookInfo3.place(relx=0.3,rely=0.52, relwidth=0.6, relheight=0.08)

    lb4 = Label(labelFrame,text="Salary                  :", bg='black', fg='white',font=('Lucida Fax',12))
    lb4.place(relx=0.08,rely=0.68, relheight=0.08)
        
    bookInfo4 = Entry(labelFrame,font=('Lucida Fax',12))
    bookInfo4.place(relx=0.3,rely=0.68, relwidth=0.6, relheight=0.08)

    SubmitBtn = Button(root,text="ADD",bg='#d1ccc0', fg='black',command=EmpRegister,font=('Lucida Fax',12))
    SubmitBtn.place(relx=0.28,rely=0.85, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy,font=('Lucida Fax',12))
    quitBtn.place(relx=0.53,rely=0.85, relwidth=0.18,relheight=0.08)
    
    root.mainloop()