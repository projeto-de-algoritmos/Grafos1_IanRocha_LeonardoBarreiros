class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.playerHeight = 15
        self.playerWidth = 15
        self.movementSpeed = 0.1
        self.imagePlayer = None

    def moveUp(self):
        if (self.y < 0):
            self.y = 0

        self.y = self.y - self.movementSpeed

    def moveDown(self, limit):
        if (self.y >= limit):
            self.y = limit

        self.y = self.y + self.movementSpeed

    def moveRight(self, limit):
        if (self.x >= limit):
            self.x = limit

        self.x = self.x + self.movementSpeed

    def moveLeft(self):
        if (self.x < 0):
            self.x = 0

        self.x = self.x - self.movementSpeed