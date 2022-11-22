import tkinter as tk

from shopScreen import CarShopScreen
import os.path

PATH = "//users//kshu//desktop//other_desktop_stuff//cse//osu_post_bacc//cs_361//CarShopApp2//"

class LoginScreen:
    """ This class will create the login screen window for the app."""

    def __init__(self, root):
        """ this will initialize all the variables in order to create
        the screen for login."""

        self.root = root
        # username_input_str = tk.StringVar()
        # password_input_str = tk.StringVar()
        login_window = tk.Toplevel(root)
        login_window.geometry("250x150")
        login_window.grid()
        self.login_screen_gui1(login_window)
        self.login_screen_gui2(login_window)

    def login_screen_gui1(self, login_window):
        """this function will take care of creating all the login gui for this screen."""
        username = tk.Label(login_window, text="Username", font=('calibre', 10, 'bold'))
        username.grid(row=0)

        self.username_input = tk.Entry(login_window, font=('calibre', 10, 'bold'))
        self.username_input.grid(row=0, column=1)

    def login_screen_gui2(self, login_window):
        password = tk.Label(login_window, text="Password", font=('calibre', 10, 'bold'))
        password.grid(row=1)

        self.password_input = tk.Entry(login_window, font=('calibre', 10, 'bold'))
        self.password_input.grid(row=1, column=1)

        login_button = tk.Button(login_window, text='Login', command=self.login_to_profile)
        login_button.grid(row=2, column=0)

    def login_to_profile(self):
        """This will check to see if login credentials are correct
        if so it will log the user in. And display the main car shop screen"""
        # do some checking here, see if login information is correct/exist
        if self.password_input.get() and self.username_input.get():  # need to have inputs
            if os.path.isfile(PATH + self.username_input.get() + ".txt"): #this username exists
                user_profile = open(self.username_input.get() + ".txt", "r")
                info = user_profile.readline().split(",")
                if info[-1] == self.password_input.get():
                    CarShopScreen(self.root, info)


if __name__=="__main__":
    username = input("enter user name: ")
    password = input("enter password: ")

    if username and password:  # need to have inputs
        if os.path.isfile(PATH + username + ".txt"):  # this username exists
            user_profile = open(username + ".txt", "r")
            info = user_profile.readline().split(",")
            print(info)
            if info[-1] == password:
                #CarShopScreen(self.root)
                print("made it")