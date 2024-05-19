#tupple data type
x=[1,2,3,4,5]
print(x)
print(len(x))
print(type(x))
print(x[3])
y=["honda"]
print(type(y))
z=tuple((10,20,30,40))
print(z)
print(x[:3])
print(z[:2])
print(z[4:])
print(z[2:])
print("tata"not in y)
x=list(z)
print(x)
x[2]=6
print(x)
z=tuple(x)
print(z)
for i in z:
    print(i)
print(y+x)
x=(2,4)
print(x*2)
print(x.count(2))