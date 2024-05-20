#dictionary(data type)
x={"name":"anuraj","age":27,"job":"data analyst"}
print(x)
print(type(x))
print(len(x))
y=dict(honda="city")
print(y)
print(x["age"])
print(x.get("job"))
print(x.keys())
print(x.values())
print(x.items())
print("age"in x)
print("age"not in x)
x["name"]="anu"
print(x)
x.update({"age":26})
print(x)
x.update({"palce":"kadavoor"})
print(x)
x["colour"]="red"
print(x)
x.pop("age")
print(x)
x.popitem()
print(x)
#del x["name"]
#print(x)
#x.clear()
#print(x)
#del x
#print(x)
for i in x:
    print(i)
for i in x:
    print(x[i]) 
for i in x.keys():
    print(i)
for i in x.values():
    print(i)
for i in x.items():
    print(i)
y=x.copy()
print(y)
z=dict(x)
print(x)
family={"child1":{"name":"malin","age":27},"child2":{"name":"abhiram","age":27},"child3":{"name":"kannanunni","age":27}}
print(family)
print(family["child3"]["name"])
print(family["child2"]["age"])

