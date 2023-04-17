import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))

# Set the title of the game window
pygame.display.set_caption("Super Mario Game")

# Create Mario character
class Mario(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("mario.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 500

    def update(self):
        # Move Mario
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

# Create Mario object
mario = Mario()

# Add Mario object to sprite group
all_sprites = pygame.sprite.Group()
all_sprites.add(mario)

# Game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update sprites
    all_sprites.update()

    # Draw sprites
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
