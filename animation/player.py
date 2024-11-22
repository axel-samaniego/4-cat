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
    
    sitting = [Image.open(img_path).convert("1") for img_path in glob(cwd + "/animation/sitting_tail/" + "/*.bmp")]
    sitting.sort()
    lick = [Image.open(img_path).convert("1") for img_path in glob(cwd + "/animation/sitting_lic/" + "/*.bmp")]
    lick.sort()

    print(f"loaded images: {len(sitting + lick)}")
    
    # Animation loop
    running = True
    previous_states = {name: button.value for name, button in buttons.items()}

    try:
        while running:    
            # If the button is pressed down (transition from high to low)
            if not buttons["A"].value:
                display_images(lick, disp)
            else:
                display_images(sitting, disp)
                    
            time.sleep(0.1)  # Small delay to avoid flooding the console
    except KeyboardInterrupt:
        print("exiting")
        disp.poweroff()



if __name__ == "__main__":
    main()