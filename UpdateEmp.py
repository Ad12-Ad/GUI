from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

mypass = "root"
mydatabase="Project"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()
 
bookTable = "Emp" 

def returnn():
    try:
        en = bookInfo1.get()
        querys='select * from '+bookTable+' where empno='+en
        cur.execute(querys)
        myrecord=cur.fetchone()
        c=cur.rowcount
        if c==-1:
             messagebox.showinfo("Sucess","Empno "+en+" does not exist")
        else:
             mname=myrecord[1]
             mjob=myrecord[2]
             mbasic=myrecord[3]
             print('empno  :',myrecord[0])
             print('name   :',myrecord[1])
             print('job    :',myrecord[2])
             print('basic  :',myrecord[3])
             print('da     :',myrecord[4])
             print('hra    :',myrecord[5])
             print('gross  :',myrecord[6])
             print('tax    :',myrecord[7])
             print('net    :',myrecord[8])
             x=bookInfo2.get()
             print(x)
             if len(x)>0:
                 mname=x
             x=bookInfo3.get()
             x=str(x)
             print(x)
             if len(x)>0:
                 mjob=x

             x=bookInfo4.get()
             print(x)
             if len (x)>0:
                 mbasic=x
             query='update '+bookTable+' set name='+"'"+mname+"'"+','+'job='+"'"+mjob+"'"+','+ 'basicsalary='\
                 +str(mbasic)+' where empno='+en
             print (query)
             cur.execute(query)
             con.commit()
        messagebox.showinfo("Sucess","Emp Information Updated Successfully")
        root.destroy()
    except Exception as e:
        messagebox.showinfo("Error","Something Went Wrong!!")
    
def update(): 
    
    global issueBtn,labelFrame,lb1,bookInfo1,bookInfo2,bookInfo3,bookInfo4,quitBtn,root,Canvas1,status
    
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
    img1 = ImageTk.PhotoImage(background_image)
    
    Canvas1 = Canvas(root)
    
    Canvas1.create_image(600,450,image = img1)      
    Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="UPDATE EMPLOYEE INFORMATION", bg='black', fg='white', font=('Lucida Fax',20))
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
    
    issueBtn = Button(root,text="Update",bg='#d1ccc0', fg='black',command=returnn,font=('Lucida Fax',12))
    issueBtn.place(relx=0.28,rely=0.85, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#aaa69d', fg='black', command=root.destroy,font=('Lucida Fax',12))
    quitBtn.place(relx=0.53,rely=0.85, relwidth=0.18,relheight=0.08)
    
    root.mainloop()