f = open("numCal.txt", "r")

x = 0
y = 0
foo = 0
bar = 0
i = 0

for i in f:
    if i == "\n":
        if x > y and y < foo and y < bar:
            y = x
            x = 0
        elif x > foo and x < bar:
            foo = x
            x = 0
        elif x > bar:
            bar = x
            x = 0
        else:
            x = 0
            continue
    else:
        x = x + int(i)
        
r = y + foo + bar

print(bar)
print(foo)
print(y)

print (r)

