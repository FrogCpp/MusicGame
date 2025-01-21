import pygame
import os

from pygame.transform import scale


class S_MonoBehaviour:
    def __init__(self, coords=[0, 0], scale=[10, 10], color=(255, 255, 255), isTexture=False, Texture=''):
        self.transform = {'x':coords[0], 'y':coords[1]}
        self.scale = {'x':coords[0], 'y':coords[1]}
        self.color = color
        self.Texture = Texture if isTexture else None
        self.pygame = pygame
        self.Input = {}
        self.Way = os.path.split(os.path.dirname(__file__))[0]

    def Settings(self, Input : tuple):
        self.Input = Input
    
    def Draw(self):
        return ([self.transform['x'] - self.scale['x'] / 2, self.transform['y'] + self.scale['y'] / 2,
                 self.scale['x'], self.scale['y']],
                self.color if self.Texture is None else self.Texture)
    
    def Update(self):
        pass
    
    def Start(self):
        pass
    
    def Disabled(self):
        pass