#trait pour la séparation du terrain

#score?
import pygame
from pygame import Vector2


class Carte:
    def __init__(self):
        self.couleur = (255, 255, 255)
        self.text = 0
        self.position = Vector2(200,200)
        self.taille = 10