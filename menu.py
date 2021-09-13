import pygame
from obj import Obj


class Menu:

    def __init__(self, image):

        self.background = Obj(image, 0, 0)
        self.chance_scene = False

    def draw(self, window):

        self.background.group.draw(window)

    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.chance_scene = True


class GameOver(Menu):

    def __init__(self, image):
        super().__init__(image)



