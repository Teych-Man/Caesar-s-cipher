import customtkinter
import tkinter 
from PIL import Image
import log_shifra

menu_opened = False
image_menu = customtkinter.CTkImage(light_image=Image.open('menu.png'), dark_image=Image.open('menu.png'), size=(20, 20))
dark_menu = customtkinter.CTkImage(light_image=Image.open('dark_menu.png'), dark_image=Image.open('dark_menu.png'), size=(20, 20))
image_close_menu = customtkinter.CTkImage(light_image=Image.open('close_menu.png'), dark_image=Image.open('close_menu.png'), size=(20, 20))
theme_1 = customtkinter.CTkImage(light_image=Image.open('light.png'), dark_image=Image.open('light.png'), size=(40, 40))
theme_2 = customtkinter.CTkImage(light_image=Image.open('night.png'), dark_image=Image.open('night.png'), size=(40, 40))

def toggle_menu():
    global menu_opened
    if menu_opened:
        # Закрываем меню плавно
        menu_frame.pack_forget()
        menu_opened = False
    else:
        # Открываем меню плавно
        menu_frame.pack(side='left', fill='y')
        menu_opened = True

def closed_menu():
    global menu_opened
    if menu_opened:
        toggle_menu()
        menu_opened = False

def onesettheme():
    log_shifra.settheme(app, frame_1, frame_2, frame_3, menu_frame, close_menu, theme_button, menu_button, dark_menu, image_menu, image_close_menu, theme_1, theme_2)

def onecod():
  log_shifra.cod(user_text, text, app)

def onedek():
  log_shifra.dek(user_text, text, app)

def oneslidercommand(value):  
	log_shifra.slidercommand(value, shag2)

def start():
  global frame_1, support_button, about_button, settings_button, frame_2, frame_3, menu_frame, close_menu, theme_button, menu_button, shag2, user_text, text, app, menu_frame2

  customtkinter.set_appearance_mode("dark") 
  app = customtkinter.CTk()
  app.geometry("800x350+250+150")
  app.resizable( False, False )
  app.title("Caesar's cipher")
  app.iconbitmap('icon.ico')

  menu_button = customtkinter.CTkButton(master=app, image=image_menu, command=toggle_menu, text='', width=30, height=30, fg_color='#232323', hover_color='#232323')
  menu_button.place(x=0, y=0)
    #ЗАДНИЕ ФОНЫ ------------------------------------------------------------
  frame_1 = customtkinter.CTkFrame(master=app, width=490, height=142)
  frame_1.place(x = 25, y = 25)

  frame_2 = customtkinter.CTkFrame(master=app, width=250, height=300)
  frame_2.place(x = 530, y = 25)

  frame_3 = customtkinter.CTkFrame(master=app, width=490, height=126)
  frame_3.place(x = 25, y = 200)

  menu_frame = customtkinter.CTkFrame(master=app, width=200, fg_color='#232323')
  menu_frame.place_forget()

  menu_frame2 = customtkinter.CTkFrame(master=menu_frame, width=50, height=360)
  menu_frame2.place(x = 0, y = -5)

  settings_button = customtkinter.CTkButton(master=menu_frame, text="Настройки", text_color="#eeeeee", fg_color="#5b5b5b", hover_color="#888888")
  settings_button.place(x=10, y=10)

  about_button = customtkinter.CTkButton(master=menu_frame, text="О приложении", text_color="#eeeeee", fg_color="#5b5b5b", hover_color="#888888")
  about_button.place(x=10, y=50)

  support_button = customtkinter.CTkButton(master=menu_frame, text="Тех. поддержка", text_color="#eeeeee", fg_color="#5b5b5b", hover_color="#888888")
  support_button.place(x=10, y=90) 

  close_menu = customtkinter.CTkLabel(master = menu_frame, image=image_close_menu, text = '', width=30, height=30, fg_color='transparent')
  close_menu.bind("<Button-1>", lambda event: closed_menu())
  close_menu.bind("<Enter>", lambda event: app.config(cursor='hand2'))
  close_menu.bind("<Leave>", lambda event: app.config(cursor='arrow'))
  close_menu.place(x = 170, y = 0)

  theme_button = customtkinter.CTkLabel(master = menu_frame2, text = '', image=theme_2, width=30, height=30, fg_color='transparent')
  theme_button.bind("<Button-1>", lambda event: onesettheme())
  theme_button.bind("<Enter>", lambda event: app.config(cursor='hand2'))
  theme_button.bind("<Leave>", lambda event: app.config(cursor='arrow'))
  theme_button.place(x = 6, y = 310)

  #ПОЛЕ ВВОДА ------------------------------------------------------------
  user_text = customtkinter.CTkEntry( master=frame_1, width = 450, height = 100 )
  user_text.place( x = 20, y = 20 )

  #КНОПКА КОДИРОВАТЬ ------------------------------------------------------------
  koder = customtkinter.CTkButton( master=frame_3,  text="Кодировать", command = onecod, 
                                  text_color = "#eeeeee", fg_color = "#5b5b5b", hover_color = "#444444")
  koder.place( x = 200, y = 25 )

  #КНОПКА ДЕКОДИРОВАТЬ ------------------------------------------------------------
  dekoder = customtkinter.CTkButton( master=frame_3, text="Декодировать", command = onedek, 
                                    text_color = "#eeeeee", fg_color = "#5b5b5b", hover_color = "#444444")
  dekoder.place( x = 200, y = 75 )

  #ТЕКСТ "Скопированно" ------------------------------------------------------------
  text = customtkinter.CTkLabel( master=frame_1, text=" ", text_color = "green", fg_color='transparent', bg_color = 'transparent')
  text.place( x = 270, y = 134, anchor=tkinter.CENTER )

  #НАСТРОЙКА ШАГА ШИФРОВКИ ------------------------------------------------------------
  shag = customtkinter.CTkLabel(master=frame_2, text="Шаг Шифровки/Дешифровки", text_color = 'white')
  shag.place(x=130, y=30, anchor=tkinter.CENTER)
  #ПОКАЗАТЕЛЬ ШАГА ШИФРОВКИ ------------------------------------------------------------
  shag2 = customtkinter.CTkLabel(master=frame_2, text="1")
  shag2.place( x = 215, y = 75, anchor=tkinter.CENTER )

  slider_1 = customtkinter.CTkSlider(master=frame_2, command = oneslidercommand, from_=1, to=100, number_of_steps = 99)
  slider_1.place(x = 30, y = 50)
  slider_1.set(1)

  app.mainloop()

if __name__ == "__main__":
  start()