import csv

class Item:
    all=[]
    granted=False
    def __init__(self, name="No Name", age=-1) -> None:
        assert age >=18, f"Age should be greater than 18"

        self.name = name
        self.age = age
        # print("__init__ run...")
        Item.all.append(self)

    def __str__(self) -> str:
        return (f"{self.name} : {self.age} ==> Garanted: {self.granted}")
    
    def __repr__(self) -> str:
        return f"Item ({self.name} : {self.age}) "
    
    @classmethod
    def instantiateFromCsv(cls):
        with open("test.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
            # print(items)
        # for item in items:
        #     print(item)
        for item in items:
            a = Item(item["name"], int(item["age"]))

    @staticmethod
    def greetings():
        print("Hello, User")


# print(Item.granted)
# print(Item.__dict__)
# item1 = Item("Prem", 20)
# print(item1) 
# print(item1.__dict__)
# print(type(item1.age))
# item1.type = "Real"clear
# print(item1.type)


# a = Item("a", 100)
# b = Item("b", 200)
# c = Item('c', 55)
# for instance in Item.all:
#     print(instance)
# print(Item.all)


# Item.instantiateFromCsv()
# print(Item.all)

# Item.greetings()