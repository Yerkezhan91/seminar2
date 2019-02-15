from myclass import Student
class MyBox:
    def __init__(self):
        self.color=clr
        self.weidth=w
        self.height=h

    def __len__(self,l):
        self.l=len(self.color)
    def __add__(self,b):
        self.MyBox.append(b)
        self.b=5
    def __remove__(self,h):
        assert h in self.MyBox
        val=self.MyBox.val(h)
        return self.MyBox.pop(val)
    def __contains__(self,w):
        return w in self .MyBox
    def _iter__(self, w):
        return  MYBox(self.w)

MyBox=Student()
print(MyBox.b)
print(MyBox.l)
