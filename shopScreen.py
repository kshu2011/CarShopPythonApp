import tkinter as tk

from advancedFilter import AdvancedFilterScreen
from moreInfoScreen import MoreInfoScreen


class CarShopScreen:

    def __init__(self, root, extra_data=None):
        self.root = root




        self.advanced_filter_str = None
        self.unique_filter_str = None

        car_shop_window = tk.Toplevel(root)
        car_shop_window.geometry("550x550")
        car_shop_window.grid()

        filter_title = tk.Label(car_shop_window, text="     Filters", font=('calibre', 15, 'bold'))
        filter_title.grid(row=0)

        reset_button = tk.Button(car_shop_window, text="Reset Filter", font=('calibre', 10, 'bold'), command=self.reset)
        reset_button.grid(row=0, column=1)

        color_filter = tk.Label(car_shop_window, text="Color: ", font=('calibre', 10, 'bold'))
        color_filter.grid(row=1)

        self.input_color = tk.Entry(car_shop_window, font=('calibre', 10, 'bold'))
        self.input_color.grid(row=1, column=1)

        color_filter_explanation = tk.Label(car_shop_window, text="Exterior color of car", font=('calibre', 8))
        color_filter_explanation.grid(row=2)

        mpg_filter = tk.Label(car_shop_window, text="MPG: ", font=('calibre', 10, 'bold'))
        mpg_filter.grid(row=3)

        self.input_mpg = tk.Entry(car_shop_window, font=('calibre', 10, 'bold'))
        self.input_mpg.grid(row=3, column=1)

        mpg_filter_explanation = tk.Label(car_shop_window, text="Mile per gallon", font=('calibre', 8))
        mpg_filter_explanation.grid(row=4)

        transmission_filter = tk.Label(car_shop_window, text="Transmission: ", font=('calibre', 10, 'bold'))
        transmission_filter.grid(row=5)

        self.input_transmission = tk.Entry(car_shop_window, font=('calibre', 10, 'bold'))
        self.input_transmission.grid(row=5, column=1)

        transmission_filter_explanation = tk.Label(car_shop_window, text="Automatic/Manual", font=('calibre', 8))
        transmission_filter_explanation.grid(row=6)

        advanced_filter = tk.Button(car_shop_window, text="Advanced Filter", font=('calibre', 10, 'bold'), command=self.advanced_filter_set)
        advanced_filter.grid(row=7)

        search_button = tk.Button(car_shop_window, text="Search", font=('calibre', 10, 'bold'), command=self.search)
        search_button.grid(row=8)


        # results_text = "**Results will be shown here**"
        # if extra_data:
        #     results_text = "Unique data based on user profile"
        #
        # self.result_text = tk.Text(car_shop_window, height=15, width=30)
        # self.result_text.insert(tk.END, results_text)
        # self.result_text.grid(row=6)

        #let's try listbox instead
        # create listbox object
        self.listbox = tk.Listbox(car_shop_window, height=20, width=30, bg="grey", activestyle='dotbox', font="Helvetica", fg="yellow")
        # self.listbox.insert(1, "Nachos")
        # self.listbox.insert(2, "Sandwich")
        # self.listbox.insert(3, "Burger")

        self.listbox.grid(row=9)

        more_info_button = tk.Button(car_shop_window, text='More Info.', command=self.more_info_screen)
        more_info_button.grid(row=10, column=1)

        self.extra_data = extra_data
        if self.extra_data:
            for index in range(len(self.extra_data)):
                self.listbox.insert(index+1, self.extra_data[index])

    def reset(self):
        self.input_color.delete(0,'end')
        self.input_mpg.delete(0, 'end')
        self.input_transmission.delete(0,'end')
        self.advanced_filter_str = None
        self.unique_filter_str = None

    def search(self):

        input_color_str = self.input_color.get()
        input_mpg_str = self.input_mpg.get()
        input_transmission_str = self.input_transmission.get()

        # now display some data based on the input....
        # self.result_text.delete(1.0, 'end')
        # self.result_text.insert(tk.END, input_color_str + input_mpg_str + input_transmission_str)
        self.listbox.delete(0, 'end')

        self.listbox.insert(1, input_color_str)
        self.listbox.insert(2, input_mpg_str)
        self.listbox.insert(3, input_transmission_str)
        if self.advanced_filter_str:
            self.listbox.insert(4, self.advanced_filter_str)
        if self.unique_filter_str:
            self.listbox.insert(5, self.unique_filter_str)


    def advanced_filter_set(self):
        AdvancedFilterScreen(self.root, self)

    def set_advanced(self, input_filter, unique_filter):
        self.advanced_filter_str = input_filter
        self.unique_filter_str = unique_filter

    def more_info_screen(self):
        MoreInfoScreen(self.root)






