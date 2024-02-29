from tkinter import*
import os
import mysql.connector
import tkinter.messagebox as mm
from PIL import ImageTk, Image
def login():
    global login_screen
    login_screen=Tk()
    login_screen.title('Login')
    login_screen.geometry('500x400')
    global Username_verify
    global Password_verify
    global Username_login_entry
    global Password_login_entry

    Username_verify=StringVar()
    Password_verify=StringVar()
    img = Image.open("green.jpg") 
    img = ImageTk.PhotoImage(img)
    panel = Label(login_screen, image = img)
    panel.image = img
    panel.grid(row = 2)

    Label(login_screen,text="LOGIN PORTAL",bg="#ccc56e",font=('Ariel',26)).place(x=150,y=30)
    Label(login_screen,text='USERNAME',bg='#ccc56e',font=('Ariel',12,'bold')).place(x=80,y=180)
    Username_login_entry=Entry(login_screen,textvariable=Username_verify,width='40').place(x=200 , y=183)
    Label(login_screen,text='PASSWORD',bg='#ccc56e',font=('Ariel',12,'bold')).place(x=80,y=230)
    Password_login_entry=Entry(login_screen,textvariable=Password_verify,show='*',width='40').place(x=200 , y=233)
    Button(login_screen,text='LOGIN',bg='cyan',width='12',activebackground='brown',font=('Ariel',13,'bold'),command=submit).place(x=280, y=285)
def submit():
    mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='Asmitha'
    )
    mycursor=mydb.cursor()
    if Username_verify.get()=="" or Password_verify.get()=="":
       Label(login_screen,text=" Please complete the required field",fg='Red',font=('Calibri',16)).place(x=130,y=140)
    else:
        mycursor.execute('SELECT*FROM login WHERE username=%s AND password=%s',(Username_verify.get(),Password_verify.get()))
    if mycursor.fetchone():
     
     mm.showinfo("Message","Login successful")  
     import student 
     mycursor.close()
     mydb.close
     
    else:
        user_not_found()
def user_not_found():
     mm.showerror("Error","Invalid Username and Password")


login()
        
     
      
