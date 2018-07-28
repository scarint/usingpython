# http://usingpython.com/python-lists/
# Write a program to store items in an inventory for an RPG computer game.
# Your character can add items (like swords, shields, and various potions)
# to their inventory, as well as 'use' an item, that will remove it from the
# inventory list.
# You could even have other variables like 'health' and 'strength', that are
# affected by 'finding' or 'using' items in the inventory.

health = 100
armor = 100
weight = 0
maxWeight = 100

def ReportStats(itemList, maxWeight):
    health = 100
    armor = 100
    weight = 0
    print("Equipment: ")
    for item in itemList:
        health = health + item[3]
        armor = armor + item[4]
        weight = weight + item[5]
        print(item[0])

    if weight > maxWeight:
        print("\n!!!WARNING: Encumbered!!!\n")
    
    print("Total health:\t" + str(health) + "\n"
        "Total armor:\t " + str(armor) + "\n"
        "Total weight:\t" + str(weight) + "\n")

# Item framework:
# item-type = ['name', #atk, #speed, #health, #armor, #weight]
# speed 1-10; 1 is fastest
weapon1 = ['sword', 50, 5, 0, 0, 20]
weapon2 = ['stick', 10, 1, 0, 0,  5]
weapon3 = ['axe',   70, 7, 0, 0, 50]

armor1 =  ['helmet',      0, 0, 0,  5,  3]
armor2 =  ['pauldron',    0, 0, 0, 10,  7]
armor3 =  ['breastplate', 0, 0, 0, 30, 15]
armor4 =  ['greaves',     0, 0, 0, 10,  8]
armor5 =  ['shield',      0, 0, 0, 20, 10]

potion1 = ['smallHealth', 0, 0, 10,  0,  2]
potion2 = ['medHealth',   0, 0, 20,  0,  5]
potion3 = ['largeHealth', 0, 0, 50,  0, 10]
potion4 = ['smallArmor',  0, 0,  0, 10,  5]
potion5 = ['medArmor',    0, 0,  0, 20, 10]
potion6 = ['largeArmor',  0, 0,  0, 50, 15]

items_available = [weapon1, weapon2, weapon3, armor1, armor2, armor3, armor4, potion1, potion2, potion3, potion4, potion5, potion6]

itemList1 = [weapon1, armor1, armor2, potion3, potion4]
itemList2 = [weapon2, armor2, armor3, armor4, armor5]
itemList3 = [weapon3, armor1, armor2, armor3, armor4, armor5, armor5]

ReportStats(itemList1, maxWeight)
ReportStats(itemList2, maxWeight)
ReportStats(itemList3, maxWeight)
