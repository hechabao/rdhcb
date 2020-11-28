import os
import time

def Get_Screenshot(driver,filename):
    path = os.path.dirname(__file__)
    time_stamp1 = time.strftime('%Y%m%d')
    time_stamp2 = time.strftime('%H-%M-%S')
    image_path = path.replace('func','image')
    filepath = image_path + '/' + time_stamp1
    if not os.path.exists(filepath):
        os.mkdir(filepath)
    image_full_name = filepath + '/' + filename + time_stamp2 + '.png'
    driver.get_screenshot_as_file(image_full_name)


