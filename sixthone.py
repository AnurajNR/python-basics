#string datatype
x="dubai"
print(type(x))
print(len(x))
print(x[1])
for i in x:
    print(i)
y="   python,is,a,programming,language  "
print(type(y))
print("programming" in y)
print("of" not in y )
print(y[2:5])
print(y[:5])
print(y[3:])
print(y[-1])
print(y[-5:-2])
print(y.upper())
print(y.lower())
print(y.strip())
print(y.replace("p","h"))
print(y.split(","))
print(x+y)
age=30
z="my name is john and i am{}"
print (z.format (age))
d=20
e=100
malin= "i have{}apples and the amount is {}for each"
print(malin.format(d,e))
f="i love apple and apple is a fruit"
print(f.count ("apple"))