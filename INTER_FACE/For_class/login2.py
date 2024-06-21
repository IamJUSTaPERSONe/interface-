#interface with db
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import sqlite3

db = sqlite3.connect('databaseusers.db') #Без нижнего подчеркивания 
cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    login TEXT, 
    password TEXT
)''')
db.commit()

#Проверка поле регистрации и созранение в бд
def Win_reg():
    def save_data():
        if email_enter.get() == '':
            messagebox.showerror(':/', 'You forget to enter email')
        elif password_enter.get() == '' or com_password_enter.get() == '':
            messagebox.showerror(':0', 'You forget to enter password')
        elif password_enter.get() != com_password_enter.get():
            messagebox.showerror('-_-', 'Your passwords do not match')
        else:
            info = cursor.execute('SELECT * FROM users WHERE login=? AND password=?', (email_enter.get(),password_enter.get()))
            db.commit()
            if info.fetchone() is None:
                cursor.execute(f'INSERT INTO users (login,password) VALUES (?,?)', (email_enter.get(),password_enter.get()))
                db.commit()
                print('vi zaregestrirovan')
                for i in cursor.execute('SELECT * FROM users'):
                    print(i)
            else:
                print('uze est takaya zapis')
                for i in cursor.execute("SELECT * FROM users"):
                    print(i)
    # def login():
    #     root.withdraw()
    #     login.deiconify()

    def showpassword():
        if password_enter['show'] == '✖️':
            password_enter['show'] = ''
        else:
            password_enter['show'] = '✖️'
    login.withdraw()
    root = Tk()
    style = ttk.Style(root)
    root['bg'] = '#1C222B'
    root.title('Registration')
    root.wm_attributes('-alpha', 0.91)  # Прозрачность окна
    root.geometry('500x550')
    root.resizable(width=False, height=False)

    canvas = Canvas(root, height=500, width=500)
    canvas.pack()

    frame = Frame(root, bg='#1C222B')  # Создание фрейма, чтобы было удоблее распологать объекты
    frame.place(relwidth=1, relheight=1)


    def changeOnHover(button, colorOnHover, colorOnLeave):
        button.bind("<Enter>", func=lambda e: button.config(
            background=colorOnHover))
        # background color on leving widget
        button.bind("<Leave>", func=lambda e: button.config(
            background=colorOnLeave))
        button1.bind("<Enter>", func=lambda e: button.config(
            background=colorOnHover))
        # background color on leving widget
        button1.bind("<Leave>", func=lambda e: button.config(
            background=colorOnLeave))

    # ФОТО
    # img = Image.open('catik.png')
    # res_img = img.resize((100, 100))
    # imgg = ImageTk.PhotoImage(res_img)
    # lab = Label(image=imgg)
    # lab.image = imgg
    # lab.config(bg='#1C222B')
    # lab.place(x=202, y=447)

    # создание поля регистрации
    title = Label(frame, text='Registration', bg='#1C222B', fg='#F967BC', font=('Courier', 30))
    title.pack(pady=20)
    name = Label(frame, text='Enter username', bg='#1C222B', fg='#EBC2FF', font=('Courier', 15))
    name.pack()
    name_enter = Entry(frame, bg='#333D4D', fg='#EBC2FF')
    name_enter.pack(padx=20, pady=10)
    email = Label(frame, text='Enter email', bg='#1C222B', fg='#EBC2FF', font=('Courier', 15))
    email.pack(pady=15)
    email_enter = Entry(frame, bg='#333D4D', fg='#EBC2FF')
    email_enter.pack()
    password = Label(frame, text='Enter password', bg='#1C222B', fg='#EBC2FF', font=('Courier', 15))
    password.pack(pady=15)
    password_enter = Entry(frame, show='✖️', bg='#333D4D', fg='#EBC2FF')
    password_enter.pack()
    com_password = Label(frame, text='Repeat password', bg='#1C222B', fg='#EBC2FF', font=('Courier', 15))
    com_password.pack(pady=15)
    com_password_enter = Entry(frame, show='✖️', bg='#333D4D', fg='#EBC2FF')
    com_password_enter.pack(pady=1)
    sh_pass = Button(frame, text='👁', bg='#1C222B', fg='#F967BC', font=('Courier', 10), command=showpassword).place(x=325, y=285)
    button = Button(frame, text='Registration right now!', bg='#1C222B', fg='#F967BC', font=('Courier', 12),command=save_data)
    button.pack(pady=25)
    button1 = Button(frame, text='or login', bg='#1C222B', fg='white', font=('Courier', 8), command=login)
    button1.place(x=310, y=450)
    changeOnHover(button, "#FE95D2", "#1C222B")
    changeOnHover(button1, "#FE95D2", "#1C222B")
    
#окно После логина
def page():
    rootik = Toplevel()
    rootik['bg']='black'
    rootik.title('Wk')
    
 #ПРоверка после логина
def Win_new_page():
    if login_enter.get() == '':
        messagebox.showerror(':/', 'You forget to enter email')
    elif enter_password.get() == '':
        messagebox.showerror('-_-', 'You forget to enter password')
    else:
        info = cursor.execute('SELECT * FROM users WHERE login=? AND password=?', (login_enter.get(), enter_password.get()))
        db.commit()
        if info.fetchone() is None:
            for i in cursor.execute("SELECT * FROM users"):
                print(i)
            messagebox.showerror('', 'please go reg')
        else:
            messagebox.showinfo('', 'you sucsessful reg')
            page()

#Функция подсвета кнопок
def changeOnHoverk(button, colorOnHover, colorOnLeave):
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))

    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))

login = Tk()
stylee = ttk.Style(login)
login['bg'] = '#1C222B'
login.title('Login')
login.wm_attributes('-alpha', 0.91)  # Прозрачность окна
login.geometry('500x350')
login.resizable(width=False, height=False)
login_head = Label(login, text='Login', bg='#1C222B', fg='#F967BC',  font=('Courier', 27))
login_head.pack(pady=15)
login_email = Label(login, text='Enter email', bg='#1C222B', fg='#EBC2FF', font=('Courier', 15))
login_email.pack(pady=10)
login_enter = Entry(login, bg='#333D4D',fg='#EBC2FF')
login_enter.pack(pady=5)
login_password = Label(login, text='Enter password',  bg='#1C222B', fg='#EBC2FF', font=('Courier', 15))
login_password.pack(pady=10)
enter_password = Entry(login, show='✖️', bg='#333D4D',fg='#EBC2FF')
enter_password.pack(pady=5)

button_login = Button(login, text='Login now!', bg='#1C222B', fg='#F967BC', font=('Courier', 12), command=Win_new_page)
button_login.pack(pady=25)
button_reg = Button(login, text='or registration', bg='#1C222B', fg='white', font=('Courier', 9), command=Win_reg)
button_reg.place(x=190, y=300)
changeOnHoverk(button_login, "#FE95D2", "#1C222B")
changeOnHoverk(button_reg, "#FE95D2", "#1C222B")

login.mainloop()
db.close()
