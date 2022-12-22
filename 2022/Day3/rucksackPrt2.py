f = open("rucksack.txt","r")

finalNum = 0

list1 = []
list2 = []
list3 = []
comparNum = []

iteration = 0
lineNum = 0
breakP = 0
it = 0

for i in f:
    if iteration < 3:
        if iteration == 0:
            for t in i:
                if t != "\n":
                    list1.append(t)
                else:
                    break
            iteration += 1
        elif iteration == 1:
            for t in i:
                if t != "\n":
                    list2.append(t)
                else:
                    break
            iteration += 1
        elif iteration == 2:
            for t in i:
                if t != "\n":
                    list3.append(t)
                else:
                    break
            for s in list1:
                for l in list2:
                    if s == l:
                        comparNum.append(s)
                    else:
                        continue
                    #print(comparNum)
            for r in comparNum:
                for q in list3:
                    if breakP == 0:
                        if r == q:
                            if ord(r) > 96 and ord(r) < 123:
                                finalNum += (ord(r) - 96)
                                breakP += 1
                                print(r, ord(r)-96)
                                break
                            else:
                                finalNum += (ord(r) - 38)
                                breakP += 1
                                print(r, ord(r)-38)
                                break
                
            breakP = 0
            #reset variables
            iteration = 0
            list1 = []
            list2 = []
            list3 =[]
            comparNum = []
            continue
    else:
        iteration = 0



"""
if iteration == 0:
for t in i:
    if t != "\n":
        list1.append(t)
    else:
        break
iteration += 1
elif iteration == 1:
for i in f:
    for t in i:
        if t != "\n":
            list2.append(t)
        else:
            break
    iteration += 1
elif iteration == 2:
for i in f:
    for t in i:
        if t != "\n":
            list3.append(t)
        else:
            break
    iteration += 1
iteration = 0

print(list1)
print(list2)
print(list3)
"""            

                
#figures out priorities
"""
if s == q:
    if ord(s) > 96 and ord(s) < 123:
        #print(s, ord(s)-96)
        finalNum += (ord(s) - 96)
        k += 1
        break
"""
print(finalNum)
    
