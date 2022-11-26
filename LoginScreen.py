"""This will set up the login screen, allows user to enter username/password to login."""

import tkinter as tk
from shopScreen import CarShopScreen
import os.path

CONST_PATH = "//users//kshu//desktop//other_desktop_stuff//cse//osu_post_bacc//cs_361//CarShopApp2//"


def setup_main_window(root):
    """The function will set up the login window and return it"""
    login_window = tk.Toplevel(root)
    login_window.geometry("250x150")
    login_window.grid()
    return login_window


def setup_labels(login_window):
    """The function sets up the labels in the window."""

    username_label = tk.Label(login_window, text="Username", font=('calibre', 10, 'bold'))
    username_label.grid(row=0)

    password_label = tk.Label(login_window, text="Password", font=('calibre', 10, 'bold'))
    password_label.grid(row=1)


def setup_textbox(login_window):
    """This function will set up all the textbox GUI's. """

    username_input = tk.Entry(login_window, font=('calibre', 10, 'bold'))
    username_input.grid(row=0, column=1)

    password_input = tk.Entry(login_window, font=('calibre', 10, 'bold'))
    password_input.grid(row=1, column=1)
    return username_input, password_input


class LoginScreen:
    """ This class will create the login screen window for the app."""

    def __init__(self, root):
        """ this will initialize all the variables in order to create
        the screen for login."""

        self._root = root
        current_window = setup_main_window(root)
        self._username_input, self._password_input = self.__setup_gui(current_window)

    def __setup_gui(self, login_window):
        """This function will call other helper functions to setup
        all the GUI for this login window. And returns the pointers to
        username input and password inputs."""

        setup_labels(login_window)
        username_is, password_is = setup_textbox(login_window)
        self.__setup_login_btn(login_window)
        return username_is, password_is

    def __setup_login_btn(self, login_window):
        """This function will set up the login button."""

        login_button = tk.Button(login_window, text='Login', command=self.login_to_profile)
        login_button.grid(row=2, column=0)

    def login_to_profile(self):
        """This will check to see if login credentials are correct
        if so it will log the user in. And display the main car shop screen"""

        if self._password_input.get() and self._username_input.get():  # need to have inputs
            if os.path.isfile(CONST_PATH + self._username_input.get() + ".txt"):  # this username exists
                info_data = open(self._username_input.get() + ".txt", "r").readline().split(',')
                if info_data[-1] == self._password_input.get():
                    CarShopScreen(self._root, info_data)


if __name__ == "__main__":
    # testing login function
    username = input("enter user name: ")
    password = input("enter password: ")

    if username and password:  # need to have inputs
        if os.path.isfile(CONST_PATH + username + ".txt"):  # this username exists
            user_profile = open(username + ".txt", "r")
            info = user_profile.readline().split(",")
            print(info)
            if info[-1] == password:
                # CarShopScreen(self.root)
                print("made it")
