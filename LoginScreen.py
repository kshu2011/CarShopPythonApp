
import tkinter as tk

from profileScreen import ProfileScreen
from shopScreen import CarShopScreen


class LoginScreen:

    def __init__(self, root):
        """ This will create a login window """

        self.root = root

        username_input_str = tk.StringVar()
        password_input_str = tk.StringVar()

        login_window = tk.Toplevel(root)
        login_window.geometry("250x150")
        login_window.grid()



        username = tk.Label(login_window, text="Username", font=('calibre', 10, 'bold'))
        username.grid(row=0)

        username_input = tk.Entry(login_window, textvariable=username_input_str, font=('calibre', 10, 'bold'))
        username_input.grid(row=0,column=1)

        password = tk.Label(login_window, text="Password", font=('calibre', 10, 'bold'))
        password.grid(row=1)

        password_input = tk.Entry(login_window, textvariable=password_input_str, font=('calibre', 10, 'bold'))
        password_input.grid(row=1,column=1)

        login_button = tk.Button(login_window, text='Login', command=self.login_to_profile)
        login_button.grid(row=2, column=0)

    def login_to_profile(self):
        # do some checking here, see if login information is correct/exist



        CarShopScreen(self.root)