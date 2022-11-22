import tkinter as tk

NEW_FEATURE = "Now you can filter cars by MPG! This is filter option can be found under the filters section " \
              "on the car shop screen."


class NewFeaturesScreen:

    def __init__(self, root):
        """ This will create a login window """
        main_help_window = tk.Toplevel(root)
        main_help_window.geometry("350x150")
        main_help_window.grid()

        self.setup_gui(main_help_window)

    def setup_gui(self, main_window):
        """This function will setup the GUI items for the features screen."""
        help_title = tk.Label(main_window, text="New Features!", font=('calibre', 10, 'bold'))
        help_title.grid(row=0)

        help_text = tk.Text(main_window, height=5, width=50)
        help_text.insert(tk.END, NEW_FEATURE)
        help_text.grid(row=1)

        ok_button = tk.Button(main_window, text="OK", command=main_window.destroy)
        ok_button.grid(row=2)