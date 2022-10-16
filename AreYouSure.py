
import tkinter as tk


class AreYouSureScreen:

    def __init__(self, root, carshop, filter1, filter2):
        """ This will create a login window """
        self.shopscreen = carshop
        self.filter1 = filter1
        self.filter2 = filter2


        self.main_help_window = tk.Toplevel(root)
        self.main_help_window.geometry("300x300")
        self.main_help_window.grid()

        help_title = tk.Label(self.main_help_window, text="More Information", font=('calibre', 10, 'bold'))
        help_title.grid(row=0)

        help_text = tk.Text(self.main_help_window, height=15, width=30)
        help_info = "You are about to add advanced filters, are you sure?"
        help_text.insert(tk.END, help_info)
        help_text.grid(row=1)

        yes_button = tk.Button(self.main_help_window, text="YES", font=('calibre', 10, 'bold'), command=self.yes_button_action)
        yes_button.grid(row=2)

        no_button = tk.Button(self.main_help_window, text="NO", font=('calibre', 10, 'bold'), command=self.main_help_window.destroy)
        no_button.grid(row=2, column=1)

    def yes_button_action(self):
        self.shopscreen.set_advanced(self.filter1, self.filter2)
        self.main_help_window.destroy()



