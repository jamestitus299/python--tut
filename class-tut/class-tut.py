import csv
from Item import Item

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


Item.instantiateFromCsv()
print(Item.all)

# Item.greetings()


