f = open("cargoOrig.txt", "r")
t = 0

stack1 = []
stack2 = []
stack3 = []
stack4 = []
stack5 = []
stack6 = []
stack7 = []
stack8 = []
stack9 = []

numberMoves = 0
oldStack = "stack"
newStack = "stack"
movingNumber = 0

for i in f:
    if t == 0:
        stack1.append(i[1])
        stack2.append(i[5])
        stack4.append(i[13])
        t += 1
    elif t == 1:
        stack1.append(i[1])
        stack2.append(i[5])
        stack4.append(i[13])
        stack5.append(i[17])
        stack7.append(i[25])
        t += 1
    elif t == 2:
        stack1.append(i[1])
        stack2.append(i[5])
        stack4.append(i[13])
        stack5.append(i[17])
        stack6.append(i[21])
        stack7.append(i[25])
        t += 1
    elif t == 3:
        stack1.append(i[1])
        stack2.append(i[5])
        stack3.append(i[9])
        stack4.append(i[13])
        stack5.append(i[17])
        stack6.append(i[21])
        stack7.append(i[25])
        t += 1
    elif t == 4:
        stack1.append(i[1])
        stack2.append(i[5])
        stack3.append(i[9])
        stack4.append(i[13])
        stack5.append(i[17])
        stack6.append(i[21])
        stack7.append(i[25])
        stack9.append(i[33])
        t += 1
    elif t == 5:
        stack1.append(i[1])
        stack2.append(i[5])
        stack3.append(i[9])
        stack4.append(i[13])
        stack5.append(i[17])
        stack6.append(i[21])
        stack7.append(i[25])
        stack8.append(i[29])
        stack9.append(i[33])
        t += 1
    elif t == 6:
        stack1.append(i[1])
        stack2.append(i[5])
        stack3.append(i[9])
        stack4.append(i[13])
        stack5.append(i[17])
        stack6.append(i[21])
        stack7.append(i[25])
        stack8.append(i[29])
        stack9.append(i[33])
        t += 1
    elif t == 7:
        stack1.append(i[1])
        stack2.append(i[5])
        stack3.append(i[9])
        stack4.append(i[13])
        stack5.append(i[17])
        stack6.append(i[21])
        stack7.append(i[25])
        stack8.append(i[29])
        stack9.append(i[33])
        t += 1
f.close()
print(stack1,'\n',stack2,'\n',stack3,'\n',stack4,'\n',stack5,'\n',stack6,'\n',stack6,'\n',stack7,'\n',stack8,'\n',stack9)

f = open("cargo.txt", "r")

for i in f:
    if i[6].isnumeric():
        numberMoves = i[5]+i[6]
        numberMoves = int(numberMoves)
        oldStack = oldStack+i[13]
        for t in range(0, numberMoves-1):
            movingNumber = oldStack.pop(0)

        oldStack = "stack"
        movingNumber = 0
        numberMoves = 0
    else:
        numberMoves = int(i[5])
        

    
print(stack1,'\n',stack2,'\n',stack3,'\n',stack4,'\n',stack5,'\n',stack6,'\n',stack6,'\n',stack7,'\n',stack8,'\n',stack9)