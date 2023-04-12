from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
from tkinter import ttk 

mypass = "root"
mydatabase="Project"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

bookTable = "Emp" 

def View(): 
    
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
    headingFrame1.place(relx=0.33,rely=0.01,relwidth=0.35,relheight=0.085)
        
    headingLabel = Label(headingFrame1, text="View Employee data", bg='black', fg='white',font=('Lucida Fax',20))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.11,relwidth=0.8,relheight=0.78)
    y = 0.15
    
    Label(labelFrame,text="%-20s%-40s%-35s%-27s%-21s%-25s%-30s%-20s%-30s"%('Emp No.'
    ,'Name','Job','Basic Salary','DA','HRA','Gross Salary','Tax','Net Salary')
    ,bg='black',fg='white').place(relx=0.1,rely=0.05)
    Label(labelFrame, text="----------------------------------------------------------\
-------------------------------------------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.09,rely=0.1)
    getBooks = "select * from "+bookTable+" order by name"
    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
            Label(labelFrame, text=str(i[0]),bg='black',fg='white').place(relx=0.11,rely=y)
            Label(labelFrame, text=str(i[1]),bg='black',fg='white').place(relx=0.17,rely=y)
            Label(labelFrame, text=str(i[2]),bg='black',fg='white').place(relx=0.30,rely=y)
            Label(labelFrame, text=float(i[3]),bg='black',fg='white').place(relx=0.42,rely=y)
            Label(labelFrame, text=i[4],bg='black',fg='white').place(relx=0.50,rely=y)
            Label(labelFrame, text=i[5],bg='black',fg='white').place(relx=0.57,rely=y)
            Label(labelFrame, text=i[6],bg='black',fg='white').place(relx=0.67,rely=y)
            Label(labelFrame, text=i[7],bg='black',fg='white').place(relx=0.755,rely=y)
            Label(labelFrame, text=float(i[8]),bg='black',fg='white').place(relx=0.829,rely=y)
            y += 0.05
    except:
        messagebox.showinfo("Error","Failed to fetch files from database")
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy,font=('Lucida Fax',14))
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()