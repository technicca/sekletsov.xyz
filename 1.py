import pygame
import numpy as np

# Initialize pygame and create window
pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode(size)

# Create a numpy array to store the game state
game_state = np.random.randint(2, size=(width//10, height//10))

def update_game_state(game_state):
    # Create a copy of the game state to update
    new_game_state = np.copy(game_state)

    # Iterate over each cell in the game state
    for i in range(game_state.shape[0]):
        for j in range(game_state.shape[1]):
            # Count the number of live neighbors for the current cell
            live_neighbors = count_live_neighbors(game_state, i, j)

            # Apply the rules of Conway's Game of Life
            if game_state[i, j] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    new_game_state[i, j] = 0
            else:
                if live_neighbors == 3:
                    new_game_state[i, j] = 1

    return new_game_state

def count_live_neighbors(game_state, i, j):
    count = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            if i+x < 0 or i+x >= game_state.shape[0] or j+y < 0 or j+y >= game_state.shape[1]:
                continue
            if game_state[i+x, j+y] == 1:
                count += 1
    return count

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the current game state
    for i in range(game_state.shape[0]):
        for j in range(game_state.shape[1]):
            if game_state[i, j] == 1:
                pygame.draw.rect(screen, (199, 238, 199), (i*10, j*10, 10, 10))

    # Update the game state
    game_state = update_game_state(game_state)

    # Update the display
    pygame.display.flip()
    pygame.time.wait(40)

# Close pygame when the game loop exits
pygame.quit()
