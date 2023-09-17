#Part 1
##file = open('day5input.txt','r')
##count = 0
##matches = ('ab','cd','pq','xy')
##vowels = ('a','e','i','o','u')
##
##def double(line):
##    for i in range (len(line)-1):
##        if line[i] == line[i+1]:
##            return True
##
##
##for line in file:
##    countCheck = 3
##    if any([char in line for char in matches]):
##        continue
##    else:
##        for char in line:
##            if countCheck <= 0 or (char in vowels) :
##                countCheck -= 1
##        if double(line) and countCheck <= 0:
##            count += 1
##print(count)
    

#Part 2
import re
file = open('day5input.txt','r')
count = 0


def double(line):
    list1 = []
    for i in range (len(line)-2):
        doubleLetter = line[i]+line[i+1]
        list1.append(doubleLetter)
    for t in list1:
        if line.count(t) >=2:
            return True         

def repeat(line):
    for i in range (len(line)-2):
        if line[i] == line[i+2]:
            return True

for line in file:
    if double(line) and repeat(line):
        count += 1
    
print(count)

