
import tkinter as tk


class MoreInfoScreen:

    def __init__(self, root):
        """ This will create a login window """
        main_help_window = tk.Toplevel(root)
        main_help_window.geometry("300x300")
        main_help_window.grid()

        help_title = tk.Label(main_help_window, text="More Information", font=('calibre', 10, 'bold'))
        help_title.grid(row=0)

        help_text = tk.Text(main_help_window, height=15, width=30)
        help_info = "On this page, one can choose to use filters or not. If filters are not used, all available data" \
                    "will be displayed. If the filters are chosen, then only cars that have those features will be displayed."
        help_text.insert(tk.END, help_info)
        help_text.grid(row=1)