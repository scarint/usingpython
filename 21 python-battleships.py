board = [ ['o', 'o', 'o'],
['o', 'x', 'x'],
['o', 'o', 'o'] ]

print(board)

x = int(input("X coordinate: ")) - 1
y = int(input("Y coordinate: ")) - 1

if board[x][y] == 'x':
    print("Hit!")
else:
    print("Miss!")

board[x][y] = 'h'
print(board)