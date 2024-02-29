from tkinter import*
import tkinter.messagebox as mb
import mysql.connector
from tkcalendar import Calendar, DateEntry
from tkinter import ttk   
import datetime


headlabelfont = ("Calibri", 15, 'bold')
labelfont = ('Calibri', 14,'bold')
entryfont = ('Calibri', 14)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="asmitha"
)    
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS STUDENT_MANAGEMENT (STUDENT_ID INTEGER PRIMARY KEY AUTO_INCREMENT , NAME TEXT, EMAIL TEXT, PHONE_NO TEXT, GENDER TEXT,DOB TEXT, STREAM TEXT)")
def reset_fields():
   global name_strvar, email_strvar, contact_strvar, gender_strvar, dob, stream_strvar
   for i in ['name_strvar', 'email_strvar', 'contact_strvar', 'gender_strvar', 'stream_strvar']:
       exec(f"{i}.set('')")
   dob.set_date(datetime.datetime.now().date())
def add_record():
   global name_strvar, email_strvar, contact_strvar, gender_strvar, dob, stream_strvar
   name = name_strvar.get()
   email = email_strvar.get()
   contact = contact_strvar.get()
   gender = gender_strvar.get()
   DOB = dob.get_date()
   stream = stream_strvar.get()
      
   if not name or not email or not contact or not gender or not DOB or not stream:
       mb.showerror('Error!', "Please enter all the details!")
   else:
       try:
          sql="INSERT INTO STUDENT_MANAGEMENT (NAME, EMAIL, PHONE_NO, GENDER, DOB, STREAM) VALUES (%s,%s,%s,%s,%s,%s)"

          val=(name,email,contact,gender,DOB,stream)

          mycursor.execute(sql,val)
           #mycursor.execute('INSERT INTO STUDENT_MANAGEMENT (NAME, EMAIL, PHONE_NO, GENDER, DOB, STREAM) VALUES (?,?,?,?,?,?)', '(name, email, contact, gender, DOB, stream)')
          print(mycursor)
          mydb.commit()
          mb.showinfo('Record inserted', f"Record of {name} is added")
          reset_fields()
          display_records()
       except:
         # mb.showerror('Wrong type', 'The contact number should be 10 digits')
         pass
#Function to remove record

def remove_record():
   if not tree.selection():
       mb.showerror('Error!', 'Please select an item from the database')
   else:
       current_item = tree.focus()
       values = tree.item(current_item)
       selection = values["values"]
       tree.delete(current_item)
       print(selection[0])
       mycursor.execute('DELETE FROM STUDENT_MANAGEMENT WHERE STUDENT_ID=%d' % selection[0])
       mydb.commit()
       mb.showinfo('Done', 'The record is deleted successfully.')
       

#function to display records
def display_records():
   tree.delete(*tree.get_children())
   mycursor.execute('SELECT * FROM STUDENT_MANAGEMENT')
   print(mycursor)
   data =  mycursor.fetchall()
   for records in data:
       tree.insert('', END, values=records)

def reset_form():
    global tree
    tree.delete(*tree.get_children())



main = Tk()
main.title('Student Management System')
main.geometry('1000x800')
main.resizable(0, 0)

# Creating the background and foreground color variables
lf_bg = '#f28ecb' # bg color for the left_frame


# Creating the StringVar or IntVar variables
name_strvar = StringVar()
email_strvar = StringVar()
contact_strvar = StringVar()
gender_strvar = StringVar()
stream_strvar = StringVar()

# Placing the components in the main window
Label(main, text="STUDENT MANAGEMENT SYSTEM",relief=GROOVE,font=("Calibri", 18, 'bold') , bg='#ad0b5f').pack(side=TOP, fill=X)
left_frame = Frame(main, bg=lf_bg,relief=RIDGE)
left_frame.place(x=0, y=30, height=1000, width=400)
right_frame = Frame(main, bg="black",relief=RIDGE)
right_frame.place(x=400, y=30, height=1000, width=700)


