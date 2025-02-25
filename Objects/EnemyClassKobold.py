from S_MonoBehaviour import S_MonoBehaviour
import os
import pygame
import random


class EnemyClass(S_MonoBehaviour):
    def __init__(self):
        super().__init__()
        self.iGO = True
        self.Texture = pygame.image.load(os.path.join(self.Way, 'MusicGame/Assets/FreePack/RookWhite.png'))
        self.WalkSpeed = 62.5
        self.Timer = 0
        self.anims = {'Idle': (6, 'MusicGame/Assets/KoboldAnim/Sprites/without_outline/IDLE.png', 0.25, True),
                    'Run': (8, 'MusicGame/Assets/KoboldAnim/Sprites/without_outline/Run.png', 1, False),
                    'AttackRight': (5, 'MusicGame/Assets/KoboldAnim/Sprites/without_outline/ATTACKright.png', 0.5, False),
                    'AttackLeft': (5, 'MusicGame/Assets/KoboldAnim/Sprites/without_outline/ATTACKleft.png', 0.5, False)}
        self.feel = {'anim': 'Idle', 'frame': 0}
        self.layer = 0

    def Start(self):
        self.transform['x'] = self.WalkSpeed * 5
        self.transform['y'] = self.WalkSpeed * 3
        self.scale['x'] = 2
        self.scale['y'] = 2
        self.scale['z'] = 1.25
        self.AnimU()

    def Update(self):
        if self.GameObject[-1].ivents['strong share'] and (self.feel['frame'] == self.anims[self.feel['anim']] if self.feel['anim'] == 'AttackRight' or self.feel['anim'] == 'AttackLeft' else True):
            self.feel['anim'] = 'Idle'
            self.AnimU()
            Hero = None
            for j in self.GameObject:
                if 'MainHero' in j.Tags:
                    Hero = j
                    break

            Hero = Hero if random.randint(0, 10) > 7 else None

            if Hero is not None:
                x = Hero.transform['x']
                y = Hero.transform['y']
                if self.transform['x'] - x < 0 < x < 437.5:
                    x_t = x - self.WalkSpeed
                elif self.transform['x'] - x > 0 < x < 437.5:
                    x_t = x + self.WalkSpeed
                elif x == 0:
                    x_t = x + self.WalkSpeed
                else:
                    x_t = x - self.WalkSpeed
                y_t = y
                if self.transform['x'] == x_t and self.transform['y'] == y_t:
                    if self.transform['x'] - x < 0:
                        self.feel['frame'] = 0
                        self.feel['anim'] = 'AttackRight'
                        self.AnimU()
                    if self.transform['x'] - x > 0:
                        self.feel['frame'] = 0
                        self.feel['anim'] = 'AttackLeft'
                        self.AnimU()
                else:
                    if abs(self.transform['x'] - x_t) > abs(self.transform['y'] - y_t):
                        self.transform['x'] += self.WalkSpeed * (-1 if self.transform['x'] - x_t > 0 else 1)
                    else:
                        self.transform['y'] += self.WalkSpeed * (-1 if self.transform['y'] - y_t > 0 else 1)

        if self.GameObject[-1].ivents['weak share'] and (self.feel['frame'] == self.anims[self.feel['anim']] if self.feel['anim'] == 'AttackRight' or self.feel['anim'] == 'AttackLeft' else True):
            self.feel['anim'] = 'Idle'
            self.AnimU()
            Hero = None
            for j in self.GameObject:
                if 'MainHero' in j.Tags:
                    Hero = j
                    break

            Hero = Hero if random.randint(0, 10) > 7 else None

            if Hero is not None:
                x = Hero.transform['x']
                y = Hero.transform['y']
                if self.transform['x'] - x < 0 < x < 437.5:
                    x_t = x - self.WalkSpeed
                elif self.transform['x'] - x > 0 < x < 437.5:
                    x_t = x + self.WalkSpeed
                elif x == 0:
                    x_t = x + self.WalkSpeed
                else:
                    x_t = x - self.WalkSpeed
                y_t = y
                if self.transform['x'] == x_t and self.transform['y'] == y_t:
                    pass
                else:
                    if abs(self.transform['x'] - x_t) > abs(self.transform['y'] - y_t):
                        self.transform['x'] += self.WalkSpeed * (-1 if self.transform['x'] - x_t > 0 else 1)
                    else:
                        self.transform['y'] += self.WalkSpeed * (-1 if self.transform['y'] - y_t > 0 else 1)

        if self.feel['anim'] != 'Idle' and self.feel['frame'] == self.anims[self.feel['anim']][0] - 1:
            self.feel['anim'] = 'Idle'
            self.feel['frame'] = 0
            self.AnimU()
        self.feel['frame'] += self.anims[self.feel['anim']][2] if self.feel['frame'] < self.anims[self.feel['anim']][0] - 1 else - self.anims[self.feel['anim']][0] + 1

    def Draw(self):
        return ([self.transform['x'], self.transform['y'],
                 self.scale],
                self.color if self.Texture is None else self.Texture,
                (0 + int(self.feel['frame']) * 148 * self.scale['z'], 0, 148 * self.scale['z'], 148 * self.scale['z']),
                self.anims[self.feel['anim']][0]
                )

    def AnimU(self):
        self.Texture = pygame.image.load(os.path.join(self.Way, self.anims[self.feel['anim']][1]))
        self.Texture = pygame.transform.scale(self.Texture, [self.Texture.get_width() * self.scale['z'],
                                                             self.Texture.get_height() * self.scale['z']])