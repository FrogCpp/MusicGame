from S_MonoBehaviour import S_MonoBehaviour
import os


class Agobject(S_MonoBehaviour):
    def __init__(self):
        super().__init__()
        self.Texture = os.path.join(self.Way, 'MusicGame\\Assets\\FreePack\\RookWhite.png')
        self.WalkSpeed = 62.5
        self.Timer=0

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