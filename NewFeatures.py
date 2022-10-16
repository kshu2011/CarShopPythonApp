
import tkinter as tk


class NewFeaturesScreen:

    def __init__(self, root):
        """ This will create a login window """
        main_help_window = tk.Toplevel(root)
        main_help_window.geometry("350x150")
        main_help_window.grid()

        help_title = tk.Label(main_help_window, text="New Features!", font=('calibre', 10, 'bold'))
        help_title.grid(row=0)

        help_text = tk.Text(main_help_window, height=5, width=50)
        help_info = "Now you can filter cars by MPG! This is filter option can be found under the filters section " \
                    "on the car shop screen."
        help_text.insert(tk.END, help_info)
        help_text.grid(row=1)

        ok_button = tk.Button(main_help_window, text="OK", command=main_help_window.destroy)
        ok_button.grid(row=2)