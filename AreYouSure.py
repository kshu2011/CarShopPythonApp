import tkinter as tk


def setup_main_window(root):
    """this function sets up the window for this."""

    main_help_window = tk.Toplevel(root)
    main_help_window.geometry("300x300")
    main_help_window.grid()
    return main_help_window


def title_label(main_help_window):
    """This function takes care of creating the label for the screen."""

    help_title = tk.Label(main_help_window, text="More Information", font=('calibre', 10, 'bold'))
    help_title.grid(row=0)


def help_textbox(main_help_window):
    """This function takes care of setting up the help textbox."""

    help_text = tk.Text(main_help_window, height=15, width=30)
    help_info = "You are about to add advanced filters, are you sure?"
    help_text.insert(tk.END, help_info)
    help_text.grid(row=1)


class AreYouSureScreen:
    """this class takes care of creating the Are You Sure screen."""

    def __init__(self, root, carshop, filter2):
        """ Initializes all the necassary private variables. """

        self._shop_screen = carshop
        self._filter2 = filter2
        self._main_window = setup_main_window(root)
        self.setup_gui(self._main_window)

    def setup_gui(self, main_help_window):
        """this function calls helper methods to setup the gui."""

        title_label(main_help_window)
        help_textbox(main_help_window)
        self._setup_button(main_help_window)

    def _setup_button(self, main_help_window):
        """this function set up the buttons - yes, no buttons."""

        yes_button = tk.Button(main_help_window, text="YES", font=('calibre', 10, 'bold'),
                               command=self._yes_button_action)
        yes_button.grid(row=2)

        no_button = tk.Button(main_help_window, text="NO", font=('calibre', 10, 'bold'),
                              command=main_help_window.destroy)
        no_button.grid(row=2, column=1)

    def _yes_button_action(self):
        """This function is the action of 'Yes' button, it will save the extra
        function user has entered."""

        self._shop_screen.set_advanced(self._filter2)
        self._main_window.destroy()
