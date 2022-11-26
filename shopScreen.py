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

from advancedFilter import AdvancedFilterScreen
from moreInfoScreen import MoreInfoScreen

# CONSTANTS
# Path were images are downloaded
# Host and Port address to communicate with server
IMAGE_PATH = "//users//kshu//desktop//other_desktop_stuff//cse//osu_post_bacc//cs_361//MicroServiceGetImage_partner_built//imageDownloads//*"
HOST = "127.0.0.1"
PORT = 65432


def model_label(root):
    """This creates the model label and explanation."""

    model_filter = tk.Label(root, text="Model: ", font=('calibre', 10, 'bold'))
    model_filter.grid(row=3)

    model_filter_explanation = tk.Label(root, text="Specific model name", font=('calibre', 8))
    model_filter_explanation.grid(row=4)


def year_label(root):
    """This creates the year label and explanation."""

    year_filter = tk.Label(root, text="Year: ", font=('calibre', 10, 'bold'))
    year_filter.grid(row=5)

    year_filter_explanation = tk.Label(root, text="Year of car", font=('calibre', 8))
    year_filter_explanation.grid(row=6)


def setup_root(root, extra_background):
    """Sets up the window for this class"""
    main_window = tk.Toplevel(root)
    main_window.geometry("750x750")
    main_window.configure(background=extra_background)
    main_window.grid()
    return main_window


def title_make_exp_labels(root, extras_font):
    """This creates the title, make and explanation labels."""

    filter_title = tk.Label(root, text="     Filters", font=('calibre', extras_font + 5, 'bold'))
    filter_title.grid(row=0)

    make_filter = tk.Label(root, text="Make: ", font=('calibre', extras_font, 'bold'))
    make_filter.grid(row=1)

    make_filter_explanation = tk.Label(root, text="Make of car", font=('calibre', extras_font - 2))
    make_filter_explanation.grid(row=2)


def setup_label_gui(car_shop_window, extras):
    """This function will call helper methods to set up labels."""

    title_make_exp_labels(car_shop_window, extras)
    model_label(car_shop_window)
    year_label(car_shop_window)


