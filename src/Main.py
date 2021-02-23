import random
import pygame
from Color import *
from Player import *
from Cell import *

pygame.init()

windowSize = (800, 700)
screen = pygame.display.set_mode(windowSize)
pygame.display.set_caption("Random Maze")

done = False

clock = pygame.time.Clock()

width = 25 # largura de cada cell
cols = int(windowSize[0] / width)
rows = int(windowSize[1] / width)

stack = []

pos = (0,0)

def load_background():
    background = pygame.Surface.fill(screen, Color.BLACK.value)
    return background

def load_player(background):
    player = pygame.Surface((10, 10))
    player.fill(Color.BLUE.value)

    posx = random.randint(0, rows-1) * width + width//2
    posy = random.randint(0, cols-1) * width + width//2

    return Player(player, (posx, posy), background)

def removeWalls(current_cell,next_cell):
    x = int(current_cell.x / width) - int(next_cell.x / width)
    y = int(current_cell.y / width) - int(next_cell.y / width)
    if x == -1: # right of current
        current_cell.walls[1] = False
        next_cell.walls[3] = False
    elif x == 1: # left of current
        current_cell.walls[3] = False
        next_cell.walls[1] = False
    elif y == -1: # bottom of current
        current_cell.walls[2] = False
        next_cell.walls[0] = False
    elif y == 1: # top of current
        current_cell.walls[0] = False
        next_cell.walls[2] = False

grid = []

for y in range(rows):
    grid.append([])
    for x in range(cols):
        grid[y].append(Cell(x, y, width))

current_cell = grid[0][0]
next_cell = 0

def main():
    global current_cell

    player = None
    initialized = False
    frame = 0
    clock = pygame.time.Clock()
    sprites = pygame.sprite.Group()

    if not initialized:
        background = load_background()
        background = None
        player = load_player(background)
        sprites.add(player)
        initialized = True

    play = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for y in range(rows):
            for x in range(cols):
                grid[y][x].draw(screen, width)

        if play == True:
            pygame.init()

            while not done:
                events = pygame.event.get()

                for e in events:
                    if e.type == pygame.QUIT:
                        return

                player_x = player.pos[0]
                player_y = player.pos[1]
                pygame.draw.rect(screen, Color.LIGHTSKYBLUE.value, player.rect)

                sprites.update(grid, None, frame, width, cols, rows)

                sprites.draw(screen)
                pygame.display.flip()
                frame = clock.tick(60)
        else:
            current_cell.visited = True
            current_cell.current = True

            next_cell = current_cell.checkNeighbors(grid, width, rows, cols)
            if next_cell != False:
                current_cell.neighbors = []
                stack.append(current_cell)
                removeWalls(current_cell,next_cell)
                current_cell.current = False
                current_cell = next_cell
            elif len(stack) > 0:
                current_cell.current = False
                current_cell = stack.pop()
            else:
                play = True
        pygame.display.flip()

if __name__ == "__main__":
    main()
    pygame.quit()