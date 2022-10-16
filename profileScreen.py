
import tkinter as tk

from shopScreen import CarShopScreen


class ProfileScreen:

    def __init__(self, root):
        """ This will create a profile window """
        self.root = root

        input_name_str = tk.StringVar()
        fav_color_input_str = tk.StringVar()
        mpg_input_str = tk.StringVar()
        transmission_input_str = tk.StringVar()

        profile_window = tk.Toplevel(root)
        profile_window.geometry("350x350")
        profile_window.grid()

        name = tk.Label(profile_window, text="Name: ", font=('calibre', 10, 'bold'))
        name.grid(row=0)

        self.input_name = tk.Entry(profile_window, textvariable=input_name_str, font=('calibre', 10, 'bold'))
        self.input_name.grid(row=0, column=1)

        fav_color = tk.Label(profile_window, text="Favorite Color: ", font=('calibre', 10, 'bold'))
        fav_color.grid(row=1)

        self.input_fav_color = tk.Entry(profile_window, textvariable=fav_color_input_str, font=('calibre', 10, 'bold'))
        self.input_fav_color.grid(row=1, column=1)

        mpg = tk.Label(profile_window, text="MPG: ", font=('calibre', 10, 'bold'))
        mpg.grid(row=2)

        self.input_mpg = tk.Entry(profile_window, textvariable=mpg_input_str, font=('calibre', 10, 'bold'))
        self.input_mpg.grid(row=2,column=1)

        transmission = tk.Label(profile_window, text="Transmission: ", font=('calibre', 10, 'bold'))
        transmission.grid(row=3)

        self.input_transmission = tk.Entry(profile_window, textvariable=transmission_input_str, font=('calibre', 10, 'bold'))
        self.input_transmission.grid(row=3,column=1)

        additional_opt_button = tk.Button(profile_window, text="Additional Options", command=self.additional_options)
        additional_opt_button.grid(row=4)

        reset_button = tk.Button(profile_window, text="Rest", command=self.reset)
        reset_button.grid(row=5)

        create_profile_button = tk.Button(profile_window, text="Create Profile", command=self.create_profile)
        create_profile_button.grid(row=6,column=1)

    def additional_options(self):
        print("open up additional options")

    def reset(self):
        self.input_name.delete(0,'end')
        self.input_fav_color.delete(0, 'end')
        self.input_mpg.delete(0,'end')
        self.input_transmission.delete(0,'end')

    def create_profile(self):
        extra_data = list()
        extra_data.append(self.input_fav_color.get())
        extra_data.append(self.input_mpg.get())
        extra_data.append(self.input_transmission.get())
        CarShopScreen(self.root, extra_data)





