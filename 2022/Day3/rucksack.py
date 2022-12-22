f = open("rucksack.txt","r")

finalNum = 0

for i in f:
    list1 = []
    list2 = []
    l = len(i)+1
    r = 0
    k = 0
    for t in i:
        if t != "\n":
            if r < ((l/2)-1):
                list1.append(t)
                r += 1
            else:
                list2.append(t)
                r += 1
                
    #add to final
    for s in list1:
        if k == 0:
            for q in list2:
                if s == q:
                    if ord(s) > 96 and ord(s) < 123:
                        #print(s, ord(s)-96)
                        finalNum += (ord(s) - 96)
                        k += 1
                        break
                        
                    else:
                        #print(s, ord(s)-38)
                        finalNum += (ord(s) - 38)
                        k += 1
                        break
                        
                else:
                    continue
        else:
            continue      
    print(list1)
    print(list2)
print(finalNum)
    
