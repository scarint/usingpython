import pickle

phonebook = { "Alistair": { "home": "07834210928", "work": "01137892472" },
"Micah": { "home": "07834210928", "work": "01137892472"}}

favorite_colour = { "lion": "yellow", "kitty": "red"}

pickle.dump(favorite_colour, open("save.txt", "wb"))

favorite_color = pickle.load(open("save.txt", "rb"))

print(favorite_color)