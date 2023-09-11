#Part 1

"""
file = open("day2.txt","r")
total = 0
    
def calculate(l,w,h):
    side1 = 2*l*w
    side2 = 2*w*h
    side3 = 2*h*l

    smallest = min(side1,side2,side3)

    total = side1 + side2 + side3 + (smallest/2)
    return total

for line in file:
    l, w, h = line.split('x')
    l, w, h = int(l), int(w), int(h)
    total += calculate(l,w,h)
print(total)

file.close()
"""
#Part 2
file = open("day2.txt","r")
total = 0
    
def calculate(l,w,h):
    side1 = 2*l*w
    side2 = 2*w*h
    side3 = 2*h*l

    smallest = min(side1,side2,side3)
    if smallest == side1:
        smallest = l+l+w+w
    elif smallest == side2:
        smallest = w+w+h+h
    elif smallest == side3:
        smallest = h+h+l+l

    total = smallest + (l*w*h)
    return total

for line in file:
    l, w, h = line.split('x')
    l, w, h = int(l), int(w), int(h)
    total += calculate(l,w,h)
print(total)

file.close()
