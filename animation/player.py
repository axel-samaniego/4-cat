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
    screen = pygame.display.set_mode((128, 64))  # Adjust to your display resolution
    # pygame.display.set_caption("Cat Animation")

    # Load images
    images = [pygame.image.load(img) for img in sorted(glob(cwd + "/animation/sitting_tail/" + "/*.bmp"))]
    print(f"loaded images: {images}")
    
    # Animation loop
    running = True
    frame = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear the screen with a background color
        screen.fill((255, 255, 255))  # Black background
        # Display frame
        screen.blit(images[frame], (64 - 16,32))
        pygame.display.flip()

        # Update to the next frame
        frame = (frame + 1) % len(images)
        time.sleep(0.2)  # Adjust for animation speed

    pygame.quit()

if __name__ == "__main__":
    main()