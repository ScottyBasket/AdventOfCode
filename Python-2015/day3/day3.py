##Part 1
##file = open('day3input.txt','r')
##mainList = []
##secondList = []
##x = 0
##y = 0
##coord = (x,y)
##mainList.append(coord)
##for line in file:
##    for char in line:
##        if char == '^':
##            x +=1
##            coord = (x,y)
##            mainList.append(coord)
##        elif char == '>':
##            y += 1
##            coord = (x,y)
##            mainList.append(coord)
##        elif char == '<':
##            y -= 1
##            coord = (x,y)
##            mainList.append(coord)
##        elif char == 'v':
##            x -= 1
##            coord = (x,y)
##            mainList.append(coord)
##
##for i in mainList:
##    if i not in secondList:
##        secondList.append(i)
##    else:
##        continue
##
##print(len(secondList))

#Part 2
file = open('day3input.txt','r')
mainList = []
secondList = []
x = 0
y = 0
v = 0
w = 0
coord1 = (x,y)
coord2 = (v,w)
counter = 0
mainList.append(coord1)

for line in file:
    for char in line:
        counter += 1
        if counter % 2 == 0:
            if char == '^':
                x +=1
                coord1 = (x,y)
                mainList.append(coord1)
            elif char == '>':
                y += 1
                coord1 = (x,y)
                mainList.append(coord1)
            elif char == '<':
                y -= 1
                coord1 = (x,y)
                mainList.append(coord1)
            elif char == 'v':
                x -= 1
                coord1 = (x,y)
                mainList.append(coord1)
        else:
            if char == '^':
                v +=1
                coord2 = (v,w)
                mainList.append(coord2)
            elif char == '>':
                w += 1
                coord2 = (v,w)
                mainList.append(coord2)
            elif char == '<':
                w -= 1
                coord2 = (v,w)
                mainList.append(coord2)
            elif char == 'v':
                v -= 1
                coord2 = (v,w)
                mainList.append(coord2)

for i in mainList:
    if i not in secondList:
        secondList.append(i)
    else:
        continue

print(len(secondList))

