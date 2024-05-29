from tkinter import *
from tkinter import messagebox
import pickle
import tkinter.ttk as ttk

def save_data():
    if email_enter.get() == '':
        messagebox.showerror(':/', 'You forget to enter email')
    elif password_enter.get() == '' or com_password_enter.get() == '':
        messagebox.showerror(':0', 'You forget to enter password')
    elif password_enter.get() != com_password_enter.get():
        messagebox.showerror('-_-', 'Your passwords do not match')
    else:
        login_pass_save = {}
        login_pass_save[email_enter.get()] = password_enter.get()
        file_save = open('file_login.txt', 'wb')
        pickle.dump(login_pass_save, file_save)
        file_save.close()
        loginn()

def loginn():
    login = Toplevel()
    stylee = ttk.Style(login)
    login['bg'] = '#6BBFFF'
    login.title('Login')
    login.wm_attributes('-alpha', 0.9)  # Прозрачность окна
    login.geometry('600x400')
    login.resizable(width=False, height=False)

    frame_1 = Frame(login, bg='#6BBFFF')
    frame_1.place(relwidth=1, relheight=1)

    login_head = Label(login, text='Ok! Now you need to login', bg='#6BBFFF', font=('Courier', 27))
    login_head.pack(pady=15)
    login_email = Label(login, text='Enter email', bg='#6BBFFF', font=('Courier', 15))
    login_email.pack(pady=10)
    login_enter = Entry(login)
    login_enter.pack(pady=5)
    login_password = Label(login, text='Enter password', bg='#6BBFFF', font=('Courier', 15))
    login_password.pack(pady=10)
    enter_password = Entry(login, show='✖️')
    enter_password.pack(pady=5)
    button_login = Button(login, text='Login now!',bg='#29A9FF', font=('Courier', 12), command=lambda:log_pass)
    button_login.pack(pady=25)

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

root = Tk()
style = ttk.Style(root)
root['bg'] = '#6BBFFF'
root.title('Registration')
root.wm_attributes('-alpha', 0.9)#Прозрачность окна
root.geometry('500x500')
root.resizable(width=False, height=False)

canvas = Canvas(root, height=500, width=500)
canvas.pack()

frame = Frame(root, bg='#6BBFFF')#Создание фрейма, чтобы было удоблее распологать объекты
frame.place(relwidth=1, relheight=1)

#создание поля регистрации
title = Label(frame, text='Registration', bg='#6BBFFF', font=('Courier', 30))
title.pack(pady=20)
name = Label(frame, text='Enter username', bg='#6BBFFF',font=('Courier',15))
name.pack()
name_enter = Entry(frame)
name_enter.pack(pady=10)
email = Label(frame, text='Enter email', bg='#6BBFFF',font=('Courier',15))
email.pack(pady=5)
email_enter = Entry(frame)
email_enter.pack()
password = Label(frame, text='Enter password', bg='#6BBFFF',font=('Courier',15))
password.pack(pady=10)
password_enter = Entry(frame, show='✖️')
password_enter.pack()
com_password = Label(frame, text='Repeat password', bg='#6BBFFF',font=('Courier',15))
com_password.pack(pady=10)
com_password_enter = Entry(frame, show='✖️')
com_password_enter.pack()
button = Button(frame, text='Registration right now!', bg='#29A9FF', font=('Courier', 12), command=save_data)
button.pack(pady=25)

root.mainloop()

