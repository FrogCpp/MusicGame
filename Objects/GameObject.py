from S_MonoBehaviour import S_MonoBehaviour
import os
import pygame


class Agobject(S_MonoBehaviour):
    def __init__(self):
        super().__init__()
        self.Texture = pygame.image.load(os.path.join(self.Way, 'MusicGame\\Assets\\FreePack\\RookWhite.png'))
        self.WalkSpeed = 62.5
        self.Timer=0
        self.anims = {'Idle': (10, 'MusicGame\\Assets\\GG_Anim\\IDLE.png', 0.5, True),
                    'Run': (8, 'MusicGame\\Assets\\GG_Anim\\RUN.png', 1, False),
                    'AttackRight': (7, 'MusicGame\\Assets\\GG_Anim\\AttackRight.png', 0.5, False),
                    'Hurt': (4, 'MusicGame\\Assets\\GG_Anim\\HURT.png', 1, False),
                    'AttackLeft': (7, 'MusicGame\\Assets\\GG_Anim\\AttackLeft.png', 0.5, False)}
        self.feel = {'anim':'Idle', 'frame':0}

    def Start(self):
        self.transform['x'] = 0
        self.transform['y'] = 0
        self.scale['x'] = 2
        self.scale['y'] = 2
        self.scale['z'] = (self.scale['x'] + self.scale['y']) / 2
        self.AnimU()

    def Update(self):
        if self.GameObject[2].Time['Index'] == 1:
            self.feel['anim'] = 'Idle'
            self.AnimU()
            for i in self.Input:
                if i == 'a' and self.Input[i]: self.transform['x'] -= self.WalkSpeed if self.transform['x'] > 32.5 else 0
                if i == 'd' and self.Input[i]: self.transform['x'] += self.WalkSpeed if self.transform['x'] < 470 else 0
                if i == 'w' and self.Input[i]: self.transform['y'] -= self.WalkSpeed if self.transform['y'] > -47.5 else 0
                if i == 's' and self.Input[i]: self.transform['y'] += self.WalkSpeed if self.transform['y'] < 390 else 0
                if i == 3 and self.Input[i]:
                    self.feel['frame'] = 0
                    self.feel['anim'] = 'AttackRight'
                    self.AnimU()
                if i == 1 and self.Input[i]:
                    self.feel['frame'] = 0
                    self.feel['anim'] = 'AttackLeft'
                    self.AnimU()
                if self.Input[i]: break

        if self.feel['anim'] != 'Idle' and self.feel['frame'] == self.anims[self.feel['anim']][0] - 1:
            self.feel['anim'] = 'Idle'
            self.feel['frame'] = 0
            self.AnimU()
        self.feel['frame'] += self.anims[self.feel['anim']][2] if self.feel['frame'] < self.anims[self.feel['anim']][0] - 1 else - self.anims[self.feel['anim']][0] + 1

    def Draw(self):
        return ([self.transform['x'], self.transform['y'],
                 self.scale],
                self.color if self.Texture is None else self.Texture,
                (0 + int(self.feel['frame']) * 96 * self.scale['z'], 0, 96 * self.scale['z'], 96 * self.scale['z']),
                self.anims[self.feel['anim']][0]
                )

    def AnimU(self):
        a = open(f"{os.path.join(os.environ['USERPROFILE'], 'Desktop', 'stp.txt')}", 'a')
        a.write(f'\n {self.Way}')
        a.close()
        self.Texture = pygame.image.load(os.path.join(self.Way, self.anims[self.feel['anim']][1]))
        self.Texture = pygame.transform.scale(self.Texture, [self.Texture.get_width() * self.scale['z'],
                                                             self.Texture.get_height() * self.scale['z']])