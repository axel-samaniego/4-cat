import time
from glob import glob
import os
from PIL import Image
import adafruit_ssd1306
import busio
import board
from digitalio import DigitalInOut, Direction, Pull
import numpy as np

def main():

    i2c = busio.I2C(board.SCL, board.SDA)
    disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

    disp.fill(0)
    disp.show()
    now = time.time() 
    face_folder_names = ['blink',
                        'nose',
                        'static',
                        'whisker']
    img_paths = {}
    total_loaded = 0
    cwd = os.getcwd()
    for folder in face_folder_names:
        images = glob(cwd + f"/animation/face/{folder}/*.bmp")
        images.sort()
        img_paths[f"face/{folder}"] = [Image.open(img_path).convert("1") for img_path in images if int(img_path.split("tile")[-1].split('.')[0])%2==0]
        total_loaded += len(images)
    
    main_animation = "face/static"
    current_animation = main_animation
    current_frame = 0
    # Time between frames
    face_delay = 0.001  
    sit_delay = 0.025
    interval = 5
    next_check = time.time() + interval

    while True:
        start = time.time()
        if (main_animation == "face/static") and time.time()>=next_check:
            rand_num = np.random.randint(0, 8)
            if rand_num < 4:
                current_animation = f"face/{face_folder_names[rand_num]}"
                current_frame = 0
            next_check = time.time() + interval
        disp.fill(0)
        disp.image(images[current_frame])
        disp.show()
        if (current_animation!=main_animation) and (current_frame >= len(images) - 1):
            current_animation = main_animation
            current_frame = 0
        else:
            current_frame = (current_frame + 1) % len(images)  # Loop frames
        end = time.time()
        print(f"loop time taken: {end - start}")
        if now - start > 5:
            break


if __name__ == "__main__":
    main()
