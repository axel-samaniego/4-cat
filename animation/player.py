import pygame
import time
from glob import glob
import os

def main():

    cwd = os.getcwd()
    ani_folders = glob(cwd + "/animation/*")
    print(f"ani_folders {ani_folders}")
    pygame.init()

    # Set up the screen
    screen = pygame.display.set_mode((36, 36))  # Adjust to your display resolution
    # pygame.display.set_caption("Cat Animation")

    # Load images
    images = [pygame.image.load(img) for img in sorted(glob(ani_folders[0] + "/*.png"))]
    print(f"loaded images: {images}")
    
    # Animation loop
    running = True
    frame = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear the screen with a background color
        screen.fill((0, 0, 0))  # Black background
        # Display frame
        screen.blit(images[frame], (0,0))
        pygame.display.flip()

        # Update to the next frame
        frame = (frame + 1) % len(images)
        time.sleep(0.2)  # Adjust for animation speed

    pygame.quit()

if __name__ == "__main__":
    main()