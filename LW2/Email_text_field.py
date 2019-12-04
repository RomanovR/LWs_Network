import pickle
import socket
import tkinter as tk
from platform import system

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 49001        # The port used by the server

def send_event():
    # Network
    print(e_to.get())
    print(e_theme.get())
    print(t_main_text.get("1.0", 'end-1c'))

    to_send = pickle.dumps({'To': e_to.get(),
                            'Theme': e_theme.get(),
                            'Mail': t_main_text.get("1.0", 'end-1c')})

    b_send['fg'] = 'gray50'
    b_send['text'] = 'Sending...'
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
        except ConnectionRefusedError:
            print('Connection refused.')
            b_send['text'] = 'Error.'

        else:
            s.sendall(to_send)
            print('Sent.')
            b_send['text'] = 'Sent.'


def about_event():
    about = tk.Tk()
    s_about = ''' Приложение связывается с консольным приложением через TCP, чтобы отправить через него письмо по SMTP.\n
    Адрес отправки: xdrond.bot@gmail.com\n
    2019. Романов Р.'''
    m_about = tk.Message(about,
                         width=200,
                         text=s_about,
                         font="Helvetica 13")
    m_about.pack(expand=True, fill=tk.BOTH)
    about.title("About app")
    window_width_about = 300
    window_height_about = 200
    x_screen_pos_about = about.winfo_screenwidth() // 2 - window_width_about // 2
    y_screen_pos_about = about.winfo_screenheight() // 2 - window_height_about // 2
    about.geometry('{}x{}+{}+{}'.format(window_width_about, window_height_about, x_screen_pos_about, y_screen_pos_about))
    about.resizable(False, False)
    about.mainloop()

root = tk.Tk()
root.title("Email sender")
window_width = 377
window_height = 352
x_screen_pos = root.winfo_screenwidth() // 2 - window_width // 2
y_screen_pos = root.winfo_screenheight() // 2 - window_height // 2
root.geometry('{}x{}+{}+{}'.format(window_width, window_height, x_screen_pos, y_screen_pos))
root.resizable(False, False)

platformD = system()
if platformD == 'Darwin':

    logo_image = 'images/logo.icns'

elif platformD == 'Windows':

    logo_image = 'images/logo.ico'

else:

    logo_image = 'images/logo.xbm'
root.iconbitmap(logo_image)

l_to = tk.Label(root,
                fg='black',
                font="Helvetica 12")
l_to['text'] = 'To:'
l_to.grid(row=0,
          column=0,
          ipadx=1,
          ipady=1,
          padx=6,
          pady=6,
          sticky='w')


l_theme = tk.Label(root, fg='black', font="Helvetica 12")
l_theme['text'] = 'Theme:'
l_theme.grid(row=1,
             column=0,
             ipadx=1,
             ipady=1,
             padx=6,
             pady=6,
             sticky='w')

s_recipient = 'xdrond@gmail.com'
e_to = tk.Entry(root,
                textvariable=s_recipient,
                width=40,
                fg='black',
                bg='white',
                font="Helvetica 12",
                relief="ridge",
                borderwidth=1,
                highlightthickness=3,
                highlightcolor='#b3d7ff')
e_to.grid(row=0,
          column=1,
          ipadx=1,
          ipady=1,
          padx=6,
          pady=6,
          columnspan=4)
e_to.focus()

s_theme = "Test mail"
e_theme = tk.Entry(root,
                   textvariable=s_theme,
                   width=40,
                   fg='black',
                   bg='white',
                   font="Helvetica 12",
                   relief="ridge",
                   borderwidth=1,
                   highlightthickness=3,
                   highlightcolor='#b3d7ff')
e_theme.grid(row=1,
             column=1,
             ipadx=1,
             ipady=1,
             padx=6,
             pady=6,
             columnspan=3)

main_text = "Send from \"Email sender\" app"
t_main_text = tk.Text(root,
                      width=50,
                      height=15,
                      font="Helvetica 12",
                      wrap=tk.WORD,
                      relief="ridge",
                      borderwidth=1,
                      highlightthickness=3,
                      highlightcolor='#b3d7ff')
t_main_text.grid(row=2,
                 column=0,
                 ipadx=1,
                 ipady=1,
                 padx=8,
                 pady=8,
                 rowspan=2,
                 columnspan=4)

scroll = tk.Scrollbar(root, command=t_main_text.yview)
scroll.grid(row=2,
            column=3,
            rowspan=2,
            ipadx=1,
            ipady=1,
            padx=13,
            pady=13,
            sticky='nes')

t_main_text.config(yscrollcommand=scroll.set)

b_send = tk.Button(root,
                   text='Send',
                   width=12,
                   height=1,
                   font='Helvetica 12')
b_send.config(command=send_event)
b_send.grid(row=4,
            column=0,
            ipadx=1,
            ipady=1,
            padx=8,
            pady=5,
            columnspan=3,
            sticky='w')

b_about = tk.Button(root,
                    text='About',
                    width=9,
                    height=1,
                    font='Helvetica 12')
b_about.config(command=about_event)
b_about.grid(row=4,
             column=3,
             ipadx=1,
             ipady=1,
             padx=8,
             pady=5,
             columnspan=3,
             sticky='e')

root.mainloop()

