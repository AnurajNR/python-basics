#loop2
x=1
while x<10:
    print(x)
    x+=1
x=0
while x<11:
    print(x)
    if x==6:
        break
    x+=1
x=0
while x<11:
    x+=4
    if x==6:
        continue
    print(x)


