name = input("What is your name? ")

# Convert first character to upp, all others to lower
name = name[0].upper() + name[1:].lower()

# Bounding box based on length of name
print("-" * (len(name) + 6))
print(".::" + name + "::.")
# Lower bounding box
print("-" * (len(name) + 6))
