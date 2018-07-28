homeworkMarks = [10, 8, 2, 7]

for mark in homeworkMarks:
    print(mark)
    mark = 0

print(homeworkMarks)

i = 0

while i <= (len(homeworkMarks) -1 ):
    homeworkMarks[i] = 0
    i += 1

print(homeworkMarks)