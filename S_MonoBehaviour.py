import pygame
import os

from pygame.transform import scale


class S_MonoBehaviour:
    def __init__(self, coords=[0, 0], scale=[10, 10], color=(255, 255, 255), isTexture=False, Texture=''):
        self.iGO = False
        self.layer = 0
        self.transform = {'x':coords[0], 'y':coords[1]}
        self.scale = {'x':coords[0], 'y':coords[1], 'z':1}
        self.color = color
        self.Texture = pygame.image.load(Texture) if isTexture else None
        self.pygame = pygame
        self.Input = {}
        self.Way = os.path.split(os.path.dirname(__file__))[0]
        self.GameObject = []
        self.Tags = []

    def Settings(self, Input : tuple):
        self.Input = Input
    
    def Draw(self):
        return ([self.transform['x'], self.transform['y'],
                 self.scale],
                self.color if self.Texture is None else self.Texture)
    
    def Update(self):
        pass
    
    def Start(self):
        self.Texture = pygame.transform.scale(self.Texture, [self.Texture.get_width() * self.scale['z'],
                                                             self.Texture.get_height() * self.scale['z']])
    
    def Disabled(self):
        pass