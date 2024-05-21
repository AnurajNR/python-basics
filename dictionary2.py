#dictionary2 datatype
x={"name":"vijay","age":49,"job":"acting","place":"chennai"}
print(x)
print(type(x))
print(len(x))
y=dict(tamilnadu="chennai")
print(y)
print(x["age"])
print(x.get("job"))
print(x.keys())
print(x.values())
print(x.items())
print("age" in x)
print("age"not in x)
x["name"]="thalapathy"
print(x)
x.update({"place":"chennai"})
print(x)
x["car"]="bmw"
print(x)
x.pop("age")
print(x)
x.popitem()
print(x)
#del x["name"]
#print(x)
#x.clear[x]
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
family={"child1":{"name":"anuraj","age":27},"child2":{"name":"malin","age":27},"child3":{"name":"abhiram","age":27}}
print(family)
print(family["child2"]["name"])
print(family["child3"]["age"])