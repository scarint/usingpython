awesome1 = 100
awesome2 = awesome1

name1 = input("Enter the first name name: ")
name2 = input("Enter the second name name: ")

weight = awesome1 / len(name1)

for char in name1:
    if char.lower() not in ['l', 'o', 'v', 'e']:
        awesome1 -= weight

weight = awesome2 / len(name2)

for char in name2:
    if char.lower() not in ['l', 'o', 'v', 'e']:
        awesome2 -= weight

result = "inconclusive"

if awesome1 / awesome2 > 0.9:
    result = "destined to be together"
elif awesome1 / awesome2 > 0.5:
    result = "the envy of your friends"
elif awesome1 / awesome2 > 0.25:
    result = "compatible"
else:
    result = "going to both die alone"

print("You two are " + result)