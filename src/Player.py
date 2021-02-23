import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, image, pos, background):
        super().__init__()
        self.image = image
        self.pos = pygame.Vector2(pos)
        self.rect = self.image.get_rect(center=self.pos)
        self.background = background

    def update(self, grid, events, dt, width, cols, rows):
        keyEvent = pygame.key.get_pressed()
        move = pygame.Vector2((0, 0))

        # calculate maximum movement and current cell position
        testdist = dt // 5 + 2
        cellx = self.rect.centerx // width
        celly = self.rect.centery // width
        minx = self.rect.left // width
        maxx = self.rect.right // width
        miny = self.rect.top // width
        maxy = self.rect.bottom // width

        # test move up
        if minx == maxx and keyEvent[pygame.K_UP]:
            nexty = (self.rect.top-testdist) // width
            if celly == nexty or (nexty >= 0 and not grid[celly][cellx].walls[0]):
                move += (0, -1)

        # test move right
        elif miny == maxy and keyEvent[pygame.K_RIGHT]:
            nextx = (self.rect.right+testdist) // width
            if cellx == nextx or (nextx < cols and not grid[celly][cellx].walls[1]):
                move += (1, 0)

        # test move down
        elif minx == maxx and keyEvent[pygame.K_DOWN]:
            nexty = (self.rect.bottom+testdist) // width
            if celly == nexty or (nexty < rows and not grid[celly][cellx].walls[2]):
                move += (0, 1)

        # test move left
        elif miny == maxy and keyEvent[pygame.K_LEFT]:
            nextx = (self.rect.left-testdist) // width
            if cellx == nextx or (nextx >= 0 and not grid[celly][cellx].walls[3]):
                move += (-1, 0)

        self.pos = self.pos + move*(dt/5)
        self.rect.center = self.pos