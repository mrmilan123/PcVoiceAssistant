import tkinter as tk
import pyrebase
from tkinter import Button, Entry, Label, StringVar
from tkinter import messagebox

#---------------------------------------------------------------------------------------------------------------------------------
# connecting Firebase

config = {

  "apiKey": "AIzaSyB7kvhCIpdmpylLIiSicyKIUOtTsAWouMM",
  "authDomain": "ai-voice-assistant-36388.firebaseapp.com",
  "projectId": "ai-voice-assistant-36388",
  "storageBucket": "ai-voice-assistant-36388.appspot.com",
  "messagingSenderId": "6158845205",
  "appId": "1:6158845205:web:59ad37b69165073b96151c",
  "measurementId": "G-W739M3PH4K",
  # Database Url
  "databaseURL": "https://ai-voice-assistant-36388-default-rtdb.firebaseio.com/"
}

# connecting app
firebase = pyrebase.initialize_app(config)

# connecting realtime database
database = firebase.database()

# connecting Authenticataion
auth = firebase.auth()


#---------------------------------------------------------------------------------------------------------------------------------
# functions

def signup(email,password):

    data = {"query":"null", "password":"unlock pc"}
   
    try:
        auth.create_user_with_email_and_password(email,password)
        
    except:
        messagebox.showerror("error","error occured")
    else:
        print('Login sucessfull')

        email = email.split("@")
        user = email[0]
        
        database.child("users").child(user).set(data)
        messagebox.showinfo("sucessfull","Account created sucessfully")
        root.destroy()


def create_account():
    email = str()
    crPass = str()
    coPass = str()

    email = emailEt.get()
    crPass = crPassEt.get()
    coPass = conPassEt.get()
    screenlock = setLockEt.get()

    email = str(email)
    crPass = str(crPass)
    coPass = str(coPass)
    screenlock = str(screenlock)

    if (email=="" or crPass=="" or coPass=="" or screenlock==""):
        messagebox.showinfo("Error","No entry should be left empty")
    elif (crPass != coPass):
        messagebox.showinfo("Error","Passwords don't match")
    else:
        signup(email,coPass)




#---------------------------------------------------------------------------------------------------------------------------------
# GUI

root = tk.Tk()
root.geometry('500x500')
root.title("Get Started")
root.resizable(False,False)


label_0 = Label(root, text="Voice Assistant",width=20,font=("bold", 20))                   # title
label_0.place(x=90,y=53)

label_1 = Label(root, text="Email:",width=20,font=("bold", 10))                            # email
label_1.place(x=80,y=130)
emailEt = Entry(root)
emailEt.place(x=240,y=130)

label_2 = Label(root, text="Create password:",width=20,font=("bold", 10))                 # Create Pass
label_2.place(x=68,y=180)
crPassEt = Entry(root, show="*")
crPassEt.place(x=240,y=180)

label_3 = Label(root, text="Confirm Password:",width=20,font=("bold", 10))                # confirm Pass
label_3.place(x=70,y=230)
conPassEt = Entry(root)
conPassEt.place(x=240,y=230)

label_4 = Label(root, text="Set ScreenPass:",width=20,font=("bold", 10))                   # set Lock
label_4.place(x=70,y=280)
setLockEt = Entry(root)
setLockEt.place(x=240,y=280)


button = Button(root, text='Create Account',width=20,bg='brown',fg='white',command=create_account)
button.place(x=180,y=380)


root.mainloop()