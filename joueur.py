import pygame
from pygame import Vector2


class JoueurUn:

    def __init__(self):
        self.positionh = Vector2(20,350)
        self.positionl = Vector2(20,450)
        self.largeur = 20
        self.couleur = (255, 255, 255)
        self.direction = Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.line(screen, self.couleur, self.positionh, self.positionl, self.largeur)

    def moveup(self):
        print(self.positionh)
        self.direction = (0, -5)
        self.positionh = self.positionh + self.direction
        self.positionl = self.positionl + self.direction


    def movedown(self):

        self.direction = (0, 5)
        self.positionh = self.positionh + self.direction
        self.positionl = self.positionl + self.direction

    def borderup(self):

        if self.positionh.y < 0:
            self.direction = (0, 5)
        else:
            self.direction = (0, 0)

        self.positionh = self.positionh + self.direction
        self.positionl = self.positionl + self.direction

    def borderdown(self):

        if self.positionl.y > 800:
            self.direction = (0, -5)
        else:
            self.direction = (0, 0)

        self.positionh = self.positionh + self.direction
        self.positionl = self.positionl + self.direction

class JoueurDeux:
    def __init__(self):
        self.positionh = Vector2(780,350)
        self.positionl = Vector2(780,450)
        self.largeur = 20
        self.couleur = (255, 255, 255)
        self.direction = Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.line(screen, self.couleur, self.positionh, self.positionl, self.largeur)

    def moveup(self):
        print("J2up")
        self.direction = (0, -5)
        self.positionh = self.positionh + self.direction
        self.positionl = self.positionl + self.direction

    def movedown(self):

        self.direction = (0, 5)
        self.positionh = self.positionh + self.direction
        self.positionl = self.positionl + self.direction

    def borderup(self):

        if self.positionh.y < 0:
            self.direction = (0, 5)
        else:
            self.direction = (0, 0)

        self.positionh = self.positionh + self.direction
        self.positionl = self.positionl + self.direction

    def borderdown(self):

        if self.positionl.y > 800:
            self.direction = (0, -5)
        else:
            self.direction = (0, 0)

        self.positionh = self.positionh + self.direction
        self.positionl = self.positionl + self.direction