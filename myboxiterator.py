class MyBoxIterator():
    #def __init__(self):
        #self.num=1
    def __iter__(self):
        self.num=1
        return self

    def __next__(self):
        if self.num<=150:
            x=self.num
            num=self.num
            self.num+=2
            return x
        else:
            raise StopItration
if __name__=="__main__":
    L=MyBoxIterator()
    for item in L:
        print (item)

            
        
        
