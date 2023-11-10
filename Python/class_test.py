class Item():
    def __init__(self,name,price):
        self.name=name
        self.price=price
class Phone(Item):
    def __init__(self,w):
        self.w=w
a=Phone("sony",1000,2)
print(a.name)