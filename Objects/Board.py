from S_MonoBehaviour import S_MonoBehaviour
import os


class Agobject(S_MonoBehaviour):
    def __init__(self):
        super().__init__()
        self.Texture = os.path.join(self.Way, 'MusicGame\\Assets\\FreePack\\Board.png')
        self.WalkSpeed = 5

    def Start(self):
        self.scale['x'] = 500
        self.scale['y'] = 500
        self.transform['x'] = 250
        self.transform['y'] = -250