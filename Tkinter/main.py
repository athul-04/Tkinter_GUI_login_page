from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import sqlite3

window=Tk()
window.title("Login page")
window.geometry("700x700")
window.config(bg="blue")




##Database things:

conn=sqlite3.connect("rough.db")
conn.execute("create table if not exists create_users (id INT AUTO_INCREMENT PRIMARY KEY,name varchar(255),gmail varchar(255),password varchar(255))")
conn.execute("create table if not exists users (id INT AUTO_INCREMENT PRIMARY KEY,username varchar(255),gmail varchar(255),password varchar(255))")
def clear():
    user_entry.delete(0,END)
    pass_entry.delete(0,END)
    gmail_entry.delete(0,END)


def login():
    cre_name=[]
    cre_password=[]
    query="SELECT NAME,PASSWORD FROM CREATE_USERS"
    cursor=conn.execute(query)
    for x in cursor:
        cre_name.append(x[0])
        cre_password.append(x[1])
    name=user_entry.get()
    gmail=gmail_entry.get()
    password=pass_entry.get()
    if name=="" or gmail=="" or password=="":
        messagebox.showwarning("showinfo","Insufficient Details")
        return
    if name in cre_name:
        index=cre_name.index(name)
        if cre_password[index]==password:
            messagebox.showinfo("showinfo","Login sucessfull")
        else:
            messagebox.showinfo("showinfo","Incorrect Password")
            return
    else:
        user_entry.delete(0,END)
        pass_entry.delete(0,END)
        gmail_entry.delete(0,END)

        messagebox.showinfo("showinfo","No account found")
    
    #print(name,gmail,password)

    

    # sql="INSERT INTO USERS(username,gmail,password) VALUES(?,?,?)"
    # entries=(name,gmail,password)
    # conn.execute(sql,entries)
    # conn.commit()
    # messagebox.showinfo("showinfo","Login sucessfull!")


###########################################################
def create():
    user_entry.delete(0,END)
    pass_entry.delete(0,END)
    gmail_entry.delete(0,END)
    window2=Tk()
    window2.title("Account Creation Page")
    window2.geometry("700x700")
    window2.config(bg="blue")
    label2=Label(master=window2,text="Welcome to the Account Creation page",font=("Times",26,"bold"),bg="blue")
    label2.place(x=55,y=35)
    label2.config(fg="white")
    def clear2():
        name2_entry.delete(0,END)
        pass2_entry.delete(0,END)
        re_pass2_entry.delete(0,END)
        gmail2_entry.delete(0,END)
    
    def create2():
        name2=name2_entry.get()
        gmail2=gmail2_entry.get()
        password2=pass2_entry.get()
        retype_password2=re_pass2_entry.get()
        #print(name2,gmail,password)
        if name2=="" or gmail2=="" or password2=="":
            messagebox.showwarning("showinfo","Insufficient Details")
            return

        if password2!=retype_password2:
            messagebox.showwarning("showinfo","Password dosent match!!")
            clear2()



        else:
            sql2="INSERT INTO create_users(name,gmail,password) VALUES(?,?,?)"
            entries2=(name2,gmail2,password2)
            conn.execute(sql2,entries2)
            conn.commit()
            messagebox.showinfo("showinfo","Account Created Sucessfully!")
            


        

    #username2-label

    name2_label=Label(master=window2,text="Name          :",font=("verdana",16,"roman"),bg="blue")
    name2_label.place(x=142,y=180)
    name2_label.config(fg="white")

    #username2-Entry

    name2_entry=Entry(master=window2,width=30,bd=2)
    name2_entry.place(x=340,y=185,height=25)

    #gmail-label
    gmail2_label=Label(master=window2,text="Gmail         :",font=("verdana",16,"roman"),bg="blue")
    gmail2_label.place(x=144,y=250)
    gmail2_label.config(fg="white")



    #gmail-entry
    gmail2_entry=Entry(master=window2,width=30,bd=2)
    gmail2_entry.place(x=340,y=255,height=25)


    #password-label

    pass2_label=Label(master=window2,text="Password    :",font=("verdana",16,"roman"),bg="blue")
    pass2_label.place(x=140,y=320)
    pass2_label.config(fg="white")


    #password-entry
    pass2_entry=Entry(master=window2,show="*",width=30,bd=2)
    pass2_entry.place(x=340,y=325,height=25)

    #re-password-label

    re_pass2_label=Label(master=window2,text="Retype-Pass:",font=("verdana",16,"roman"),bg="blue")
    re_pass2_label.place(x=137,y=390)
    re_pass2_label.config(fg="white")


    #re-password-entry
    re_pass2_entry=Entry(master=window2,show="*",width=30,bd=2)
    re_pass2_entry.place(x=340,y=395,height=25)

    #clear-button

    clear_btn=Button(master=window2,text="Clear",width=8,bd=3,bg="blue2",fg="white",activebackground="yellow",command=clear2)
    clear_btn.place(x=300,y=500,height=30)



    #create-account-button

    create_acc_btn=Button(master=window2,text="Create",width=22,bd=3,bg="blue2",fg="white",font=("verdana",10,"bold"),activebackground="white", command=create2)
    create_acc_btn.place(x=238,y=600,height=30)

    window2.mainloop()
    


#welcome portal
label1=Label(master=window,text="Welcome to the Login page",font=("Times",26,"bold"),bg="blue")
label1.place(x=135,y=35)
label1.config(fg="white")

#username-label

user_label=Label(master=window,text="Username   :",font=("verdana",16,"roman"),bg="blue")
user_label.place(x=140,y=180)
user_label.config(fg="white")

#username-Entry

user_entry=Entry(master=window,width=30,bd=2)
user_entry.place(x=340,y=185,height=25)

#gmail-label
gmail_label=Label(master=window,text="Gmail         :",font=("verdana",16,"roman"),bg="blue")
gmail_label.place(x=144,y=250)
gmail_label.config(fg="white")



#gmail-entry
gmail_entry=Entry(master=window,width=30,bd=2)
gmail_entry.place(x=340,y=255,height=25)


#password-label

pass_label=Label(master=window,text="Password    :",font=("verdana",16,"roman"),bg="blue")
pass_label.place(x=140,y=320)
pass_label.config(fg="white")


#password-entry
pass_entry=Entry(master=window,show="*",width=30,bd=2)
pass_entry.place(x=340,y=325,height=25)

#clear-button

clear_btn=Button(master=window,text="Clear",width=8,bd=3,bg="blue2",fg="white",activebackground="yellow",command=clear)
clear_btn.place(x=300,y=440,height=30)


#Login-Button

login_btn=Button(master=window,text="Login",width=15,bd=3,bg="blue2",fg="white",font=("verdana",10,"bold"),activebackground="yellow", command=login)
login_btn.place(x=265,y=500,height=30)


#create-account-button

create_acc_btn=Button(master=window,text="Create Account",width=22,bd=3,bg="blue2",fg="white",font=("verdana",10,"bold"),activebackground="white", command=create)
create_acc_btn.place(x=238,y=600,height=30)


################################################################################

#welcome portal

window.mainloop()
