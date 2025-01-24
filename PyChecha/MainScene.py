import os
import pydoc
import inspect


class MainScene(list):
    def __init__(self, *Input):
        super().__init__()
        self.Way = os.path.split(os.path.dirname(__file__))[0]
        self.Input = {x:0 for x in Input}
        b = os.path.join(self.Way, 'Objects')
        for i in os.listdir(b):
            if i[:2] != '__' and i[:3] != 'S_':
                a = pydoc.importfile(os.path.join(b, i))
                c = inspect.getmembers(a, inspect.isclass)
                self.append(c[0][1]())
                self[-1].Start()
        for i in self:
            i.GameObject = self


    def UpdateScene(self):
        for i in self:
            i.Settings(self.Input)
            i.Update()