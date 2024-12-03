import time
from glob import glob
import os
from PIL import Image
import adafruit_ssd1306
import busio
import board
from digitalio import DigitalInOut, Direction, Pull
import numpy as np
from controller import Controller



def display_frame(frame_image, disp):
    disp.fill(0)
    disp.image(frame_image)
    disp.show()

    

def main():
      
    i2c = busio.I2C(board.SCL, board.SDA)
    disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

    # Input pins:
    # Input pins:
    buttons = {
        "A": DigitalInOut(board.D5),
        "B": DigitalInOut(board.D6),
        "L": DigitalInOut(board.D27),
        "R": DigitalInOut(board.D23),
        "U": DigitalInOut(board.D17),
        "D": DigitalInOut(board.D22),
        "C": DigitalInOut(board.D4),
    }

    # Configure buttons as inputs with pull-ups
    for button in buttons.values():
        button.direction = Direction.INPUT
        button.pull = Pull.UP 
    
    disp.fill(0)
    disp.show()
    cwd = os.getcwd()
   

    # Set up the screen
    # pygame.display.set_caption("Cat Animation")

    # Load images
    # images = [pygame.image.load(img) for img in sorted(glob(cwd + "/animation/sitting_tail/" + "/*.bmp"))]
    sitting_folder_names = ['running',
                            'attack',
                            'sleeping',
                            'sitting_lick',
                            'scared',
                            'paw_tap',
                            'sitting_tail']
    face_folder_names = ['blink',
                        'nose',
                        'static',
                        'whisker']
    img_paths = {}
    total_loaded = 0
    for folder in sitting_folder_names:
        images = glob(cwd + f"/animation/{folder}/*.bmp")
        images.sort()
        img_paths[folder] = [Image.open(img_path).convert("1") for img_path in images]
        total_loaded += len(images)

    for folder in face_folder_names:
        images = glob(cwd + f"/animation/face/{folder}/*.bmp")
        images.sort()
        img_paths[f"face/{folder}"] = [Image.open(img_path).convert("1") for img_path in images]
        total_loaded += len(images)
   

    print(f"loaded images: {total_loaded}")
    print(f"image keys: {img_paths.keys()}")
    
    # Initialize state variables
    main_animation = "face/static"
    current_animation = main_animation
    current_frame = 0
    frame_delay = 0.075  # Time between frames
    interval = 10
    next_check = time.time() + interval
    
    while True:    
        # If the button is pressed down (transition from high to low)
        # Check buttons and switch animation
        if buttons["C"].value:  
            if (main_animation == "face/static") and time.time()>=next_check:
                rand_num = np.random.randint(0, 10)
                if rand_num < 4:
                    current_animation = face_folder_names[rand_num]
                    current_frame = 0
                next_check = time.time() + interval
            pass
        else:  # Button "C" pressed
            if main_animation != "sitting_tail":
                main_animation = "sitting_tail"
                current_frame = 0  # Reset frame index
        
        if main_animation == "sitting_tail":
            if buttons["A"].value:
                pass
            else:
                if current_animation!="scared":
                    current_animation = "scared"
                    current_frame = 0

        # Get the current animation frames
        images = img_paths[current_animation]

    
        display_frame(images[current_frame], disp)
        if (current_animation!=main_animation) and (current_frame >= len(images) - 1):
            current_animation = main_animation
            current_frame = 0
        else:
            current_frame = (current_frame + 1) % len(images)  # Loop frames
        time.sleep(frame_delay)
        if not buttons["A"].value and not buttons["B"].value and not buttons["C"].value:
            break
    
    disp.poweroff()




if __name__ == "__main__":
    main()