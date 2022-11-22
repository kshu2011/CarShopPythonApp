# This is the main car shopping screen. Where the user can enter the car
# and it will display information and picture of the car.
# Source used to help figure out the image:
# https://stackoverflow.com/questions/13148975/tkinter-label-does-not-show-image
# https://www.geeksforgeeks.org/how-to-resize-image-in-python-tkinter/

import glob
import os
import socket
import time
import tkinter as tk

import Image
import ImageTk
# import ImageFile
# ImageTk.LOAD_TRUNCATED_IMAGES = True

from advancedFilter import AdvancedFilterScreen
from moreInfoScreen import MoreInfoScreen

# CONSTANTS
# Path were images are downloaded
# Host and Port address to communicate with server
IMAGE_PATH = "//users//kshu//desktop//other_desktop_stuff//cse//osu_post_bacc//cs_361//MicroServiceGetImage_partner_built//imageDownloads//*"
HOST = "127.0.0.1"
PORT = 65432


class CarShopScreen:
    """
    This class creates the Car Shop Screen with all the necassary GUI's.
    """

    def __init__(self, root, extra_data=None):
        """Initializes all variables"""
        self.background_color = extra_data[1]
        self.font_size = int(extra_data[2])
        self.root = root
        self.advanced_filter_str = None
        self.unique_filter_str = None
        car_shop_window = self.setup_root(root)
        self.setup_filter(car_shop_window)

    def setup_filter(self, car_shop_window):
        """this function will setup all the filter GUI's
        by calling upon other functions."""
        self.create_filter_part1(car_shop_window)
        self.create_filter_part2(car_shop_window)
        self.create_filter_part3(car_shop_window)
        self.create_list_display(car_shop_window)

    def setup_root(self, root):
        """Sets up the window for this class"""
        main_window = tk.Toplevel(root)
        main_window.geometry("750x750")
        main_window.configure(background=self.background_color)
        main_window.grid()
        return main_window

    def create_filter_part1(self, root):
        """This creates the first part of the filter section in car shop window.
        It will create the title, reset button, car make label and text input and
        the explanation."""
        filter_title = tk.Label(root, text="     Filters", font=('calibre', self.font_size+5, 'bold'))
        filter_title.grid(row=0)

        reset_button = tk.Button(root, text="Reset Filter", font=('calibre', self.font_size, 'bold'), command=self.reset)
        reset_button.grid(row=0, column=1)

        make_filter = tk.Label(root, text="Make: ", font=('calibre', self.font_size, 'bold'))
        make_filter.grid(row=1)

        self.input_make = tk.Entry(root, font=('calibre', self.font_size, 'bold'))
        self.input_make.grid(row=1, column=1)

        make_filter_explanation = tk.Label(root, text="Make of car", font=('calibre', self.font_size-2))
        make_filter_explanation.grid(row=2)

    def create_filter_part2(self, root):
        """This function creates the second part of filter section for car shop window.
        It creates the model lable and textbox to input the model and a text to explain
        what it means."""
        model_filter = tk.Label(root, text="Model: ", font=('calibre', 10, 'bold'))
        model_filter.grid(row=3)

        self.input_model = tk.Entry(root, font=('calibre', 10, 'bold'))
        self.input_model.grid(row=3, column=1)

        model_filter_explanation = tk.Label(root, text="Specific model name", font=('calibre', 8))
        model_filter_explanation.grid(row=4)

    def create_filter_part3(self, root):
        """This function creates the third part of the filter section. It creates
        the year label and input textbox for the year and an explanation as to what
        this means. Also creates the advanced filter and search buttons."""
        year_filter = tk.Label(root, text="Year: ", font=('calibre', 10, 'bold'))
        year_filter.grid(row=5)

        self.input_year = tk.Entry(root, font=('calibre', 10, 'bold'))
        self.input_year.grid(row=5, column=1)

        year_filter_explanation = tk.Label(root, text="Year of car", font=('calibre', 8))
        year_filter_explanation.grid(row=6)

        advanced_filter = tk.Button(root, text="Advanced", font=('calibre', 10, 'bold'), command=self.adv_filter_set)
        advanced_filter.grid(row=7)

        search_button = tk.Button(root, text="Search", font=('calibre', 10, 'bold'), command=self.search)
        search_button.grid(row=8)

    def create_list_display(self, root):
        """This function will create the listbox that will display the car information. It
        also sets the image label so image can be displayed properly."""
        self.listbox = tk.Listbox(root, height=20, width=30, bg="grey", activestyle='dotbox', fg="yellow")
        self.listbox.grid(row=9)

        more_info_button = tk.Button(root, text='More Info.', command=self.more_info_screen)
        more_info_button.grid(row=10, column=1)

        # Creates a Tkinter-compatible photo image, which can be used
        # everywhere Tkinter expects an image object. Initially will set it to default_image.png
        path = "default_image.png"
        img_to_display = ImageTk.PhotoImage(Image.open(path).resize((350, 350)))
        self.panel = tk.Label(root, image=img_to_display)
        self.panel.image = img_to_display
        self.panel.grid(row=9, column=1)

    def reset(self):
        """This function will reset all the fields to blank"""
        self.input_make.delete(0, 'end')
        self.input_model.delete(0, 'end')
        self.input_year.delete(0, 'end')
        self.advanced_filter_str = None
        self.unique_filter_str = None

    def search(self):
        """This function will take the users input and
        send it to the server to search for image of vehicle that the user wants"""
        make_of_car = self.input_make.get()
        model_of_car = self.input_model.get()
        year_of_car = self.input_year.get()

        search_result = self.check_database(year_of_car, make_of_car, model_of_car)
        if search_result:
            self.update_results_to_display(year_of_car, make_of_car, model_of_car, search_result)
        else:
            img_to_display = ImageTk.PhotoImage(Image.open('default_image.png').resize((350, 350)))
            self.panel.configure(image=img_to_display)
            self.panel.image = img_to_display
            self.listbox.delete(0, 'end')

    def adv_filter_set(self):
        """This function calls the class AdvancedFilterScreen to create
        a new window"""
        AdvancedFilterScreen(self.root, self)

    def set_advanced(self, input_filter, unique_filter):
        """This function will save the advanced filter choices chosen by
        the user."""
        self.advanced_filter_str = input_filter
        self.unique_filter_str = unique_filter

    def more_info_screen(self):
        """This function will call the class MoreInfoScreen to
        create a new window to display the extra information."""
        MoreInfoScreen(self.root)

    def check_database(self, year, make, model):
        """Checks to see if the 'database' has data in it, if it does
        it will read it in and return it. """

        while True:
            file = open("car_database.txt", "r")
            lines = file.readlines()
            file.close()
            data = None
            for line in lines:
                if year in line and make in line and model in line:
                    data = line
            return data

    def socket_connection(self, year_of_car, make_of_car, model_of_car):
        """This function will use socket to connect to server by HOST, and PORT
        in order to communicate with server to download image."""

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print("Sending Request... ")
            s.sendall(str.encode(year_of_car + make_of_car + model_of_car))
        time.sleep(2)

    def get_newest_file(self):
        """this function will grab the newest image from IMAGE_PATH and
        update the image being displayed."""
        all_files = glob.glob(IMAGE_PATH)
        newest_file_path = max(all_files, key=os.path.getctime)

        # now update the image being displayed
        img_to_display = ImageTk.PhotoImage(Image.open(newest_file_path).resize((250, 250)))
        self.panel.configure(image=img_to_display)
        self.panel.image = img_to_display

    def update_results_to_display(self, year_of_car, make_of_car, model_of_car, search_result):
        """This function will take the information user has inputed and update the GUI to display the
        appropriate information based on users input."""
        self.listbox.delete(0, 'end')
        self.listbox.insert(1, make_of_car)
        self.listbox.insert(2, model_of_car)
        self.listbox.insert(3, year_of_car)

        search_data = search_result.split(",")
        for index in range(3, len(search_data)):
            self.listbox.insert(index + 1, search_data[index])

        self.socket_connection(year_of_car, make_of_car, model_of_car)
        self.get_newest_file()
