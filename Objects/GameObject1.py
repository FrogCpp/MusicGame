from S_MonoBehaviour import S_MonoBehaviour


class AbobbaScript(S_MonoBehaviour):
    def __init__(self):
        super().__init__()
        self.WalkSpeed = 5

    def Start(self):
        self.transform['x'] = 200
        self.transform['y'] = 200
        self.scale[0] = 50
        self.scale[1] = 50

    def Update(self):
        self.transform['x'] += self.Input[self.pygame.key.name(self.pygame.K_d)] * self.WalkSpeed
        self.transform['x'] -= self.Input[self.pygame.key.name(self.pygame.K_a)] * self.WalkSpeed
        self.transform['y'] += self.Input[self.pygame.key.name(self.pygame.K_s)] * self.WalkSpeed
        self.transform['y'] -= self.Input[self.pygame.key.name(self.pygame.K_w)] * self.WalkSpeed