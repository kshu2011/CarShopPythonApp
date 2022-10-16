import os
import time
import json


def get_image_path():
    """This function will read 'image-services.txt' and if it contains
    a integer then it will erase it and write in a image path
    based on that integer it found initially."""
    while True:
        time.sleep(1)
        file = open("car_data.txt", "r")
        lines = file.readlines()
        file.close()
        if len(lines) > 0 and lines[0].isdigit():
            path = "//Users//kshu//Desktop//Other_desktop_stuff//CSE//OSU_post_bacc//CS_361//assignment2//picture//"
            num_of_images = len(os.listdir(path))
            information = {"path": path, "number_of_images": num_of_images, "random_image": int(lines[0])}
            file = open("car_data.txt", "w")
            #file.write(str(information))
            json.dump(information, file)
            file.close()


if __name__ == '__main__':
    get_image_path()

