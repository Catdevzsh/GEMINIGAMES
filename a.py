import sys
## import
import pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My First Pygame Game")

# Set up the clock
clock = pygame.time.Clock()

# Create a player object
player = pygame.sprite.Sprite()
player.image = pygame.Surface((50, 50))
player.image.fill((255, 0, 0))
player.rect = player.image.get_rect()
player.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

# Create a group to hold all the sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the game state
    all_sprites.update()

    # Draw the game state
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    # Flip the display
    pygame.display.flip()

    # Tick the clock
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
