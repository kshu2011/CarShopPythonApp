import tkinter as tk

NEW_FEATURE = "Now you can filter cars by MPG! This is filter option can be found under the filters section " \
              "on the car shop screen."


def setup_main_window(root):
    """This function sets up the main window.
    and returns the window """

    main_help_window = tk.Toplevel(root)
    main_help_window.geometry("350x150")
    main_help_window.grid()
    return main_help_window


def title_and_button(main_window):
    """This function sets up the title label and ok button."""

    help_title = tk.Label(main_window, text="New Features!", font=('calibre', 10, 'bold'))
    help_title.grid(row=0)

    ok_button = tk.Button(main_window, text="OK", command=main_window.destroy)
    ok_button.grid(row=2)


def help_text(main_window):
    """This sets up the help text information to be displayed."""

    help_textbox = tk.Text(main_window, height=5, width=50)
    help_textbox.insert(tk.END, NEW_FEATURE)
    help_textbox.grid(row=1)


def setup_gui(main_window):
    """This function will setup the GUI items for the features screen."""

    title_and_button(main_window)
    help_text(main_window)


class NewFeaturesScreen:
    """This is the new features screen class, it will create a new screen
    to display information on new features."""

    def __init__(self, root):
        """ This will create a login window by calling helper functions
        to set up the necessary gui."""
        main_help_window = setup_main_window(root)
        setup_gui(main_help_window)

