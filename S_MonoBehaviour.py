class S_MonoBehaviour:
    def __init__(self, coords=(0, 0), scale=(10, 10), color=(255, 255, 255), isTexture=False, Texture=''):
        self.coords = coords
        self.scale = scale
        self.color = color
        self.Texture = Texture if isTexture else None
    
    def Draw(self):
        return self.coords, self.scale, self.color if self.Texture is None else self.Texture
    
    def Update(self):
        pass
    
    def Start(self):
        pass
    
    def Disabled(self):
        pass