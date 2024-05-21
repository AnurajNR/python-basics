#loop.py
x=1
while x<10:
    print(x)
    x+=1
x=0
while x<11:
    print(x)
    if x==5:
        break
    x+=1
x=0
while x<11:
    x+=3
    if x==5:
        continue
    print(x)


