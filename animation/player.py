import pygame
import time
from glob import glob
import os
from PIL import Image
import adafruit_ssd1306
import busio
import board
import numpy as np




def main():

    i2c = busio.I2C(board.SCL, board.SDA)
    disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
    disp.fill(0)
    disp.show()
    cwd = os.getcwd()
    ani_folders = glob(cwd + "/animation/*")
    print(f"ani_folders {ani_folders}")
    pygame.init()

    # Set up the screen
    screen = pygame.display.set_mode((128, 64))  # Adjust to your display resolution
    # pygame.display.set_caption("Cat Animation")

    # Load images
    # images = [pygame.image.load(img) for img in sorted(glob(cwd + "/animation/sitting_tail/" + "/*.bmp"))]
    
    images = [Image.open(img_path).convert("1") for img_path in glob(cwd + "/animation/sitting_tail/" + "/*.bmp")]

    print(f"loaded images: {len(images)}")
    
    # Animation loop
    running = True
    frame = 0
    while running:
        # Clear the display
        disp.fill(0)
        
        # Display the current frame
        frame_image = images[frame]
        disp.image(frame_image)
        disp.show()

        # Update to the next frame
        frame = (frame + 1) % len(images)
        time.sleep(0.2)  # Adjust for animation speed

    pygame.quit()

if __name__ == "__main__":
    main()