import tkinter as tk

root = tk.Tk()

root.title("Email sender")
window_width = 550
window_height = 380
x_screen_pos = root.winfo_screenwidth() // 2 - window_width // 2
y_screen_pos = root.winfo_screenheight() // 2 - window_height // 2
root.geometry('{}x{}+{}+{}'.format(window_width, window_height, x_screen_pos, y_screen_pos))
root.resizable(False, False)
root.iconbitmap('email.ico')

l_to = tk.Label(root, fg='black', font="Helvetica 10")
l_to['text'] = 'To:'
l_to.grid(row=0, column=0, ipadx=1, ipady=1, padx=6, pady=6, sticky='e')


l_theme = tk.Label(root, fg='black', font="Helvetica 10")
l_theme['text'] = 'Theme:'
l_theme.grid(row=1, column=0, ipadx=1, ipady=1, padx=6, pady=6, sticky='e')

s_recipient = 'xdrond@gmail.com'
e_to = tk.Entry(root, textvariable=s_recipient, width=20, fg='black', bg='white', font="Helvetica 10")
e_to.grid(row=0, column=1, ipadx=1, ipady=1, padx=6, pady=6, columnspan=3)

s_theme = "Test mail"
e_theme = tk.Entry(root, textvariable=s_theme, width=20, fg='black', bg='white', font="Helvetica 10")
e_theme.grid(row=1, column=1, ipadx=1, ipady=1, padx=6, pady=6, columnspan=3)

main_text = "Send from \"Email sender\" app"
t_main_text = tk.Text(width=65, height=15)
t_main_text.grid(row=2, column=0, ipadx=1, ipady=1, padx=8, pady=8, rowspan=5, columnspan=4)

root.mainloop()

# row = 4(0-4)
# column = 7(0-7)