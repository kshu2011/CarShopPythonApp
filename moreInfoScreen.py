import tkinter as tk

INFO_CONSTANT = "On this page, one can choose to use filters or not. If filters are not used, all available " \
                "data will be displayed. If the filters are chosen, then only cars that have those features " \
                "will be displayed."


def setup_gui(main_help_window):
    """This will set up the GUI items for the MoreInfoScreen window"""

    help_title = tk.Label(main_help_window, text="More Information", font=('calibre', 10, 'bold'))
    help_title.grid(row=0)


def setup_help_text(main_help_window):
    """This function will set up text box and insert helpful information. """

    help_text = tk.Text(main_help_window, height=15, width=30)
    help_info = INFO_CONSTANT
    help_text.insert(tk.END, help_info)
    help_text.grid(row=1)


class MoreInfoScreen:
    """this class will create a window and display helpful information. """
    def __init__(self, root):
        """ This will create a login window by creating the main root window
         then calling setup_gui function to setup the rest."""

        main_help_window = tk.Toplevel(root)
        main_help_window.geometry("300x300")
        main_help_window.grid()
        setup_gui(main_help_window)
        setup_help_text(main_help_window)
