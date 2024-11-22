import pygame
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

def display_images(images, disp):
    frame = 0
    # Clear the display
    disp.fill(0)
    
    # Display the current frame
    frame_image = images[frame]
    disp.image(frame_image)
    disp.show()

    # Update to the next frame
    frame = (frame + 1) % len(images)
    time.sleep(0.1)  # Adjust for animation speed



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
    ani_folders = glob(cwd + "/animation/*")
    print(f"ani_folders {ani_folders}")
    pygame.init()

    # Set up the screen
    # pygame.display.set_caption("Cat Animation")

    # Load images
    # images = [pygame.image.load(img) for img in sorted(glob(cwd + "/animation/sitting_tail/" + "/*.bmp"))]
    folder_names = ['running',
                    'attack',
                    'sleeping',
                    'sitting_lick',
                    'scared',
                    'paw_tap',
                    'sitting_tail']
    img_paths = {}
    total_loaded = 0
    for folder in folder_names:
        images = glob(cwd + f"/animation/{folder}/*.bmp")
        images.sort()
        img_paths[folder] = [Image.open(img_path).convert("1") for img_path in images]
        total_loaded += len(images)
   

    print(f"loaded images: {total_loaded}")
    
    # Animation loop
    running = True

    try:
        while running:    
            # If the button is pressed down (transition from high to low)
            if buttons["A"].value:
                display_images(img_paths['sitting_tail'], disp)
            else:
                display_images(img_paths['scared'], disp)
                    
    except KeyboardInterrupt:
        print("exiting")
        disp.poweroff()



if __name__ == "__main__":
    main()