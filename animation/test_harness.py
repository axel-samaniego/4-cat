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

    while True:
        start = time.time()
        num = np.random.randint(0,3)
        if num==1:
            print("Check")
        else:
            print(0)
        end = time.time()
        print(f"loop time taken: {end - start}")
        if now - start > 5:
            break


if __name__ == "__main__":
    main()
