
f = open("pairs.txt", "r")

numOfPairs = 0

a = []
b = []
c = []
d = []


for i in f:
    print(i)
    #a two numbers
    if i[1].isnumeric(): 
        a = i[0] + i[1]
        #b two numbers
        if i[4].isnumeric():
            b = i[3] + i[4]
            #c two numbers
            if i[7].isnumeric():
                c = i[6] + i[7]
                if i[10].isnumeric():
                    d = i[9]+i[10]
                else:
                    d = i[9]
            #c one number
            else:
                c = i[6]
                if i[9].isnumeric():
                    d = i[8]+i[9]
                else:
                    d = i[8]
        #b one number
        else:
            b = i[3]
            if i[6].isnumeric():
                c = i[5]+i[6]
                if i[9].isnumeric():
                    d = i[8]+i[9]
                else:
                    d = i[8]
            #c is one number
            else:
                c = i[5]
                if i[8].isnumeric():
                    d = i[7]+i[8]
                else:
                    d = i[7]

    else:
        #a one number
        a = i[0]
        #b is two numbers
        if i[3].isnumeric():
            b = i[2]+i[3]
            #c is two numbers
            if i[6].isnumeric():
                c = i[5]+i[6] 
                if i[9].isnumeric():
                    d = i[8]+i[9] 
                else:
                    d = i[8]
            else:
                c = i[5]
                if i[8].isnumeric():
                    d = i[7]+i[8]
                else:
                    d = i[7]
        #b is one number   
        else:
            b = i[2]
            #c is two numbers
            if i[5].isnumeric():
                c = i[4] + i[5]
                #d is two numbers
                if i[8].isnumeric():
                    d = i[7]+ i[8]
                #d is one number
                else:
                    d = i[7]
            #c is one number
            else:
                c = i[4]
                if len(i) < 7:
                    d = i[6]
                else:
                    d = i[6]+i[7]

        
        
    #print(a, b,  c, d)
    if a <= c and b >= d:
        numOfPairs += 1
        print(a,b,c,d)
        print(numOfPairs)
    elif c <= a and d >= b:
        numOfPairs += 1
        print(a,b,c,d)
        print(numOfPairs)
    else:
        continue
print(numOfPairs)
