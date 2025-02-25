import os
import pydoc
import inspect


class MainScene(list):
    def __init__(self, *Input):
        super().__init__()
        try:
            self.Way = os.path.split(os.path.dirname(__file__))[0]
            self.Input = {x: 0 for x in Input}
            b = os.path.join(self.Way, 'Objects')
            # for i in os.listdir(b):
            #     if i[:2] != '__' and i[:3] != 'S_' and i[-1] == 'y':
            #         a = pydoc.importfile(os.path.join(b, i))
            #         c = inspect.getmembers(a, inspect.isclass)
            #         self.append(c[0][1]())
            for i in os.listdir(b):
                if i[:2] != '__' and i[:3] != 'S_' and i[-1] == 'y':
                    a = pydoc.importfile(os.path.join(b, i))
                    c = inspect.getmembers(a, inspect.isclass)
                    bol = False
                    helpMe = None
                    for i in c[0]:
                        try:
                             bol = c.layer != -100
                             helpMe = c
                        except:
                             pass
                    self.append(helpMe())
            self.sort(key=lambda x: x.layer)
            for i in self:
                i.GameObject = self.copy()
            for i in self:
                i.Start()
        except Exception as e:
            print(e)
            # a = open(f"{os.path.join(os.environ['USERPROFILE'], 'Desktop', 'stp.txt')}", 'a')
            # a.write(f'\n {e}')
            # a.close()

    def UpdateScene(self):
        for i in self:
            i.Settings(self.Input)
            i.Update()

    def __repr__(self):
        return ' '.join(map(lambda x: f'{x} : {x.layer};\n', self))

    def __str__(self):
        return ' '.join(map(lambda x: f'{x} : {x.layer};\n', self))
