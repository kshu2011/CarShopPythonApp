"""This is the main menu screen, it will create a menu where the user can choose
how to navigate/use the application."""

"""Resources used: 
https://www.pythontutorial.net/tkinter/tkinter-stringvar/ and
https://www.geeksforgeeks.org/python-tkinter-entry-widget/
will need to use pyinstaller to make it an executable? Need to update PATH? 
https://datatofish.com/add-python-to-windows-path/
https://datatofish.com/executable-pyinstaller/
https://pyinstaller.org/en/stable/usage.html
https://docs.microsoft.com/en-us/sql/connect/python/pyodbc/step-1-configure-development-environment-for-pyodbc-python-development?view=sql-server-2017
https://www.geeksforgeeks.org/open-a-new-window-with-a-button-in-python-tkinter/"""

import tkinter as tk

from PreviewCarShopScreen import PreviewCarShopScreen
from LoginScreen import LoginScreen
from NewFeatures import NewFeaturesScreen
from mainHelpScreen import MainHelpScreen
from profileScreen import ProfileScreen


def setup_root_window():
    """Function will set up the root window - which is the main window
    for this application."""
    root = tk.Tk()
    root.geometry("300x200")
    frame = tk.Frame(root, padx=30, pady=30)
    frame.grid()
    return frame, root


def title_label(frame):
    """Function sets up the title for this window."""
    title_name = tk.Label(frame, text='Car Shop App Menu.', font=('calibre', 20, 'bold'))
    title_name.grid(row=0)


class MainScreen:
    """This class creates the main screen for the car shop application."""

    def __init__(self):
        """Initializes the window and calls functions to create GUI's."""
        self._frame, self._root = setup_root_window()
        self.__setup_gui(self._frame)
        self._root.mainloop()

    def __setup_gui(self, frame):
        """Function will call all necessary function to setup GUI's."""
        title_label(frame)
        self.__login_new_user_btn(frame)
        self.__guest_feature_btn(frame)
        self.__help_btn(frame)

    def __login_new_user_btn(self, frame):
        """Function creates login and new user buttons."""
        login_button = tk.Button(frame, text='Login', command=self.__login_command)
        login_button.grid(row=2)

        new_user_button = tk.Button(frame, text='New User', command=self.__new_user_command)
        new_user_button.grid(row=3)

    def __guest_feature_btn(self, frame):
        """Function creates guest, and new features buttons."""
        preview_button = tk.Button(frame, text='Preview', command=self.__preview_screen)
        preview_button.grid(row=4)

        new_features = tk.Button(frame, text='New Features!', command=self.__new_features)
        new_features.grid(row=6)

    def __help_btn(self, frame):
        """Function sets up the help button."""
        help_button = tk.Button(frame, text='Help', command=self.__main_help_screen)
        help_button.grid(row=7, column=5)

    def __login_command(self):
        """ This will create a login window """
        LoginScreen(self._root)

    def __main_help_screen(self):
        """This will create the main help screen"""
        MainHelpScreen(self._root)

    def __new_user_command(self):
        """this will create the profile screen"""
        ProfileScreen(self._root)

    def __preview_screen(self):
        """this will create the guest car shop screen"""
        PreviewCarShopScreen(self._root)

    def __new_features(self):
        """this will create the new features screen"""
        NewFeaturesScreen(self._root)
