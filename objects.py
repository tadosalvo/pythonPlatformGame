import pygame


# Player class that defines a new player
# call Player.move(x, y) to move current player on space
class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def create(self, win):
        pygame.draw.rect(win, (255,0,255), (self.x, self.y, self.width, self.height)) 
    


class Platform:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def create(self, win):
        pygame.draw.rect(win, (255,0,255), (self.x, self.y, self.width, self.height))

