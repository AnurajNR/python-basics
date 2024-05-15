#list datatype
fruit=["apple","mango","orange","guava","pineapple","strawberry"]
print(fruit)
print(type(fruit))
print(len(fruit))
x=list((10,11,12,))
print(x)
print(fruit[1])
print(fruit[-1])
print(fruit[:2])
print(fruit[0:])
print(fruit[:3])
print(fruit[-5:-2])
print("apple"in fruit)
print("mango"not in fruit)
print("blackberry"in fruit)
fruit[1]="pineapple"
print(fruit)
fruit[2:4]=["berry","dragonfruit"]
print(fruit)
x.append(13)
print(x)
x.insert(0,9)
print(x)
fruit.extend(x)
print(fruit)
fruit.remove("apple")
print(fruit)
fruit.pop(4)
print(fruit)
fruit.pop()
print(fruit)
del fruit[4]
print(fruit)
# fruit.clear()
# print(fruit)
# del fruit
# print(fruit)
for i in fruit:
    print(i)


#colours
colours=["green","blue","red","pink"]
colours.sort()
print(colours)
colours.sort(reverse=True)
print(colours)
y=colours.copy()
print(y)
z=list(fruit)
print(z)
d=fruit+colours
print(d)
d.extend(y)
print(d)
list1=["a","b","c"]
list2=[1,2,3,3,3,3]
for i in list2:
    list1.append(i)
print(list1)
a=list2.count(3)
print(a)
