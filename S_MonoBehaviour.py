import pygame
class S_MonoBehaviour:
    def __init__(self, coords=[0, 0], scale=[10, 10], color=(255, 255, 255), isTexture=False, Texture=''):
        self.transform = coords
        self.scale = scale
        self.color = color
        self.Texture = Texture if isTexture else None
        self.pygame = pygame
        self.Input = {}

    def Settings(self, Input : tuple):
        self.Input = Input
    
    def Draw(self):
        return ([(self.transform[0] - self.scale[0] / 2, self.transform[1] - self.scale[1] / 2),
                 (self.transform[0] - self.scale[0] / 2, self.transform[1] + self.scale[1] / 2),
                 (self.transform[0] + self.scale[0] / 2, self.transform[1] + self.scale[1] / 2),
                 (self.transform[0] + self.scale[0] / 2, self.transform[1] - self.scale[1] / 2)],
                self.color if self.Texture is None else self.Texture)
    
    def Update(self):
        pass
    
    def Start(self):
        pass
    
    def Disabled(self):
        pass