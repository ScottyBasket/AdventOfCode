"""
A = rock
B = paper
C = scissors

X = lose
Y = draw
Z = win

rock = 1
paper = 2
scissors = 3
"""

f = open("rockpaperscissors.txt", "r")

wins = 0

for i in f:
    if i[2] == "X" and i[0] == "C":
        wins += 7
    elif i[2] == "Y" and i[0] == "A":
        wins += 8
    elif i[2] == "Z" and i[0] == "B":
        wins += 9
    elif i[0] == "A" and i[2] == "X":
        wins += 4
    elif i[0] == "B" and i[2] == "Y":
        wins += 5
    elif i[0] == "C" and i[2] == "Z":
        wins += 6     
    elif i[0] == "B" and i[2] == "X":
        wins += 1
    elif i[0] == "C" and i[2] == "Y":
        wins += 2
    elif i[0] == "A" and i[2] == "Z":
        wins += 3
    else:
       continue

print(wins)


