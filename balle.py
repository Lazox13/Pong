import pygame
from pygame import Vector2


class Balle:
    def __init__(self):
        self.position = Vector2(400, 200)
        self.rayon = 10
        self.couleur = (255, 255, 255)
        self.direction = Vector2(-3,2)
        self.scorejun = 0
        self.scorejdeux = 0

    def draw(self,screen):
        pygame.draw.circle(screen, self.couleur, self.position, self.rayon)

    def move(self):
        self.position = self.position + self.direction
        print (self.position)

    def border(self):
        if self.position.y < 0 or self.position.y > 800:
            self.direction = Vector2(self.direction.x, self.direction.y * -1)

    def bounce(self):

        #la direction devrait changer en fonction de la hauteur de la balle sur le joueur
        self.direction = Vector2(self.direction.x * -1, self.direction.y * -1)

    def dead(self):
        if self.position.x < 0:
            self.position = Vector2(400, 200)
            self.direction = Vector2(3, 2)
            self.scorejun = self.scorejun + 1
            print(self.scorejun)

        if self.position.x > 800:
            self.position = Vector2(400, 200)
            self.direction = Vector2(-3, 2)
            self.scorejdeux = self.scorejdeux + 1
