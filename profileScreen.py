"""This creates the profile screen, where the user gets to enter their
information and then they can create their profile."""

import tkinter as tk
from shopScreen import CarShopScreen


def setup_main_window(root):
    """The function will create the main window for
    this profile screen. And return it."""

    profile_window = tk.Toplevel(root)
    profile_window.geometry("350x350")
    profile_window.grid()
    return profile_window


def name_backgrnd_labels(profile_window):
    """This function sets up the name and color labels in the window."""

    name = tk.Label(profile_window, text="Name: ", font=('calibre', 10, 'bold'))
    name.grid(row=0)

    background_color = tk.Label(profile_window, text="Background Color: ", font=('calibre', 10, 'bold'))
    background_color.grid(row=1)


def user_pass_font_labels(profile_window):
    """This function sets up the username/password/font size labels in the window."""

    username = tk.Label(profile_window, text="Username: ", font=('calibre', 10, 'bold'))
    username.grid(row=3)

    password = tk.Label(profile_window, text="Password: ", font=('calibre', 10, 'bold'))
    password.grid(row=4)

    font_size = tk.Label(profile_window, text="Font size: ", font=('calibre', 10, 'bold'))
    font_size.grid(row=2)


def user_pass_textbox(profile_window):
    """This function creates the username/password text box and returns
    pointers to them."""

    username_is = tk.Entry(profile_window, font=('calibre', 10, 'bold'))
    username_is.grid(row=3, column=1)

    password_is = tk.Entry(profile_window, font=('calibre', 10, 'bold'))
    password_is.grid(row=4, column=1)
    return username_is, password_is


def name_color_font_textbox(profile_window):
    """This function sets up the name, color and font size entry text boxes."""

    name = tk.Entry(profile_window, font=('calibre', 10, 'bold'))
    name.grid(row=0, column=1)

    color = tk.Entry(profile_window, font=('calibre', 10, 'bold'))
    color.grid(row=1, column=1)

    size = tk.Entry(profile_window, font=('calibre', 10, 'bold'))
    size.grid(row=2, column=1)
    return name, color, size


class ProfileScreen:
    """this class creates the profile screen so users can enter their information
    and create their unique profiles."""

    def __init__(self, root):
        """ This will create a profile window """
        self._root = root
        current_window = setup_main_window(root)
        self.__setup_gui(current_window)
        self._users_inputs = list()

    def __setup_gui(self, profile_window):
        """Setups the main window gui by calling other helper methods"""

        name_backgrnd_labels(profile_window)
        user_pass_font_labels(profile_window)
        self.__setup_gui_helper(profile_window)

    def __setup_gui_helper(self, profile_window):
        """This function is a gui helper, it calls additional helper functions
        to create textbox guis."""

        self._input_username, self._input_password = user_pass_textbox(profile_window)
        self._reset_create_btn(profile_window)
        self._name, self._color, self._font_size = name_color_font_textbox(profile_window)

    def _reset_create_btn(self, profile_window):
        """This creates the reset and create profile buttons."""

        reset_button = tk.Button(profile_window, text="Reset", command=self._reset)
        reset_button.grid(row=5)

        create_profile_button = tk.Button(profile_window, text="Create Profile", command=self._create_profile)
        create_profile_button.grid(row=6, column=1)

    def _reset(self):
        """This function will reset all the fields to blank"""

        self._name.delete(0, 'end')
        self._color.delete(0, 'end')
        self._font_size.delete(0, 'end')

    def _create_profile(self):
        """This will save all user inputed information so it can be saved
        to their profile. And then it starts the car shop screen."""

        extra_data = [self._name.get(), self._color.get(), self._font_size.get(),
                      self._input_username.get(), self._input_password.get()]
        self._save_user_profile(extra_data.copy())
        CarShopScreen(self._root, extra_data)

    def _save_user_profile(self, extras):
        """This function saves the users data into a text file, so that it
        can be retrieved at a later time."""

        file_obj = open(self._input_username.get() + ".txt", "w")
        for i in range(len(extras) - 1):
            extras[i] = extras[i] + ","
        file_obj.writelines(extras)
        file_obj.close()
