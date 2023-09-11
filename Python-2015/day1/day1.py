#Part 1
"""
floor = 0
file = open("input.txt","r")

for line in file:
    for i in line:
        if i == "(":
            floor += 1
        elif i==")":
            floor -= 1
print(floor)

file.close()
"""

#Part 2
floor = 0
count = 0
file = open("input.txt","r")

for line in file:
    for i in line:
        count += 1
        
        if i == "(":
            floor += 1
        elif i==")":
            if floor == -1:
                print(count - 1)
                break
            else:
                floor -= 1
print(floor)

file.close()

