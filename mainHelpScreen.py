
import tkinter as tk


class MainHelpScreen:

    def __init__(self, root):
        """ This will create a login window """
        main_help_window = tk.Toplevel(root)
        main_help_window.geometry("300x300")
        main_help_window.grid()

        help_title = tk.Label(main_help_window, text="Help Page", font=('calibre', 10, 'bold'))
        help_title.grid(row=0)

        help_text = tk.Text(main_help_window, height=15, width=30)
        help_info = "Hello, welcome to the Car Shop App. On the main page, there are three options: login - if" \
                    "already have a profile can login immediately, new user - use this option to create a new profile" \
                    "and guest view - can use the app as guest with limited capabilities."
        help_text.insert(tk.END, help_info)
        help_text.grid(row=1)