from S_MonoBehaviour import S_MonoBehaviour
import os
import pygame
import random

class Indicator(S_MonoBehaviour):
    def __init__(self):
        super().__init__()
        self.Texture = (96, 218, 12)
        self.TimeCodes = [1]
        self.Time = {'Index': 0, 'NowTime': 0, 'NowIndex': 0}
        self.Error = 10

    def Start(self):
        self.scale['x'] = 20
        self.scale['y'] = 20
        self.scale['z'] = 1
        self.transform['x'] = 400
        self.transform['y'] = 560
        for i in range(1000): self.TimeCodes.append(self.TimeCodes[-1] + random.randint(1, 100) / 100)
        self.layer = 2

    def Update(self):
        if abs(self.TimeCodes[self.Time['NowIndex']] - self.Time['NowTime']) < self.Error:
            self.Time['Index'] = 1
            self.Time['NowIndex'] += 1
        else:
            self.Time['Index'] = 0
        self.Time['NowTime'] += 1/60
        if self.Time['Index'] == 1:
            self.Texture = (222, 27, 14)
        else:
            self.Texture = (96, 218, 12)