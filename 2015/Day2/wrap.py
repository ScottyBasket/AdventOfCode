f = open("wrapTrial.txt", "r")

totalArea = 0

for i in f:
    if i[2] == "x":
        l = (i[0]+i[1])
        if i[5] == "x":
            w = i[3]+i[4]
            if i[7] == "/n":
                h = i[6]
            else:
                h = i[6]+i[7]
        else:
            w = i[3]
            if len(i) == 7:
                h = i[5]+i[6]
            else:
                h = i[5]
                
    elif i[1] == "x":
        l = i[0]
        if i[3] == "x":
            w = i[2]
            if i[6] == "/n":
                h = i[4]+i[5]
            else:
                h = i[4]
        elif i[3] != "x":
            w = i[2]+i[3]
            if i[6] != "/n":
                h = i[5]+i[6]
            else:
                h = i[5]
    l = int(l)
    w = int(w)
    h = int(h)
    side1 = 2*l*w
    side2 = 2*w*h
    side3 = 2*h*l

    area1 = l*w
    area2 = w*h
    area3 = h*l

    if area1 < area2 and area1 < area3:
        smallestSide = area1
    elif area2 < area1 and area2 < area3:
        smallestSide = area2
    elif area3 < area2 and area3 < area1:
        smallestSide = area3

    squareFeet = side1 + side2 + side3

    totalPresent = squareFeet + smallestSide

    totalArea += totalPresent

print(totalArea)
    
            
"""
    w = int(i[2])
    h = int(i[4])
    size = (2*l*w)+(2*w*h)+(2*h*l)
    print(size)
    """
