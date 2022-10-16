
import tkinter as tk

from AreYouSure import AreYouSureScreen


class AdvancedFilterScreen:

    def __init__(self, root, shopscreen):
        """ This will create a login window """

        self.root = root
        self.shopscreen = shopscreen

        main_help_window = tk.Toplevel(root)
        main_help_window.geometry("300x300")
        main_help_window.grid()

        help_title = tk.Label(main_help_window, text="Advanced Filter", font=('calibre', 10, 'bold'))
        help_title.grid(row=0)


        car_manufacturer_filter = tk.Label(main_help_window, text="Car Manufacturer: ", font=('calibre', 10, 'bold'))
        car_manufacturer_filter.grid(row=1)

        self.input_car_manufacturer = tk.Entry(main_help_window, font=('calibre', 10, 'bold'))
        self.input_car_manufacturer.grid(row=1, column=1)

        unique_filter = tk.Label(main_help_window, text="Unique Feature from user: ", font=('calibre', 10, 'bold'))
        unique_filter.grid(row=2)

        self.input_unique_filter = tk.Entry(main_help_window, font=('calibre', 10, 'bold'))
        self.input_unique_filter.grid(row=2, column=1)

        ok_button = tk.Button(main_help_window, text="ADD", command=self.submit)
        ok_button.grid(row=3)

    def submit(self):
        #self.shopscreen.set_advanced(self.input_car_manufacturer.get(), self.input_unique_filter.get())
        AreYouSureScreen(self.root, self.shopscreen, self.input_car_manufacturer.get(), self.input_unique_filter.get())


