file = open("data.txt", "r")

data = file.readlines()

file.close()

question = ""

bull = True
changed = False

while bull:
    question = input(">")
    found = False

    for li in data:
        if(li.split(": ")[0].lower() == question.lower()):
            found = True
            print(li.split(": ")[1], end="")

    if question.lower() == 'q':
        found = True
        bull = False

    if found == False:
        answer = input("How should this be answered? ")
        data.append(question + ": " + answer)
        changed = True

if changed == True:
    file = open("data.txt", "w")
    for line in data:
        file.write(line)
    file.write("\n")
    file.close()