# Placing components in the left frame
Label(left_frame, text="NAME", font=labelfont, bg=lf_bg).place(x=30, y=50)
Label(left_frame, text="CONTACT NO:",font=labelfont,  bg=lf_bg).place(x=30,y=100)
Label(left_frame, text="EMAIL ADDRESS",font=labelfont,  bg=lf_bg).place(x=30,y=150)
Label(left_frame, text="GENDER", font=labelfont, bg=lf_bg).place(x=30, y=200)
Label(left_frame, text="DOB",font=labelfont,  bg=lf_bg).place(x=30, y=250)
Label(left_frame, text="STREAM",font=labelfont, bg=lf_bg).place(x=30, y=300)
Entry(left_frame, width=20, textvariable=name_strvar, font=entryfont).place(x=170, y=50)
Entry(left_frame, width=20, textvariable=contact_strvar, font=entryfont).place(x=170, y=100)
Entry(left_frame, width=20, textvariable=email_strvar, font=entryfont).place(x=170,y=150)
Entry(left_frame, width=20, textvariable=stream_strvar, font=entryfont).place(x=170, y=300)
OptionMenu(left_frame, gender_strvar, 'Male', "Female").place(x=170, y=200, width=70)
dob = DateEntry(left_frame, font=("Arial", 12), width=19)
dob.place(x=170, y=250)
Button(left_frame, text='Submit and Add Record', font=labelfont,bg='#0ff606', command=add_record, width=18).place(x=80, y=380)
def view_record():
   global name_strvar, email_strvar, contact_strvar, gender_strvar, dob, stream_strvar
   if not tree.selection():
       mb.showerror('Error!', 'Please select a record to view')
   else:
        current_item = tree.focus()
        values = tree.item(current_item)
        selection = values["values"]

        name_strvar.set(selection[1]);
        email_strvar.set(selection[2])
        contact_strvar.set(selection[3]);
        gender_strvar.set(selection[4])
        print(selection[5])
        print(selection[5][:4])
        print(selection[5][5:7])
        print(selection[5][8:])
        date = datetime.date(int(selection[5][:4]), int(selection[5][5:7]), int(selection[5][8:]))
        dob.set_date(date);
        print(selection[6])
        stream_strvar.set(selection[6])



Button(left_frame, text='Delete Record', font=labelfont,bg='#ad0b5f',relief=GROOVE, command=remove_record, width=15).place(x=30, y=450)
Button(left_frame, text='View Record', font=labelfont,bg='#ad0b5f',relief=RIDGE, command=view_record, width=15).place(x=200, y=450)
Button(left_frame, text='Clear Fields', font=labelfont,bg='#ad0b5f',command=reset_fields, width=15).place(x=30, y=520)
Button(left_frame, text='Remove database', font=labelfont,bg='#ad0b5f', command=reset_form, width=15).place(x=200, y=520)
# Placing components in the right frame

Label(right_frame, text='Students Records',font=('Calibri', 19,'bold'),relief=GROOVE,bg='#b44389', fg='black').pack(side=TOP, fill=X)
tree = ttk.Treeview(right_frame, height=100, selectmode=BROWSE,
                   columns=('Stud ID', "Name", "Email Addr", "Contact No", "Gender", "Date of Birth", "Stream"))
s = ttk.Style()
s.theme_use('classic')
s.configure('Treeview.Heading', background="green")
ttk.Style().configure("Treeview.Heading", foreground='white')

ttk.Style().configure("Treeview", background="#98fb98",foreground="black", fieldbackground="#A3E5C6",font=('Calibri', 10,'bold'))
X_scroller = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
Y_scroller = Scrollbar(tree, orient=VERTICAL, command=tree.yview)
X_scroller.pack(side=BOTTOM, fill=X)
Y_scroller.pack(side=RIGHT, fill=Y)
tree.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)

tree.heading('Stud ID', text='ID', anchor=CENTER)
tree.heading('Name', text='Name', anchor=CENTER)
tree.heading('Email Addr', text='Email ID', anchor=CENTER)
tree.heading('Contact No', text='Phone No', anchor=CENTER)
tree.heading('Gender', text='Gender', anchor=CENTER)
tree.heading('Date of Birth', text='DOB', anchor=CENTER)
tree.heading('Stream', text='Stream', anchor=CENTER)
tree.column('#0', width=0, stretch=NO)
tree.column('#1', width=40, stretch=NO)
tree.column('#2', width=120, stretch=NO)
tree.column('#3', width=180, stretch=NO)
tree.column('#4', width=60, stretch=NO)
tree.column('#5', width=60, stretch=NO)
tree.column('#6', width=70, stretch=NO)
tree.column('#7', width=120, stretch=NO)
tree.place(y=30, relwidth=1, relheight=0.9, relx=0)
display_records()




main.update()
main.mainloop()
