# Read the puzzle file
boxIds = tuple(open("day-02.txt", 'r'))

# First part of the day

countOfDouble = 0
countOfTriple = 0

for boxId in boxIds:
    twice = False
    threeTimes = False
    for char in boxId:
        c = boxId.count(char)
        if c == 2:
            twice = True
        if c == 3:
            threeTimes = True
    if twice:
        countOfDouble += 1
    if threeTimes:
        countOfTriple += 1

print("Double: ", countOfDouble)
print("Triple: ", countOfTriple)
print("Checksum of the Box:", countOfDouble * countOfTriple)

