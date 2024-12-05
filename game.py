import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WINDOW_SIZE_X = 500 # Size of the square window
WINDOW_SIZE_Y = 500 # Size of the square window
win = pygame.display.set_mode((WINDOW_SIZE_X, WINDOW_SIZE_Y))
pygame.display.set_caption("Find Luigi!")

# Set up colors
BLACK = (0, 0, 0)

# Square properties
square_size = 50

class Character:
    def __init__(self, image_path):
        # Load the image and scale it to the desired size
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (square_size, square_size))

        # Initialize position randomly within bounds
        self.x = random.randint(0, WINDOW_SIZE_X - square_size)
        self.y = random.randint(0, WINDOW_SIZE_Y - square_size)

        # Initialize random velocities for movement (range: -5 to 5, excluding 0)
        self.velocity_x = random.choice([-1, 1]) * random.randint(2, 5)
        self.velocity_y = random.choice([-1, 1]) * random.randint(2, 5)

    def update_position(self):
        # Update character position
        self.x += self.velocity_x
        self.y += self.velocity_y

        # Bounce logic: reverse direction if hitting a wall
        if self.x <= 0 or self.x + square_size >= WINDOW_SIZE_X:
            self.velocity_x *= -1

        if self.y <= 0 or self.y + square_size >= WINDOW_SIZE_Y:
            self.velocity_y *= -1

    def draw_character(self):
        # Draw the image on the screen at its current position
        win.blit(self.image, (self.x, self.y))

# Game loop control
run = True
clock = pygame.time.Clock()

obj_count = 100

luigi_character_image_path = "sprites/luigi.png"  # Path for Luigi's image
non_luigi_character_image_paths = ["sprites/mario.png", "sprites/wmario.png", "sprites/yoshi.png"]  # Paths for Mario and Wario images

# Create multiple characters and store them in a list
characters = []


# Add obj_count number of Mario and Wario characters
for _ in range(obj_count//2):
    # Randomly choose between Mario and Wario for each character
    random_image_path = random.choice(non_luigi_character_image_paths)
    characters.append(Character(random_image_path))

# Add one Luigi character
characters.append(Character(luigi_character_image_path))

# Add obj_count number of Mario and Wario characters
for _ in range(obj_count//2):
    # Randomly choose between Mario and Wario for each character
    random_image_path = random.choice(non_luigi_character_image_paths)
    characters.append(Character(random_image_path))


while run:
    clock.tick(30)  # Limit to 60 frames per second
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Update positions and draw characters
    win.fill(BLACK)  # Clear screen with black background

    for character in characters:
        character.update_position()
        character.draw_character()

    pygame.display.update()  # Update the display

# Quit Pygame
pygame.quit()