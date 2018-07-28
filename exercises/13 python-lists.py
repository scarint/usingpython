import random

part1 = ['Tears', 'Fear', 'Happiness', 'Life']
part2 = ['like a', 'for the', 'near the', 'against a']
part3 = ['mountain', 'shadow', 'heartache', 'briefcase']
part4 = ['of a lifetime', 'of my heart' , 'near my face', 'in a reflection']

rand1 = random.randint(0, len(part1) -1)
rand2 = random.randint(0, len(part2) -1)
rand3 = random.randint(0, len(part3) -1)
rand4 = random.randint(0, len(part4) -1)

poem = part1[rand1] + " " + part2[rand2] + " " + part3[rand3] + " " + part4[rand4]
print(poem)