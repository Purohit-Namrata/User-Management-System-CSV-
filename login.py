import tkinter as tk
from tkinter import messagebox
import csv
from PIL import ImageTk,Image
import bcrypt       
import os 
import pandas as pd
import re

def login():
    def adminlogin():
        def adminpage():
            
            def viewall():
                if os.path.exists("userdb.csv"):
                    with open("userdb.csv", "r") as file:
                        reader = csv.reader(file)
                        users = [row for row in reader]
                        if users:
                            users_info = "\n".join(["USERNAME: {}, PASSWORD: {}, EMAIL: {}".format(*book) for book in users])
                            messagebox.showinfo("Users List", users_info)
                        else:
                            messagebox.showinfo("Users List", "No user found.")
                else:
                    messagebox.showinfo("Users List", "The user list is empty.")
            
            
            def deleteacc():
                def deleterow():
                    un=e1.get()
                    df = pd.read_csv('C:/Users/BLAUPLUG/Documents/Python_programs/User Management System/userdb.csv', index_col='username')
                    df = df.drop(un)
                    df.to_csv('C:/Users/BLAUPLUG/Documents/Python_programs/User Management System/userdb.csv', index=True)
                
                    messagebox.showinfo("Success","Account deleted")
                lbl=tk.Label(root1,text="Enter username to delete account",fg="Brown")
                lbl.grid(row=6,column=0)
                e1=tk.Entry(root1)
                e1.grid(row=6,column=1)
                
                b1=tk.Button(root1,text="Delete",command=deleterow,bg="Brown",fg="White")
                b1.grid(row=8,column=1)
                

            def logout():
                answer=messagebox.askyesno("Sure?","Are you sure you want to logout?")
                if answer:
                    root1.destroy()
                    messagebox.showinfo("Success","Admin successfully logged out")
                    login()
                else:
                    adminpage()
            
            root1=tk.Tk()
            root1.geometry("400x400")
            root1.title("Admin page")
            root1.configure(bg="orange")
            l1=tk.Label(root1, text="Welcome, Admin!",font=10,fg="Brown")
            l1.grid(row=1,column=1)
            b1=tk.Button(root1, text="View all users",command=viewall,fg="white",bg="brown")
            b1.grid(row=3,column=0)
            b2=tk.Button(root1,text="Delete accounts",command=deleteacc,fg="white",bg="brown")
            b2.grid(row=3,column=1)
            b3=tk.Button(root1, text="Logout",command=logout,fg="white",bg="brown")
            b3.grid(row=3,column=2)
            root1.mainloop()

        username=un_entry.get()
        pwd=pwd_entry.get()
        if username=="" or pwd=="":
            messagebox.showinfo("Insert status","All fields are required")
        
        if username=="admin" and pwd=="admin":
            messagebox.showinfo("Admin logged in ","Welcome, Admin!")
            adminpage()
            
        else:
            messagebox.showinfo("Error","Invalid username or passord")    

    def loginpage():
               
        def uploadimage():
            def upload():
                info1=path_entry.get()
                img=Image.open(info1).resize((250,188))
                img=ImageTk.PhotoImage(img)
                l3=tk.Label(root2,image=img,bd=2,relief="groove")
                l3.grid(row=6,column=1)

            lbl=tk.Label(root2, text="Enter path to upload image",fg="brown")
            lbl.grid(row=3,column=1)
            path_entry=tk.Entry(root2,width=20)
            path_entry.grid(row=4,column=1)
            b1=tk.Button(root2,text="Upload",command=upload,bg="brown",fg="white")
            b1.grid(row=5,column=1)
        
        def viewprofile():
            def view():
                un=e1.get()
                if not re.match(r"^[A-za-z\s]+$",un):
                    messagebox.showinfo("Error","Please enter valid Username")
                    return
                if os.path.exists("C:/Users/BLAUPLUG/Documents/Python_programs/User Management System/userdb.csv"):
                    with open("C:/Users/BLAUPLUG/Documents/Python_programs/User Management System/userdb.csv", "r") as file:
                        reader = csv.reader(file)
                        for row in reader:
                            if un in row:
                                messagebox.showinfo("Book Details", f"Username: {row[0]}\nPassword: {row[1]}\nEmail: {row[2]}")
                                #clear_searchbox()
                                return
                            messagebox.showerror("Error", "User not found!")
                            #clear_searchbox()
                    

            l1=tk.Label(root2,text="Enter username",fg="Brown")
            l1.grid(row=3,column=0)
            e1=tk.Entry(root2)
            e1.grid(row=4,column=0)
            b1=tk.Button(root2,text="View profile",bg="brown",fg="white",command=view)
            b1.grid(row=5,column=1)
            
                    
        def updateprofile():
            def update():

                if selectedtaskindex==0:
                    l1=tk.Label(root,text="Enter old username and new username ",fg="Brown")
                    l1.grid(row=5,column=1)
                

                    e1=tk.Entry(root)
                    e1.pack()
                    e2=tk.Entry(root)
                    e2.pack()
                    
                    oldun=e1.get()
                    newun=e2.get()
                    if oldun=="" or newun=="":
                        messagebox.showinfo("Error","All fields are required")

                    if not re.match(r"^[A-za-z\s]+$",oldun):
                        messagebox.showinfo("Error","Please enter valid old username")
                        return
                    if not re.match(r"^[A-za-z\s]+$",newun):
                        messagebox.showinfo("Error","Please enter valid new username")
                        return
                    
                    df = pd.read_csv("C:/Users/BLAUPLUG/Documents/Python_programs/User Management System/userdb.csv") 
                    df['Username'] = df['Username'].replace({'oldun': 'newun'}) 
                    df.to_csv("C:/Users/BLAUPLUG/Documents/Python_programs/User Management System/userdb.csv", index=False) 
               
                    messagebox.showinfo("Success","Username updated succesfully")

                if selectedtaskindex==1:
                    l1=tk.Label(root,text="Enter old email and new email ",fg="Brown")
                    l1.pack()
                    e1=tk.Entry(root)
                    e1.pack()
                    e2=tk.Entry(root)
                    e2.pack()
                    
                    oldemail=e1.get()
                    newemail=e2.get()
                    if oldemail=="" or newemail=="":
                        messagebox.showinfo("Error","All fields are required")
                    
                    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

                    if not (re.fullmatch(regex, oldemail)):
                        messagebox.showinfo("Error","Please enter a valid old email id")
                    
                    if not (re.fullmatch(regex, newemail)):
                        messagebox.showinfo("Error","Please enter a valid new email id")

                    
                    df = pd.read_csv("C:/Users/BLAUPLUG/Documents/Python_programs/User Management System/userdb.csv") 
                    df['Username'] = df['Username'].replace({'oldun': 'newun'}) 
                    df.to_csv("C:/Users/BLAUPLUG/Documents/Python_programs/User Management System/userdb.csv", index=False) 
               
                    messagebox.showinfo("Success","Email updated succesfully")

    

            l4=tk.Label(root,text="What do you want to update?",fg="Brown")
            l4.pack()
            t1=tk.Listbox(root,height = 5, width = 10)
            t1.insert(tk.END,"Username\n")
            t1.insert(tk.END,"Email")
            t1.grid(row=3,column=1)
            selectedtaskindex=t1.curselection()
            b1=tk.Button(root,text="Update",bg="brown",fg="white",command=update)
            b1.grid(row=4,column=1)
           
        def managepwd():
            def changepwd():
                l2=tk.Label(root2,text="Enter new password")
                l2.grid(row=7,column=1)
                e2=tk.Entry(root2)
                e2.grid(row=8,column=1)
                em=e1.get()
                pwd=e2.get()
                bytes=pwd.encode('utf-8')
                salt=bcrypt.gensalt()
                hashedpwd = bcrypt.hashpw(bytes, salt) 
            
                query="Update User set Password="+hashedpwd+"where Email="+em
                con=pymysql.connect(host='localhost',user='root',password='ROOT123')
                cursor=con.cursor()
                try:
                    cursor.execute(query)
                    con.commit()
                    messagebox.showinfo("Success","Password changes successfully")
                except:
                    messagebox.showinfo("Error","Failed to change password")
            
            l1=tk.Label(root2,text="Enter email",fg="Brown")
            l1.grid(row=4,column=1)
            e1=tk.Entry(root)
            e1.grid(row=5,column=1)
            b1=tk.Button(root2,text="Change Password",fg="Brown",command=changepwd)
            b1.grid(row=6,column=1)
        
        def deleteacc():
            def delete():
                un=e1.get()
                query="delete * from User where Username="+un
                cursor.execute(query)
                con.commit()
                messagebox.showinfo("Success","Account deleted successfully")
                root2.destroy()
                login()
            answer=messagebox.showinfo("Sure?","Are you sure you want to delete your account?")
            if answer:
                l1=tk.Label(root2,text="Enter Username")
                l1.grid(row=3,column=1)
                e1=tk.Entry(root2)
                e1.grid(row=4,column=1)
                b1=tk.Button(root2,text="delete",bg="brown",fg="white",command=delete)
                b1.grid(row=4,column=1)
                

        def logout():
                answer=messagebox.askyesno("Sure?","Are you sure you want to logout?")
                if answer:
                    root2.destroy()
                    messagebox.showinfo("Success","User successfully logged out")
                    login()
                else:
                    loginpage()
        root2=tk.Tk()
        root2.geometry("600x600")
        root2.title("Login page")
        b1=tk.Button(root2,text="Upload image",command=uploadimage)
        b1.grid(row=2,column=0)
        b2=tk.Button(root2,text="View Profile",width=10,command=viewprofile,fg="white",bg="brown")
        b2.grid(row=2,column=1)
        b3=tk.Button(root2,text="Update Profile",width=10,command=updateprofile,fg="white",bg="brown")
        b3.grid(row=2,column=2)
        b4=tk.Button(root2, text="Delete account",width=10,command=deleteacc,fg="white",bg="brown")
        b4.grid(row=2,column=3)
        b5=tk.Button(root2,text="Manage password",width=10,command=managepwd,fg="white",bg="brown")
        b5.grid(row=2,column=4)
        b6=tk.Button(root2, text="Logout",width=10,command=logout)
        b6.grid(row=2,column=5)

        root2.mainloop()
    
    def userlogin():
        con=pymysql.connect(host='localhost',user='root',password='ROOT123')
        cursor=con.cursor()

        username=un_entry.get()
        pwd=pwd_entry.get()
        
        if username=="" or pwd=="":
            messagebox.showinfo("Insert status","All fields are required")
        
        else:
            cursor.execute('select %s from User') % username
            dbuser = cursor.fetchone()
            if dbuser == username:
                cursor.execute('select %s from User') % pwd
                dbpass = cursor.fetchone()

                userBytes = pwd.encode('utf-8') 
                salt = bcrypt.gensalt() 
                hash = bcrypt.hashpw(bytes, salt) 
                result = bcrypt.checkpw(userBytes, hash) 
                
                if dbpass == result:
                    messagebox.showinfo("User logged in",f"Welcome,{username}")
                    loginpage()
                else:
                    messagebox.showinfo("Error","Password is incorrect") 

            else:
                messagebox.showinfo("Error", "Username is incorrect.") 
        

    root=tk.Tk()
    root.title("Login page")
    root.geometry("400x400")
    root.configure(bg="orange")
    l1=tk.Label(root,text="Welcome to login page",fg="brown")
    l1.grid(row=0,column=1)
    un_lbl=tk.Label(root,text='Username',fg="brown")
    un_lbl.grid(row=1,column=0)
    un_entry=tk.Entry(root)
    un_entry.grid(row=1,column=1)

    pwd_lbl=tk.Label(root,text="Password",fg="brown")
    pwd_lbl.grid(row=2,column=0)
    pwd_entry=tk.Entry(root,show="*")
    pwd_entry.grid(row=2,column=1)
    
    b1=tk.Button(root,text="Admin login",command=adminlogin,fg="white",bg="brown")
    b1.grid(row=3,column=0)
    b2=tk.Button(root,text="User login",command=userlogin,fg="white",bg="brown")
    b2.grid(row=3,column=1)

    root.mainloop()