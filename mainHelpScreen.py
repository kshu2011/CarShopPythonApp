"""This is the help window - it will create a window that display helpful information
to the user."""

import tkinter as tk

HELP_TEXT = "Hello, welcome to the Car Shop App. On the main page, there are three options: login - if" \
            "already have a profile can login immediately, new user - use this option to create " \
            "a new profile and guest view - can use the app as guest with limited capabilities."


def setup_main_window(root):
    """This will set up the main window for this help screen."""

    main_help_window = tk.Toplevel(root)
    main_help_window.geometry("300x300")
    main_help_window.grid()
    return main_help_window


def title_label(main_help_window):
    """This creates the title label for the window."""

    help_title = tk.Label(main_help_window, text="Help Page", font=('calibre', 10, 'bold'))
    help_title.grid(row=0)


def help_textbox(main_help_window):
    """This creates the help textbox for the window."""

    help_text = tk.Text(main_help_window, height=15, width=30)
    help_info = HELP_TEXT
    help_text.insert(tk.END, help_info)
    help_text.grid(row=1)


def setup_gui(main_help_window):
    """ this will set up all the gui for the main help screen."""

    title_label(main_help_window)
    help_textbox(main_help_window)


class MainHelpScreen:
    """this class object creates the help screen, it will display helpful
    information to the user."""
    def __init__(self, root):
        """ Initializes the main window and calls setup_gui function to
         set up the gui's."""

        main_window = setup_main_window(root)
        setup_gui(main_window)

