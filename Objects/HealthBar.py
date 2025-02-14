from S_MonoBehaviour import S_MonoBehaviour
import os
import pygame


class HBar(S_MonoBehaviour):
    def __init__(self):
        super().__init__()
        self.Texture = (191, 191, 191)
        self.layer = 1

    def Start(self):
        self.scale['x'] = 300
        self.scale['y'] = 30
        self.scale['z'] = 1
        self.transform['x'] = 5
        self.transform['y'] = 560