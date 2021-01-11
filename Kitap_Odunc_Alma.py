from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

mypass = "root"
mydatabase="python_projesi"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

issueTable = "Kitap_Listesi" 
bookTable = "Kitaplar"
    
allBid = [] 

def KitapOduncVer():
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
    Kitap_ID = inf1.get()
    Kitap_Durum = inf2.get()

    issueBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()
    
    
    extractBid = "select bid from "+bookTable
    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            allBid.append(i[0])
        
        if Kitap_ID in allBid:
            checkAvail = "select status from "+bookTable+" where bid = '"+Kitap_ID+"'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]
                
            if check == 'avail':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error","Kitap ID si bulunamadý!")
    except:
        messagebox.showinfo("Error","Kitap ID leri getirilemedi!")
    
    issueSql = "insert into "+issueTable+" values ('"+Kitap_ID+"','"+Kitap_Durum+"')"
    show = "select * from "+issueTable
    
    updateStatus = "update "+bookTable+" set status = 'Verildi' where bid = '"+Kitap_ID+"'"
    try:
        if bid in allBid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success',"Kitap Verildi.")
            root.destroy()
        else:
            allBid.clear()
            messagebox.showinfo('Message',"Kitap Önceden verilmiþtir!")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error","Girilen deðer yanlýþ, tekrar deneyin")
    
    print(bid)
    print(issueto)
    
    allBid.clear()
    
def OduncAl(): 
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
    root = Tk()
    root.title("DiJiTAL KüTüPHANEM")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="KITAP ÖDÜNÇ ALMA", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  

    lb1 = Label(labelFrame,text="KITAP ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2)
        
    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    lb2 = Label(labelFrame,text="KITAP DURUMU: ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.4)
        
    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3,rely=0.4, relwidth=0.62)
    
    issueBtn = Button(root,text="KAYDET",bg='#d1ccc0', fg='black',command=KitapOduncVer)
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="ÇIKIÞ",bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()