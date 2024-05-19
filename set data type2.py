#set data type2
x={"sachin","dhoni","kohli","rohit","rahul"}
print(x)
print(type(x))
print(len(x))
y=set((1,2,3,4,5))
print(x)
for i in x:
    print(i)
print("sachin"in x)
print(6 in y)
x.add("dravid")
print(x)
x.update(y)
print(x)
z={"vijay","surya","srk","fahad","dq"}
print(z)
x.update(z)
print(x)
y.remove(3)
print(y)
y.discard(6)
print(y)
y.discard(5)
print(y)
h=y.pop()
print(h)
#x.clear()
#print(x)
#del x

d={2,4,6,8}
e=x.union(d)
print(e)
f={10,20,30,40}
g={100,200,300}
i=f.intersection(g)
print(i)
j=f.difference(g)
print(j)