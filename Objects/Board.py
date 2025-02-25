from S_MonoBehaviour import S_MonoBehaviour
import os
import pygame


class Agobject(S_MonoBehaviour):
    def __init__(self):
        super().__init__()
        self.iGO = True
        self.Texture = pygame.image.load(os.path.join(self.Way, 'MusicGame/Assets/FreePack/Board.png'))
        self.layer = -1

    def Start(self):
        self.scale['x'] = 500
        self.scale['y'] = 500
        self.scale['z'] = 1.95
        self.transform['x'] = 0
        self.transform['y'] = 0
        self.Texture = pygame.transform.scale(self.Texture, [self.Texture.get_width() * self.scale['z'],
                                                             self.Texture.get_height() * self.scale['z']])