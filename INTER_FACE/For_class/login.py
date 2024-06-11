from tkinter import *
from tkinter import messagebox
import pickle
import tkinter.ttk as ttk
from PIL import ImageTk, Image

#Проверка заполнения формы
def save_data():
    if email_enter.get() == '':
        # ff = Label(root, text='enter email!!!', bg='#1C222B', fg='red', font=('Courier', 10)).place(x=198, y=148)
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

#2 окно
#Функция подсвета кнопок
def loginn():
    def changeOnHoverk(button, colorOnHover, colorOnLeave):
        button.bind("<Enter>", func=lambda e: button.config(
            background=colorOnHover))

        # background color on leving widget
        button.bind("<Leave>", func=lambda e: button.config(
            background=colorOnLeave))


    # root.withdraw() #ЗАкрывает главное окно при открытие дочернего
    login = Toplevel()
    login.protocol('WM_DELETE_WINDOW', lambda: root.destroy())
    stylee = ttk.Style(login)
    login['bg'] = '#1C222B'
    login.title('Login')
    login.wm_attributes('-alpha', 0.91)  # Прозрачность окна
    login.geometry('600x400')
    login.resizable(width=False, height=False)

    # img1 = Image.open('лапки.png')
    # res_img1 = img1.resize((100, 100))
    # imgg1 = ImageTk.PhotoImage(res_img1)
    # lab1 = Label(image=imgg1)
    # lab1.image = imgg1
    # lab1.config(bg='#1C222B')
    # lab1.place(x=202, y=200)
    # frame_1 = Frame(login, bg='#1C222B')
    # frame_1.place(relwidth=1, relheight=1)

    #проверка после регистр
    def log_pass():
        if login_enter.get() == '':
            messagebox.showerror(':/', 'You forget to enter email')
        elif enter_password.get() == '':
            messagebox.showerror('-_-','You forget to enter password')
        else:
            file_save = open('file_login.txt', 'rb')
            a = pickle.load(file_save)
            file_save.close()
            if login_enter.get() in a:
                if enter_password.get() == a[login_enter.get()]:
                    messagebox.showinfo('Welcome!', 'Our app is not finished. Come back later:)')
                else:
                    messagebox.showerror('Error', 'Incorrect email or password')
            else:
                messagebox.showerror('Error', 'Incorrect email')

    login_head = Label(login, text='Ok! Now you need to login', bg='#1C222B', fg='#F967BC',  font=('Courier', 27))
    login_head.pack(pady=15)
    login_email = Label(login, text='Enter email', bg='#1C222B', fg='#EBC2FF', font=('Courier', 15))
    login_email.pack(pady=10)
    login_enter = Entry(login, bg='#333D4D',fg='#EBC2FF')
    login_enter.pack(pady=5)
    login_password = Label(login, text='Enter password',  bg='#1C222B', fg='#EBC2FF', font=('Courier', 15))
    login_password.pack(pady=10)
    enter_password = Entry(login, show='✖️', bg='#333D4D',fg='#EBC2FF')
    enter_password.pack(pady=5)
    button_login = Button(login, text='Login now!', bg='#1C222B', fg='#F967BC', font=('Courier', 12), command=log_pass)
    button_login.pack(pady=25)
    changeOnHoverk(button_login, "#FE95D2", "#1C222B")

def on_closing():
    if messagebox.askokcancel('Exiting the app', 'Do you want to exiting the app?'):
        root.destroy()

def showpassword():
    if password_enter['show'] == '✖️':
        password_enter['show'] = ''
    else:
        password_enter['show'] = '✖️'

#ИЗМЕНЕНИЕ ЦЫЕТА ПРИ НАВЕДЕНИИ
def changeOnHover(button, colorOnHover, colorOnLeave):
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))
    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))

root = Tk()
style = ttk.Style(root)
root.protocol('WM_DELETE_WINDOW', on_closing)
root['bg'] = '#1C222B'
root.title('Registration')
root.wm_attributes('-alpha', 0.91)#Прозрачность окна
root.geometry('500x550')
root.resizable(width=False, height=False)

canvas = Canvas(root, height=500, width=500)
canvas.pack()

frame = Frame(root, bg='#1C222B')#Создание фрейма, чтобы было удоблее распологать объекты
frame.place(relwidth=1, relheight=1)

#ФОТО
img = Image.open('catik.png')
res_img = img.resize((100,100))
imgg = ImageTk.PhotoImage(res_img)
lab = Label(image=imgg)
lab.image = imgg
lab.config(bg='#1C222B')
lab.place(x=202,y=447)

#создание поля регистрации
title = Label(frame, text='Registration', bg='#1C222B', fg='#F967BC', font=('Courier', 30))
title.pack(pady=20)
name = Label(frame, text='Enter username', bg='#1C222B', fg='#EBC2FF', font=('Courier',15))
name.pack()
name_enter = Entry(frame, bg='#333D4D',fg='#EBC2FF')
name_enter.pack(padx=20, pady=10)
email = Label(frame, text='Enter email', bg='#1C222B', fg='#EBC2FF', font=('Courier',15))
email.pack(pady=15)
email_enter = Entry(frame, bg='#333D4D',fg='#EBC2FF')
email_enter.pack()
password = Label(frame, text='Enter password', bg='#1C222B', fg='#EBC2FF', font=('Courier',15))
password.pack(pady=15)
password_enter = Entry(frame, show='✖️', bg='#333D4D',fg='#EBC2FF')
password_enter.pack()
com_password = Label(frame, text='Repeat password', bg='#1C222B', fg='#EBC2FF', font=('Courier',15))
com_password.pack(pady=15)
com_password_enter = Entry(frame, show='✖️', bg='#333D4D',fg='#EBC2FF')
com_password_enter.pack(pady=1)
sh_pass = Button(frame, text='👁', bg='#1C222B', fg='#F967BC', font=('Courier', 10), command=showpassword).place(x=325, y=285)
button = Button(frame, text='Registration right now!', bg='#1C222B', fg='#F967BC', font=('Courier', 12), command=save_data)
button.pack(pady=25)

changeOnHover(button, "#FE95D2", "#1C222B")

root.mainloop()

