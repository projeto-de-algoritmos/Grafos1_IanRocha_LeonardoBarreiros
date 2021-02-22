from random import shuffle, randrange

class Maze:
    def __init__(self):
       self.col = 15
       self.row = 15
       self.maze = [
                    1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                    1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1,
                    1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1,
                    1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1,
                    1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1,
                    1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1,
                    1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1,
                    1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1,
                    1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1,
                    1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1,
                    1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1,
                    1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1,
                    1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1,
                    1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1,
                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1
                ]

    def draw(self,display, blocks, width, height):
       block_x = 0
       block_y = 0
       for i in range(0, self.col * self.row):
           if self.maze[ block_x + (block_y * self.col) ] == 1:
               display.blit(blocks,( block_x * width , block_y * height))

           block_x = block_x + 1
           if block_x > self.col - 1:
               block_x = 0
               block_y = block_y + 1