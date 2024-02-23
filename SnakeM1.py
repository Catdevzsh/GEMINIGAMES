import pygame
import sys
import random # imports randoms
# Initialize pygame
pygame.init()

# Set the screen size
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption("Snake")

# Set the clock
clock = pygame.time.Clock()

# Create the snake
snake = [(250, 250), (240, 250), (230, 250)]
snake_direction = pygame.K_RIGHT

# Create the food
food = (100, 100)

# Game loop
while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_direction = pygame.K_LEFT
            elif event.key == pygame.K_RIGHT:
                snake_direction = pygame.K_RIGHT
            elif event.key == pygame.K_UP:
                snake_direction = pygame.K_UP
            elif event.key == pygame.K_DOWN:
                snake_direction = pygame.K_DOWN

    # Move the snake
    if snake_direction == pygame.K_LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
    elif snake_direction == pygame.K_RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    elif snake_direction == pygame.K_UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    elif snake_direction == pygame.K_DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)

    # Check if the snake has eaten the food
    if snake[0] == food:
        # Move the food to a new location
        food = (random.randint(0, SCREEN_WIDTH - 10), random.randint(0, SCREEN_HEIGHT - 10))
        # Add a new segment to the snake
        snake.append((snake[-1][0], snake[-1][1]))

    # Check if the snake has hit itself or the wall
    for i in range(1, len(snake)):
        if snake[0] == snake[i]:
            pygame.quit()
            sys.exit()
    if snake[0][0] < 0 or snake[0][0] > SCREEN_WIDTH - 10 or snake[0][1] < 0 or snake[0][1] > SCREEN_HEIGHT - 10:
        pygame.quit()
        sys.exit()

    # Draw the snake
    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), (segment[0], segment[1], 10, 10))

    # Draw the food
    pygame.draw.rect(screen, (255, 0, 0), (food[0], food[1], 10, 10))

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(10)
