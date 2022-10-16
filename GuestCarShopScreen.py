import tkinter as tk


class GuestCarShopScreen:

    def __init__(self, root):

        car_shop_window = tk.Toplevel(root)
        car_shop_window.geometry("450x450")
        car_shop_window.grid()

        filter_title = tk.Label(car_shop_window, text="     Filters", font=('calibre', 15, 'bold'))
        filter_title.grid(row=0)

        # reset_button = tk.Button(car_shop_window, text="Reset Filter", font=('calibre', 10, 'bold'), command=self.reset)
        # reset_button.grid(row=0, column=1)

        color_filter = tk.Label(car_shop_window, text="Color: ", font=('calibre', 10, 'bold'))
        color_filter.grid(row=1)

        # self.input_color = tk.Entry(car_shop_window, font=('calibre', 10, 'bold'))
        # self.input_color.grid(row=1, column=1)

        mpg_filter = tk.Label(car_shop_window, text="MPG: ", font=('calibre', 10, 'bold'))
        mpg_filter.grid(row=2)

        # self.input_mpg = tk.Entry(car_shop_window, font=('calibre', 10, 'bold'))
        # self.input_mpg.grid(row=2, column=1)

        transmission_filter = tk.Label(car_shop_window, text="Transmission: ", font=('calibre', 10, 'bold'))
        transmission_filter.grid(row=3)

        # self.input_transmission = tk.Entry(car_shop_window, font=('calibre', 10, 'bold'))
        # self.input_transmission.grid(row=3, column=1)

        # advanced_filter = tk.Button(car_shop_window, text="Advanced Filter", font=('calibre', 10, 'bold'))
        # advanced_filter.grid(row=4)
        #
        # search_button = tk.Button(car_shop_window, text="Search", font=('calibre', 10, 'bold'), command=self.search)
        # search_button.grid(row=5)

        # create listbox object
        self.listbox = tk.Listbox(car_shop_window, height=20, width=30, bg="grey", activestyle='dotbox', font="Helvetica", fg="yellow")
        self.listbox.insert(1, "*Default data*")
        self.listbox.insert(2, "*Default data*")
        self.listbox.insert(3, "*Default data*")

        self.listbox.grid(row=7)

    def reset(self):
        self.input_color.delete(0,'end')
        self.input_mpg.delete(0, 'end')
        self.input_transmission.delete(0,'end')

    def search(self):
        input_color_str = self.input_color.get()
        input_mpg_str = self.input_mpg.get()
        input_transmission_str = self.input_transmission.get()
        #
        # # now display some data based on the input....
        # self.help_text.delete(1.0,'end')
        # self.help_text.insert(tk.END, input_color_str+input_mpg_str+input_transmission_str)







