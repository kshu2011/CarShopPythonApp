"""This PreviewCarShopScreen will setup a blank template of what the
car shop screen looks like. This allows the user to see how the app is layed out
before they commit to creating a profile."""

import tkinter as tk
import Image
import ImageTk


def setup_main_window(root):
    """Function takes the main window of tkinter as root.
    Then creates a new window by setting root as it's toplevel."""

    car_shop_window = tk.Toplevel(root)
    car_shop_window.geometry("750x750")
    car_shop_window.grid()
    return car_shop_window


def filter_title(car_shop_window):
    """Takes in a window object and creates a filter title label"""
    filter_title_label = tk.Label(car_shop_window, text="     Filters", font=('calibre', 15, 'bold'))
    filter_title_label.grid(row=0)


def generic_filter_items(car_shop_window):
    """This function creates the labels for the general filter items that will be
    available. This just shows an example of what it could look like."""

    make_label = tk.Label(car_shop_window, text="Make: ", font=('calibre', 10, 'bold'))
    make_label.grid(row=1)
    model_label = tk.Label(car_shop_window, text="Model: ", font=('calibre', 10, 'bold'))
    model_label.grid(row=2)
    year_label = tk.Label(car_shop_window, text="Year: ", font=('calibre', 10, 'bold'))
    year_label.grid(row=3)


def create_listbox_gui(car_shop_window):
    """The function will create a listbox item GUI."""
    listbox = tk.Listbox(car_shop_window, height=20, width=30, bg="grey", activestyle='dotbox', fg="yellow")
    listbox.insert(1, "*Default data*")
    listbox.insert(2, "*Default data*")
    listbox.insert(3, "*Default data*")
    listbox.grid(row=7)


def create_image_gui(car_shop_window):
    """This function sets up the image GUI."""

    path = "default_image.png"
    img_to_display = ImageTk.PhotoImage(Image.open(path).resize((350, 350)))
    panel = tk.Label(car_shop_window, image=img_to_display)
    panel.image = img_to_display
    panel.grid(row=7, column=1)


class PreviewCarShopScreen:
    """This class allows a user to preview what this is about, so it will
    show a 'example' of what things look like."""

    def __init__(self, root):
        """Initializes all the windows and GUI's by calling specific functions"""
        main_window = setup_main_window(root)
        filter_title(main_window)
        generic_filter_items(main_window)
        create_listbox_gui(main_window)
        create_image_gui(main_window)


