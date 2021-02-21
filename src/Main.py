from pygame.locals import *
from Player import *
from Display import *
import pygame


class Game:

    def __init__(self):
        self.running = True
        self.display_game = Display()
        self.player = Player()

    def on_init(self):
        pygame.init()
        self.display_game = pygame.display.set_mode((self.display_game.windowWidth,self.display_game.windowHeight), pygame.HWSURFACE)

        pygame.display.set_caption('Random Maze')
        self.running = True
        playerImage = pygame.image.load("./assets/player.png").convert()
        self.player.imagePlayer = pygame.transform.scale(playerImage, (self.player.playerWidth, self.player.playerHeight))

    def on_event(self, event):
        if event.type == QUIT:
            self.running = False

    def on_loop(self):
        pass

    def on_render(self):
        self.display_game.fill((0,0,0))
        self.display_game.blit(self.player.imagePlayer,(self.player.x,self.player.y))
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):

        limitHeight = self.display_game.windowHeight - self.player.playerHeight
        limitWidth = self.display_game.windowWidth - self.player.playerWidth

        if self.on_init() == False:
            self.running = False

        while(self.running):
            pygame.event.pump()
            keyEvent = pygame.key.get_pressed()

            if (keyEvent[K_UP]):
                self.player.moveUp()

            if (keyEvent[K_DOWN]):
                self.player.moveDown(limitHeight)
            if (keyEvent[K_RIGHT]):
                self.player.moveRight(limitWidth)

            if (keyEvent[K_LEFT]):
                self.player.moveLeft()

            if (keyEvent[K_ESCAPE]):
                self.running = False

            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__" :
    game = Game()
    game.on_execute()

