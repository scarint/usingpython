bull = True
while bull:
    choice = input("Please make a selection: ").lower()

    if choice == 'a':
        print("Apple pie!")
    elif choice == 'b':
        print("Orange juice!")
    elif choice == 'c':
        print("Sausage roll!")
    elif choice == 'q':
        bull = False
    else:
        print("Invalid selection")