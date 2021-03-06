import pygame
import random
from Color import *

class Cell:
    def __init__(self, x, y, width):
        self.x = x * width
        self.y = y * width

        self.visited = False
        self.current = False

        self.walls = [True, True, True, True] # top , right , bottom , left

        # neighbors
        self.neighbors = []

        self.top = 0
        self.right = 0
        self.bottom = 0
        self.left = 0

        self.next_cell = 0

    def draw(self, screen, width):
        if self.current:
            pygame.draw.rect(screen, Color.GREEN.value,(self.x, self.y, width, width))
        elif self.visited:
            pygame.draw.rect(screen, Color.WHITE.value,(self.x, self.y, width, width))

            if self.walls[0]:
                pygame.draw.line(screen, Color.BLACK.value,(self.x, self.y), ((self.x + width), self.y), 1)
            if self.walls[1]:
                pygame.draw.line(screen, Color.BLACK.value, ((self.x + width), self.y), ((self.x + width),(self.y + width)), 1)
            if self.walls[2]:
                pygame.draw.line(screen, Color.BLACK.value, ((self.x + width), (self.y + width)), (self.x, (self.y + width)), 1)
            if self.walls[3]:
                pygame.draw.line(screen, Color.BLACK.value,(self.x,(self.y + width)),(self.x,self.y),1)

    def checkNeighbors(self, grid, width, rows, cols):
        if int(self.y / width) - 1 >= 0:
            self.top = grid[int(self.y / width) - 1][int(self.x / width)]
        if int(self.x / width) + 1 <= cols - 1:
            self.right = grid[int(self.y / width)][int(self.x / width) + 1]
        if int(self.y / width) + 1 <= rows - 1:
            self.bottom = grid[int(self.y / width) + 1][int(self.x / width)]
        if int(self.x / width) - 1 >= 0:
            self.left = grid[int(self.y / width)][int(self.x / width) - 1]

        if self.top != 0:
            if self.top.visited == False:
                self.neighbors.append(self.top)
        if self.right != 0:
            if self.right.visited == False:
                self.neighbors.append(self.right)
        if self.bottom != 0:
            if self.bottom.visited == False:
                self.neighbors.append(self.bottom)
        if self.left != 0:
            if self.left.visited == False:
                self.neighbors.append(self.left)

        if len(self.neighbors) > 0:
            self.next_cell = self.neighbors[random.randrange(0,len(self.neighbors))]
            return self.next_cell
        else:
            return False