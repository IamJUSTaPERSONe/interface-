
from tkinter import *
from tkinter import messagebox
import sqlite3

db = sqlite3.connect('database.db')
cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users(
    login TEXT,
    password TEXT
)''')
db.commit()


def registration():
    def loginn():
        rootik.destroy()

    def reg_save1():
        info = cursor.execute('SELECT * FROM users WHERE login=? AND password=?', (email_e.get(), password_e.get()))
        db.commit()
        if info.fetchone() is None:
            cursor.execute(f"INSERT INTO users (login, password) VALUES (?, ?)", (email_e.get(), password_e.get()))
            db.commit()
            print('vi zaregestrirovan')
        else:
            print('uze est takaya zapis')
            for i in cursor.execute("SELECT * FROM users"):
                print(i)

    def reg_save():
        if email_e.get() == '':
            messagebox.showerror('', 'enter email')
        elif password_e.get() == '':
            messagebox.showerror('', 'enter password')
        elif com_password_e.get() == '':
            messagebox.showerror('', 'enter password')
        else:
            reg_save1()
    rootik = Tk()
    rootik.title('Registraton')
    rootik['bg'] = 'black'
    rootik.geometry('300x400')
    rootik.resizable(width=False, height=False)

    canvas = Canvas(rootik, height=300, width=200)
    canvas.pack()
    frame = Frame(rootik, bg='black')
    frame.place(relwidth=1, relheight=1)

    title = Label(frame, text='Registration', bg='black', fg='blue').pack()
    email = Label(frame, text='Enter email', bg='black', fg='white').pack()
    email_e = Entry(frame)
    email_e.pack()
    password = Label(frame, text='Enter password', bg='black', fg='white').pack()
    password_e = Entry(frame)
    password_e.pack()
    com_password = Label(frame, text='Repeat password', bg='black', fg='white').pack()
    com_password_e = Entry(frame)
    com_password_e.pack()
    button = Button(frame, text='Registration', command=reg_save).pack(pady=20)
    button1 = Button(frame, text='or Login', command=loginn).pack()


def login():
    if email_e.get() == '':
        messagebox.showerror('error','enter password or email')
    else:
        info = cursor.execute('SELECT * FROM users WHERE login=? AND password=?',(email_e.get(), password_e.get() ))
        db.commit()
        if info.fetchone() is None:
            messagebox.showerror('','please go reg')
        else:
            messagebox.showinfo('', 'you sucsessful reg')



root = Tk()
root.title('Login')
root['bg']='black'
root.geometry('300x200')
root.resizable(width=False, height=False)

canvas = Canvas(root, height=300, width=200)
canvas.pack()
frame = Frame(root, bg='black')
frame.place(relwidth=1, relheight=1)

title = Label(frame, text='Login', bg='black', fg='blue').pack()
email = Label(frame, text='Enter email', bg='black', fg='white').pack()
email_e = Entry(frame)
email_e.pack()
password = Label(frame, text='Enter password', bg='black', fg='white').pack()
password_e = Entry(frame)
password_e.pack()
button = Button(frame, text='Login', command=login).pack(pady=20)
button2 = Button(frame, text='Registration', command=registration).pack()

# db.commit()
# db.close()
root.mainloop()
