from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def KitapKayýt():
    
    Kitap_ID = bookInfo1.get()
    Kitap_Adi = bookInfo2.get()
    Kitap_Yazari = bookInfo3.get()
    Kitap_Turu = bookInfo4.get()
    Kitap_Turu = status.lower()
    
    insertBooks = "insert into "+bookTable+" values('"+Kitap_ID+"','"+Kitap_Adi+"','"+Kitap_Yazari+"','"+Kitap_Turu+"')"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success',"Kitap Eklendi.")
    except:
        messagebox.showinfo("Error","Kitap Eklenemedi!")
    
    print(Kitap_ID )
    print(Kitap_Adi )
    print(Kitap_Yazari )
    print(Kitap_Turu )


    root.destroy()
    
def KitapEkle(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("DiJiTAL KüTüPHANEM")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    mypass = "root"
    mydatabase="python_projesi"

    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

    bookTable = "Kitaplar" 

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="KITAP EKLEME", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    lb1 = Label(labelFrame,text="KITAP ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    lb2 = Label(labelFrame,text="KITAP ADI : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    lb3 = Label(labelFrame,text="KITAP YAZARI : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
    lb4 = Label(labelFrame,text="KITAP TÜRÜ : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
        
    SubmitBtn = Button(root,text="KAYDET",bg='#d1ccc0', fg='black',command=KitapKayýt)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="ÇIKIÞ",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()