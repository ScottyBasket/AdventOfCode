f = open("floors.txt", "r")

floor = 0
finalFloor = 0

for i in f:
    for char in i:
        if i[floor] == "(":
            floor += 1
            finalFloor += 1
        elif i[floor] == ")":
            floor +=1
            finalFloor -=1
            if finalFloor == -1:
                print(floor)
        
print(finalFloor)
        
    
