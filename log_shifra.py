import pyperclip as pc
import time

EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ qwertyuiopasdfghjklzxcvbnm ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ юбьтимсчяэждлорпавыфъхзщшгнекуцй 1234567890 !"№;%:?*()_+-=@#$^&~` ABCDEFGHIJKLMNOPQRSTUVWXYZ qwertyuiopasdfghjklzxcvbnm ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ юбьтимсчяэждлорпавыфъхзщшгнекуцй 1234567890 !"№;%:?*()_+-=@#$^&~` '
itog = ''
  
def slidercommand(value, shag2):
  global a  
  a = value
  a = int(a)
  print(a)  
  shag2.configure(text=a)

def destroy_timer(text):
  text.configure(text=" ")

def cod(user_text, text, app):
  global itog
  UT = user_text.get()
  for i in UT:
    mesto = EU.find(i)
    new_mesto = mesto + a
    if i in EU:
      itog += EU[new_mesto]
  pc.copy(itog)
  text.configure(text="Cкопировано!")
  itog = " "
  app.after(3000, destroy_timer, text)

def dek(user_text, text, app):
  global itog
  UT = user_text.get()
  for i in UT:
    mesto = EU.find(i)
    new_mesto = mesto - a
    if i in EU:
      itog += EU[new_mesto]
  pc.copy(itog) 
  text.configure(text="Cкопировано!")
  itog = " "
  app.after(3000, destroy_timer, text)

n = 1
def settheme(app, frame_1, frame_2, frame_3, menu_frame, close_menu, theme_button, menu_button, dark_menu, image_menu, image_close_menu, theme_1, theme_2):
    global n
    if n == 1:
        app.configure(fg_color='white')
        frame_1.configure(fg_color='#A9A9A9')
        frame_2.configure(fg_color='#A9A9A9')
        frame_3.configure(fg_color='#A9A9A9')
        menu_frame.configure(fg_color='white')
        theme_button.configure(image=theme_1)
        menu_button.configure(fg_color='white', hover_color='white', image=dark_menu)
        n = 0
    elif n == 0:
        app.configure(fg_color='#232323')
        frame_1.configure(fg_color='#2a2a2a')
        frame_2.configure(fg_color='#2a2a2a')
        frame_3.configure(fg_color='#2a2a2a')
        menu_frame.configure(fg_color='#232323')
        theme_button.configure(image=theme_2)
        menu_button.configure(fg_color='#232323', hover_color='#232323', image=image_menu)
        n = 1
