x={"kollam","kochi","tvm","palakkad",}
print(x)
print(type(x))
print(len(x))
y=set((1,2,3,4,5,))
print(x)
for i in x:
    print(i)
print("kollam"in x)
print("kollam"not in x)
print("6"in y)
x.add("mysore")
print(x)
x.update(y)
print(x)
z=[10,11,12,13,14]
x.update(z)
print(x)
y.remove(4)
print(y)
y.discard(6)
print(y)
y.discard(5)
print(y)
h=y.pop()
print(h)
print(h)
#x.clear()
#print(x)
#del x
d={1,2,3,4,}
e=x.union(d)
print(e)
f={10,11,12,13}
g={11,12,13,14}
i=f.intersection(g)
print(i)
j=f.difference(g)
print(j)