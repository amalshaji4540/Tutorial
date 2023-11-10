import csv

class Item():

    pay_rate=0.8 #class attribute that can be used by all objects of this class
    all=[]

    def __init__(self, name:str, price:int, quantity=0): #setting datatypes of each attributes

        #Run validation to received values and setting error messages
        assert price>=0,f"Price {price} is not greater than or equal to zero!" 
        assert quantity>=0, f"Quantity {quantity} is not greater than or equal to zero!"

        #assign to self object
        self.name=name
        self.price=price
        self.quantity=quantity
        Item.all.append(self)

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as file:
            reader=csv.DictReader(file)
            items=list(reader)
            
        for item in items:
            Item(
                name=item.get("Name"),
                price=int(item.get("price")),
                quantity=int(item.get("quantity"))
            )
        
    def calculate_total_price(self):
        return self.price*self.quantity
    
    def apply_discount(self):
        self.price=self.price*self.pay_rate
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
    
class Phone(Item):
    def __init__(self, name: str, price: int):
        super().__init__(name, price)
a=Phone()
print(Phone.all)
# item1=Item("coconut", 100, 2)
# print(item1.name)
# print(item1.calculate_total_price())
# print(Item.pay_rate)
# print(item1.pay_rate)
# print(item1.__dict__)
# item1.apply_discount()
# print(item1.price)
# item2=Item("Iphone",1000,4)
# item2.pay_rate=0.7
# item2.apply_discount()
# print(item2.price)

# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

# print(Item.all)
# for instance in Item.all:
#     print(instance.name)

# Item.instantiate_from_csv()
# print(Item.all)

# Item("Amal",100,1)
# print(Item.all)

