from tkinter import *
from tkinter import messagebox
import pickle

root = Tk()
root.geometry('500x500')
root.title('Registration')
def registration():
    head_label = Label(text='Registration', font=40, height=5)
    name = Label(text='Enter user name', font=16)
    name_enter = Entry()
    email = Label(text='Enter email', font=8)
    email_enter = Entry()
    password = Label(text='Enter password', font=1)
    password_enter = Entry(show='*')
    com_password = Label(text='Repeat password', font=1)
    com_password_enter = Entry(show='*')
    button = Button(text='Registration right now!', command = lambda: save_data())

    head_label.pack()
    name.pack()
    name_enter.pack()
    email.pack()
    email_enter.pack()
    password.pack()
    password_enter.pack()
    com_password.pack()
    com_password_enter.pack()
    button.pack()

    def save_data():
        if email_enter.get() == '':
            messagebox.showerror(':/', 'You forget to enter email')
        elif password_enter.get() == '' or com_password_enter.get() == '':
            messagebox.showerror(':0', 'You forget to enter password')
        else:
            login_pass_save = {}
            login_pass_save[email_enter.get()] = password_enter.get()
            file_save = open('file_login.txt', 'wb')
            pickle.dump(login_pass_save, file_save)
            file_save.close()
            login()

def login():
    text_label_login = Label(text='Ok! Now you need to login', font=1)
    login_email = Label(text='Enter email', font=1)
    login_enter = Entry()
    login_password = Label(text='Enter password', font=1)
    enter_password = Entry(show='*')
    button_login = Button(text='Login now!', command=lambda: log_pass())
    text_label_login.pack()
    login_email.pack()
    login_enter.pack()
    login_password.pack()
    enter_password.pack()
    button_login.pack()

    def log_pass():
        file_save = open('file_login.txt', 'rb')
        a = pickle.load(file_save)
        file_save.close()
        if login_enter.get() in a:
            if enter_password.get() == a[login_enter.get()]:
                messagebox.showinfo('Welcome!', 'Our app is not finished. Come back later:)')
            else:
                messagebox.showerror('Error', 'Incorrect login or password')
        else:
            messagebox.showerror('Error', 'Incorrect login')

registration()

root.mainloop()

