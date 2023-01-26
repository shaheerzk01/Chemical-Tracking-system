from tkinter import*
from PIL import Image, ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
from project import CMS
class LoginClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x400+220+130")
        self.root.title("Chemical Manufacturing System")
        self.root.config(bg="white")
        self.root.focus_force()
        self.var_username=StringVar()
        self.var_password=StringVar()
        Login_lbl=Label(self.root,text="LOGIN HERE",font=("goudy old style",30),bg="#184a45",fg="white",bd=5,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)
        
        lbl_username=Label(self.root,text="Username:",font=("goudy old style",20),bg="white").place(x=30,y=150)
        txt_name=Entry(self.root,textvariable=self.var_username,font=("goudy old style",18),bg="lightyellow").place(x=150,y=160,width=180)
        
        lbl_password=Label(self.root,text="Password:",font=("goudy old style",20),bg="white").place(x=40,y=200)
        txt_Password=Entry(self.root,textvariable=self.var_password,font=("goudy old style",18),bg="lightyellow").place(x=150,y=210,width=180)

        btn_login=Button(self.root,text="Login In",command=self.Login,font=("goudy old style",20,'bold'),bg="#184a45",fg='white',cursor='hand2').place(x=150,y=270)

    def Login(self):

        if  self.var_username.get()=='admin'and self.var_password.get()=='12345':
            self.new_win=Toplevel(self.root)
            self.new_obj=CMS(self.new_win)

        else:
            messagebox.showerror("Login",f'Enter Correct username or password ',parent=self.root)


        # except:
        #     messagebox.showerror("Login",f'Entry Correct username or password  ',parent=self.root)


        


if __name__=="__main__":         
    root=Tk() 
    obj=LoginClass(root)
    root.mainloop()