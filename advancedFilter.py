"""This is the advanced filter window, it allows user to enter advanced filter settings."""

import tkinter as tk
from AreYouSure import AreYouSureScreen


def setup_main_window(root):
    """this function set up the main window and returns it. """

    main_help_window = tk.Toplevel(root)
    main_help_window.geometry("300x300")
    main_help_window.grid()
    return main_help_window


def setup_label_gui(main_help_window):
    """This will set up the label GUI. """

    help_title = tk.Label(main_help_window, text="Advanced Filter", font=('calibre', 10, 'bold'))
    help_title.grid(row=0)

    unique_filter = tk.Label(main_help_window, text="Unique Feature from user: ", font=('calibre', 10, 'bold'))
    unique_filter.grid(row=2)


class AdvancedFilterScreen:
    """this creates the advanced filter screen."""
    def __init__(self, root, shop_screen):
        """ This will create a login window """

        self._root = root
        self._shop_screen = shop_screen
        main_window = setup_main_window(root)
        setup_label_gui(main_window)
        self._setup_textbox_button(main_window)

    def _setup_textbox_button(self, main_help_window):
        """This will set up the button and text box."""

        self._input_unique_filter = tk.Entry(main_help_window, font=('calibre', 10, 'bold'))
        self._input_unique_filter.grid(row=2, column=1)

        ok_button = tk.Button(main_help_window, text="ADD", command=self.submit)
        ok_button.grid(row=3)

    def submit(self):
        """This function will create the AreYouSureScreen when called. So that the user can
        interact with it."""

        AreYouSureScreen(self._root, self._shop_screen, self._input_unique_filter.get())
