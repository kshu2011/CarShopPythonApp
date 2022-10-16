# this will create a simple login screen
# resources used: https://www.pythontutorial.net/tkinter/tkinter-stringvar/ and
# https://www.geeksforgeeks.org/python-tkinter-entry-widget/
# will need to use pyinstaller to make it an executable? Need to update PATH? https://datatofish.com/add-python-to-windows-path/
# some other sources https://datatofish.com/executable-pyinstaller/
# https://pyinstaller.org/en/stable/usage.html
# https://docs.microsoft.com/en-us/sql/connect/python/pyodbc/step-1-configure-development-environment-for-pyodbc-python-development?view=sql-server-2017
# https://www.geeksforgeeks.org/open-a-new-window-with-a-button-in-python-tkinter/

# query with something like:
#     #query_mom_db('hil-sql03-svr', 'MOM', 'testing_with_dates.csv', '2022-06-03', '2022-06-08')

import tkinter as tk

from GuestCarShopScreen import GuestCarShopScreen
from LoginScreen import LoginScreen
from NewFeatures import NewFeaturesScreen
from mainHelpScreen import MainHelpScreen
from profileScreen import ProfileScreen


class MainScreen:
    """This class creates the main screen for the car shop application."""
    def __init__(self):
        """This initialize function will initialize the main window by using tkinter."""
        # create the main window
        self.root = tk.Tk()
        self.root.geometry("300x200")

        # create a frame that goes inside our main window and place it using grid
        frame = tk.Frame(self.root, padx=30, pady=30)
        frame.grid()
        # putting labels and buttons into our main window
        title_name = tk.Label(frame, text='Car Shop App.', font=('calibre', 20, 'bold'))
        title_name.grid(row=0)

        login_button = tk.Button(frame, text='Login', command=self.login_command)
        login_button.grid(row=2)

        new_user_button = tk.Button(frame, text='New User', command=self.new_user_command)
        new_user_button.grid(row=3)

        guest_button = tk.Button(frame, text='Guest View', command=self.guest_screen)
        guest_button.grid(row=4)

        new_features = tk.Button(frame, text='New Features!', command=self.new_features)
        new_features.grid(row=6)

        help_button = tk.Button(frame, text='Help', command=self.main_help_screen)
        help_button.grid(row=7, column=5)

        # start the window, or run it basically
        self.root.mainloop()

    def login_command(self):
        """ This will create a login window """
        LoginScreen(self.root)

    def main_help_screen(self):
        MainHelpScreen(self.root)

    def new_user_command(self):
        ProfileScreen(self.root)

    def guest_screen(self):
        GuestCarShopScreen(self.root)

    def new_features(self):
        NewFeaturesScreen(self.root)



