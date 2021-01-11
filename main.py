from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from Kitap_Ekleme import *
from Kitap_Silme import *
from Kitap_Listele import *
from Kitap_Odunc_Alma import *
from Kitap_Geri_Verme import *

mypass = "root"
mydatabase="python_projesi"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("DiJiTAL KüTüPHANEM")
root.minsize(width=400,height=400)
root.geometry("600x500")

same=True
n=0.25

background_image =Image.open("Giris_Ekrani.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="DiJiTAL KüTüPHANEM", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="KITAP EKLEME",bg='black', fg='white', command=Kitap_Ekleme)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="KITAP SILME",bg='black', fg='white', command=Kitap_Silme)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="KITAP SILME",bg='black', fg='white', command=Kitap_Listele)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="KITAP ÖDÜNÇ ALMA",bg='black', fg='white', command = Kitap_Odunc_Alma)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    
btn5 = Button(root,text="KITAP GERI VERME",bg='black', fg='white', command = Kitap_Geri_Verme)
btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

root.mainloop()
