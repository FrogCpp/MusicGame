from S_MonoBehaviour import S_MonoBehaviour
import os
import pygame
import random


class Indicator(S_MonoBehaviour):
    def __init__(self):
        super().__init__()
        self.iGO = True
        self.Texture = (96, 218, 12)
        self.Error = 10
        self.ivents = {'strong share': False, 'weak share': False}
        self.Music = None
        self.layer = 10

    def Start(self):
        self.scale['x'] = 20
        self.scale['y'] = 20
        self.scale['z'] = 1
        self.transform['x'] = 400
        self.transform['y'] = 560

        # self.Music = MusicAnalyser(music_file_name='HorizonMusic.mp3')
        self.Music = self.GameObject[0]
        self.Music.start_music_analyse(accuracy=1, fileName='HorizonMusic.mp3')

    def Update(self):
        self.ivents['strong share'] = self.Music.st_time
        self.ivents['weak share'] = self.Music.wk_time
