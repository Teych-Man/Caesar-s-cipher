import customtkinter
import pyperclip as pc
from PIL import Image
import log_auth
  
app = customtkinter.CTk()
app.geometry("350x500")
app.resizable(False,False)
app.title("Авторизация")
customtkinter.set_appearance_mode("dark")
app.iconbitmap('icon.ico')


my_image  = customtkinter.CTkImage(light_image = Image.open(r"show.png"),
                                  dark_image= Image.open(r"show.png"), size=(30, 30))

def onelog_in():
  log_auth.log_in(nick, password, code, no_nick, no_pass, no_code, hide_nick, hide_pass, hide_code, app)

def hide_nick():
  no_nick.configure(text_color='#2b2b2b')
def hide_pass():
  no_pass.configure(text_color='#2b2b2b')
def hide_code():
  no_code.configure(text_color='#2b2b2b')       

def show():
  if code.cget('show') == '*':
    code.configure(show='')
  else:
    code.configure(show='*')
def show_pass():
  if password.cget('show') == '*':
    password.configure(show='')
  else:
    password.configure(show='*')

frame = customtkinter.CTkFrame(master=app, width = 300, height = 450)
frame.place(x = 25, y = 22)

Button_settings = customtkinter.CTkButton( master = frame,  image=my_image, text= " ", command = show, 
                                          width=2, height=2, fg_color = "#2b2b2b", hover_color = "#2b2b2b")
Button_settings.place( x = 240, y = 150)

show_pass = customtkinter.CTkButton( master = frame,  image=my_image, text= " ", command = show_pass, 
                                    width=2, height=2, fg_color = "#2b2b2b", hover_color = "#2b2b2b")
show_pass.place( x = 240, y = 100)

nick = customtkinter.CTkEntry(master=app, placeholder_text="Ник", width=150, height=35)
nick.place(x = 115, y = 75)

password = customtkinter.CTkEntry(master=app, placeholder_text='Пароль', width=150, height=35,  show = '*')
password.place(x = 115, y = 125)

code = customtkinter.CTkEntry(master=app, placeholder_text='Код', width=150, height=35, show = '*')
code.place(x = 115, y = 175)

button = customtkinter.CTkButton(master	= app, text="Авторизоваться", command=onelog_in)
button.place(x = 120, y = 250)

no_nick = customtkinter.CTkLabel(master = app, text = 'Не верный ник', text_color='#2b2b2b', fg_color='#2b2b2b', width = 20, height = 5, font=('Arial', 11, 'normal'))
no_nick.place(x = 150, y = 110)

no_pass = customtkinter.CTkLabel(master = app, text = 'Не верный пароль', text_color='#2b2b2b', fg_color='#2b2b2b', width = 20, height = 5, font=('Arial', 11, 'normal'))
no_pass.place(x = 143, y = 160)

no_code = customtkinter.CTkLabel(master = app, text = 'Не верный код', text_color='#2b2b2b', fg_color='#2b2b2b', width = 20, height = 5, font=('Arial', 11, 'normal'))
no_code.place(x = 150, y = 210)

app.mainloop()