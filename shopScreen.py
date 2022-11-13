import tkinter as tk

from advancedFilter import AdvancedFilterScreen
from moreInfoScreen import MoreInfoScreen
import ImageTk, Image
import socket
import glob
import os

# for the image part used help from stackoverflow
# https://stackoverflow.com/questions/13148975/tkinter-label-does-not-show-image
# https://www.geeksforgeeks.org/how-to-resize-image-in-python-tkinter/

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

        make_filter = tk.Label(car_shop_window, text="Make: ", font=('calibre', 10, 'bold'))
        make_filter.grid(row=1)

        self.input_make = tk.Entry(car_shop_window, font=('calibre', 10, 'bold'))
        self.input_make.grid(row=1, column=1)

        make_filter_explanation = tk.Label(car_shop_window, text="Make of car", font=('calibre', 8))
        make_filter_explanation.grid(row=2)

        model_filter = tk.Label(car_shop_window, text="Model: ", font=('calibre', 10, 'bold'))
        model_filter.grid(row=3)

        self.input_model = tk.Entry(car_shop_window, font=('calibre', 10, 'bold'))
        self.input_model.grid(row=3, column=1)

        model_filter_explanation = tk.Label(car_shop_window, text="Specific model name", font=('calibre', 8))
        model_filter_explanation.grid(row=4)

        year_filter = tk.Label(car_shop_window, text="Year: ", font=('calibre', 10, 'bold'))
        year_filter.grid(row=5)

        self.input_year = tk.Entry(car_shop_window, font=('calibre', 10, 'bold'))
        self.input_year.grid(row=5, column=1)

        year_filter_explanation = tk.Label(car_shop_window, text="Year of car", font=('calibre', 8))
        year_filter_explanation.grid(row=6)

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

        #here' let's try to create a area for image to appear

        # actual image path will be

        path = "oregon.jpg"

        # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
        img_to_display = ImageTk.PhotoImage(Image.open(path).resize((250, 250)))

        # img = Image.open(path)
        # img_resized = img.resize((50, 50), Image.ANTIALIAS)
        #
        # img_to_display = ImageTk.PhotoImage(img_resized)

        # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
        self.panel = tk.Label(car_shop_window, image=img_to_display)
        self.panel.image = img_to_display
        self.panel.grid(row=9, column=1)


    def reset(self):
        self.input_make.delete(0, 'end')
        self.input_model.delete(0, 'end')
        self.input_year.delete(0, 'end')
        self.advanced_filter_str = None
        self.unique_filter_str = None

    def search(self):




        make_of_car = self.input_make.get()
        model_of_car = self.input_model.get()
        year_of_car = self.input_year.get()

        # now display some data based on the input....
        # self.result_text.delete(1.0, 'end')
        # self.result_text.insert(tk.END, input_color_str + input_mpg_str + input_transmission_str)

        HOST = "127.0.0.1"  # The server's hostname or IP address
        PORT = 65432  # The port used by the server

        #   Send the car information via socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print("Sending Request... ")
            s.sendall(str.encode(year_of_car+make_of_car+model_of_car))
            data = s.recv(1024).decode()


        # now get the latest file
        all_files = glob.glob("//users//kshu//desktop//other_desktop_stuff//cse//osu_post_bacc//cs_361//MicroServiceGetImage_partner_built//imageDownloads//*")  # * means all if need specific format then *.csv
        newest_file_path = max(all_files, key=os.path.getctime)

        #now update the image being displayed
        img_to_display = ImageTk.PhotoImage(Image.open(newest_file_path).resize((250, 250)))
        self.panel.configure(image=img_to_display)
        self.panel.image = img_to_display


        self.listbox.delete(0, 'end')

        self.listbox.insert(1, make_of_car)
        self.listbox.insert(2, model_of_car)
        self.listbox.insert(3, year_of_car)
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






