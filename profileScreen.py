
import tkinter as tk
from shopScreen import CarShopScreen


class ProfileScreen:
    """this class creates the profile screen so users can enter their information
    and create their unique profiles."""
    def __init__(self, root):
        """ This will create a profile window """
        self.root = root
        # input_name_str = tk.StringVar()
        # background_color_str = tk.StringVar()
        # font_size_str = tk.StringVar()
        # username_str = tk.StringVar()
        # password_str = tk.StringVar()
        # variables = [input_name_str, background_color_str, font_size_str,
        #              username_str, password_str]
       ## self.setup_root(self.root, variables)
        self.setup_root(self.root)
        self.users_inputs = list()

    def setup_root(self, root):
        """Setups the main window gui by calling other helper methods"""
        profile_window = tk.Toplevel(root)
        profile_window.geometry("350x350")
        profile_window.grid()

        # self.profile_screen_part1(profile_window, var[0], var[1])
        # self.profile_screen_part2(profile_window, var[2], var[3])
        # self.profile_screen_part3(profile_window, var[4])

        self.profile_screen_part1(profile_window)
        self.profile_screen_part2(profile_window)
        self.profile_screen_part3(profile_window)

    def profile_screen_part1(self, profile_window):
        """This will create the first part of the profile screen. It creates name label
        textbox to enter name and favorite color."""
        name = tk.Label(profile_window, text="Name: ", font=('calibre', 10, 'bold'))
        name.grid(row=0)

        # self.input_name = tk.Entry(profile_window, textvariable=input_name_str, font=('calibre', 10, 'bold'))
        self.input_name = tk.Entry(profile_window, font=('calibre', 10, 'bold'))
        self.input_name.grid(row=0, column=1)

        background_color = tk.Label(profile_window, text="Background Color: ", font=('calibre', 10, 'bold'))
        background_color.grid(row=1)

        self.input_bkgrnd_color = tk.Entry(profile_window, font=('calibre', 10, 'bold'))
        self.input_bkgrnd_color.grid(row=1, column=1)

    def profile_screen_part2(self, profile_window):
        """This creates the second part of the profile screen."""
        font_size = tk.Label(profile_window, text="Font size: ", font=('calibre', 10, 'bold'))
        font_size.grid(row=2)

        self.input_font_size = tk.Entry(profile_window, font=('calibre', 10, 'bold'))
        self.input_font_size.grid(row=2, column=1)

        username = tk.Label(profile_window, text="Username: ", font=('calibre', 10, 'bold'))
        username.grid(row=3)

        self.input_username = tk.Entry(profile_window, font=('calibre', 10, 'bold'))
        self.input_username.grid(row=3, column=1)

    def profile_screen_part3(self, profile_window):
        """This creates the third part of the profile screen."""
        # additional_opt_button = tk.Button(profile_window, text="Additional Options", command=self.additional_options)
        # additional_opt_button.grid(row=4)

        password = tk.Label(profile_window, text="Password: ", font=('calibre', 10, 'bold'))
        password.grid(row=4)

        self.input_password = tk.Entry(profile_window, font=('calibre', 10, 'bold'))
        self.input_password.grid(row=4, column=1)

        reset_button = tk.Button(profile_window, text="Reset", command=self.reset)
        reset_button.grid(row=5)

        create_profile_button = tk.Button(profile_window, text="Create Profile", command=self.create_profile)
        create_profile_button.grid(row=6,column=1)

    def additional_options(self):
        print("open up additional options")

    def reset(self):
        """This function will reset all the fields to blank"""
        self.input_name.delete(0,'end')
        self.input_bkgrnd_color.delete(0, 'end')
        self.input_font_size.delete(0, 'end')
        # self.input_transmission.delete(0,'end')

    def create_profile(self):
        """This will save all user inputed information so it can be saved
        to their profile. And then it starts the car shop screen."""
        extra_data = list()
        extra_data.append(self.input_name.get())
        extra_data.append(self.input_bkgrnd_color.get())
        extra_data.append(self.input_font_size.get())
        extra_data.append(self.input_username.get())
        extra_data.append(self.input_password.get())
        self.save_user_profile(extra_data.copy())

        # extra_data.append(self.input_transmission.get())
        CarShopScreen(self.root, extra_data)

    def save_user_profile(self, extras):
        file_obj = open(self.input_username.get()+".txt", "w")
        for i in range(len(extras) - 1):
            extras[i] = extras[i]+","
        file_obj.writelines(extras)
        file_obj.close()





