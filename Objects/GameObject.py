from S_MonoBehaviour import S_MonoBehaviour
import os


class Agobject(S_MonoBehaviour):
    def __init__(self):
        super().__init__()
        self.Texture = os.path.join(self.Way, 'MusicGame\\Assets\\FreePack\\RookWhite.png')
        self.WalkSpeed = 62.5
        self.Timer=0
        self.anims = {'Idle': (10, 'MusicGame\\Assets\\GG_Anim\\IDLE.png'),
                    'Run': (8, 'MusicGame\\Assets\\GG_Anim\\RUN.png'),
                    'Attack': (7, 'MusicGame\\Assets\\GG_Anim\\ATTACK 1.png'),
                    'Hurt': (4, 'MusicGame\\Assets\\GG_Anim\\HURT.png')}
        self.feel = {'anim':'Run', 'frame':0}

    def Start(self):
        self.transform['x'] = 220
        self.transform['y'] = 140
        self.scale['x'] = 70
        self.scale['y'] = 70

    def Update(self):
        if self.Timer == 0 and len(set(self.Input.values())) > 1:
            self.transform['x'] += self.Input[self.pygame.key.name(self.pygame.K_d)] * self.WalkSpeed if self.transform['x'] < 470 else 0
            self.transform['x'] -= self.Input[self.pygame.key.name(self.pygame.K_a)] * self.WalkSpeed if self.transform['x'] > 32.5 else 0
            self.transform['y'] += self.Input[self.pygame.key.name(self.pygame.K_s)] * self.WalkSpeed if self.transform['y'] < 390 else 0
            self.transform['y'] -= self.Input[self.pygame.key.name(self.pygame.K_w)] * self.WalkSpeed if self.transform['y'] > -47.5 else 0
            self.Timer = 2
        self.Timer = self.Timer - 0.1 if abs(self.Timer - 1) > 0.1 else 0
        if self.Timer < 0: self.Timer = 0
        self.feel['frame'] += 1 if self.feel['frame'] < self.anims[self.feel['anim']][0] - 1 else - self.anims[self.feel['anim']][0] + 1

    def Draw(self):
        self.Texture = os.path.join(self.Way, self.anims[self.feel['anim']][1])
        return ([self.transform['x'] - self.scale['x'] / 2, self.transform['y'] + self.scale['y'] / 2,
                 self.scale['x'], self.scale['y']],
                self.color if self.Texture is None else self.Texture,
                (0 + self.feel['frame'] * 96, 0, 96, 96)
                )