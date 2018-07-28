awesome = 100

name = input("Enter your name: ")

weight = 100 / len(name)

for char in name:
    if char.lower() not in ['a', 'e', 'i', 'o', 'u']:
        awesome -= weight

print("Your awesome level is " + str(awesome))