def check_database(year, make, model):
    """Checks to see if the 'database' has specified data in it, if it does
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


class CarShopScreen:
    """
    This class creates the Car Shop Screen with all the necassary GUI's.
    """

    def __init__(self, root, extra_data=None):
        """Initializes all the required variables and calls some helper methods"""
        self._input_year, self._input_model, self._input_make, self._listbox = None, None, None, None
        self._root = root
        self._unique_filter_str = ""
        car_shop_window = setup_root(root, extra_data[1])
        self.__setup_filter(car_shop_window, int(extra_data[2]))

    def __setup_filter(self, car_shop_window, extras):
        """this function will setup all the filter GUI's
        by calling upon other functions."""

        setup_label_gui(car_shop_window, extras)
        self.__setup_textbox_btn_list(car_shop_window, extras)

    def __setup_textbox_btn_list(self, car_shop_window, extras):
        """This function will call helper method to set up the textbox, button
        and listbox."""

        self.__make_model_year_textbox(car_shop_window, extras)
        self.__setup_button(car_shop_window, extras)
        self.__create_list_display(car_shop_window)

    def __make_model_year_textbox(self, root, extras_font):
        """This function creates the text boxes for the window."""

        self._input_make = tk.Entry(root, font=('calibre', extras_font, 'bold'))
        self._input_make.grid(row=1, column=1)

        self._input_model = tk.Entry(root, font=('calibre', extras_font, 'bold'))
        self._input_model.grid(row=3, column=1)

        self._input_year = tk.Entry(root, font=('calibre', extras_font, 'bold'))
        self._input_year.grid(row=5, column=1)

    def __setup_button(self, root, extras_font):
        """This function creates all the necessary buttons."""

        reset_button = tk.Button(root, text="Reset Filter", font=('calibre', extras_font, 'bold'),
                                 command=self.reset)
        reset_button.grid(row=0, column=1)
        self.__setup_adv_search_btn(root, extras_font)

    def __setup_adv_search_btn(self, root, extras_font):
        """This function will set up the advanced filter button and search button."""

        advanced_filter = tk.Button(root, text="Advanced", font=('calibre', extras_font, 'bold'),
                                    command=self.__adv_filter_set)
        advanced_filter.grid(row=7)

        search_button = tk.Button(root, text="Search", font=('calibre', extras_font, 'bold'), command=self.search)
        search_button.grid(row=8)

    def __create_list_display(self, root):
        """This function will create the listbox that will display the car information. It
        also sets the image label so image can be displayed properly."""

        self._listbox = tk.Listbox(root, height=20, width=30, bg="grey", activestyle='dotbox', fg="yellow")
        self._listbox.grid(row=9)

        more_info_button = tk.Button(root, text='More Info.', command=self.__more_info_screen)
        more_info_button.grid(row=10, column=1)

        self.__image_display(root)

    def __image_display(self, root):
        """ Creates a Tkinter-compatible photo image, which can be used
         everywhere Tkinter expects an image object. Initially will set it to default_image.png """

        path = "default_image.png"
        img_to_display = ImageTk.PhotoImage(Image.open(path).resize((350, 350)))
        self.panel = tk.Label(root, image=img_to_display)
        self.panel.image = img_to_display
        self.panel.grid(row=9, column=1)

    def reset(self):
        """This function will reset all the fields to blank"""

        self._input_make.delete(0, 'end')
        self._input_model.delete(0, 'end')
        self._input_year.delete(0, 'end')
        self._unique_filter_str = ""

    def search(self):
        """This function will take the users input and
        send it to the server to search for image of vehicle that the user wants"""
        make_of_car = self._input_make.get()
        model_of_car = self._input_model.get()
        year_of_car = self._input_year.get()
        self.__search_helper(year_of_car, make_of_car, model_of_car)

    def __search_helper(self, year_of_car, make_of_car, model_of_car):
        """this function is the search helper, it will call helper functions to make
        the correct calls."""

        search_result = check_database(year_of_car, make_of_car, model_of_car)  # make sure it's in database
        if search_result:
            self.update_results_to_display(year_of_car, make_of_car, model_of_car, search_result)
        else:
            self.__image_display_default()

    def __image_display_default(self):
        """this will display a default empty image."""

        img_to_display = ImageTk.PhotoImage(Image.open('default_image.png').resize((350, 350)))
        self.panel.configure(image=img_to_display)
        self.panel.image = img_to_display
        self._listbox.delete(0, 'end')

    def __adv_filter_set(self):
        """This function calls the class AdvancedFilterScreen to create
        a new window"""

        AdvancedFilterScreen(self._root, self)

    def set_advanced(self, unique_filter):
        """This function will save the advanced filter choices chosen by
        the user."""

        self._unique_filter_str = unique_filter

    def __more_info_screen(self):
        """This function will call the class MoreInfoScreen to
        create a new window to display the extra information."""

        MoreInfoScreen(self._root)

    def __socket_connection(self, year_of_car, make_of_car, model_of_car):
        """This function will use socket to connect to server by HOST, and PORT
        in order to communicate with server to download image."""

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print("Sending Request... ")
            s.sendall(str.encode(self._unique_filter_str + year_of_car + make_of_car + model_of_car))
        time.sleep(2)

    def __get_newest_file(self):
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

        self.__add_items_listbox(year_of_car, make_of_car, model_of_car)
        self.__add_to_listbox(search_result)
        self.__socket_connection(year_of_car, make_of_car, model_of_car)
        self.__get_newest_file()

    def __add_to_listbox(self, search_result):
        """Function will take in a string and split up the string
        and add it's information to tkinter's listbox so it can be displayed"""

        search_data = search_result.split(",")
        for index in range(3, len(search_data)):
            self._listbox.insert(index + 1, search_data[index])

    def __add_items_listbox(self, year_of_car, make_of_car, model_of_car):
        """This function will help add items to listbox display."""

        self._listbox.delete(0, 'end')
        self._listbox.insert(1, make_of_car)
        self._listbox.insert(2, model_of_car)
        self._listbox.insert(3, year_of_car)