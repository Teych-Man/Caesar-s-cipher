import pyperclip as pc
import subprocess
import interf_shifra

def log_in(nick, password, code, no_nick, no_pass, no_code, hide_nick, hide_pass, hide_code, app):
  no_nic = 0
  no_pas = 0
  no_cod = 0
  nick_get = nick.get()
  password_get = password.get()
  code_get = code.get()

  if nick_get == '1':
    no_nic = 1
  else:
    no_nick.configure(text_color='red')
    no_nick.after(3000, hide_nick)

  if password_get == '1':
    no_pas = 1
  else:
    no_pass.configure(text_color='red')
    no_pass.after(3000, hide_pass)

  if code_get == '1':
    no_cod = 1
  else:
    no_code.configure(text_color='red') 
    no_code.after(3000, hide_code)

  if no_nic and no_pas and no_cod == 1:
    print("Вы успешно вошли")
    app.destroy()
    interf_shifra.start()
