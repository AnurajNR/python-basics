#list datatype
car=["maruti","toyota","honda","hyundai","tata"]
print(car)
print(type(car))
print(len(car))
x=list((20,21,21,23))
print(x)
print(car[2])
print(car[-2])
print(car[2:])
print(car[:5])
print(car[-3:4])
print("tata"in car)
print("honda"not in car)
print("ferari" in car)
car[2]="tata"
print(car)
car[3:4]=("porsche","lamborgini")
print(car)
x.append(19)
print(x)
x.insert(0,9)
print(x)
car.extend(x)
print(car)
car.remove("tata")
print(car)
car.remove("lamborgini")
print(car)
car.pop(4)
print(car)
car.pop(4)
print(car)
car.pop()
print(car)
del car[2]
print(car)
# car,clear()
# print(car)
# del(car)
# print(car)
for i in car:
    print(i)

#bike
bike=["pulsar","apache","bullet","mt","unicorn"]
bike.sort()
print(bike)
bike.sort(reverse=True)
print(bike)
y=bike.copy()
print(y)
z=list(car)
print(z)
d=car+bike
print(d)
d.extend(y)
print(d)
list1=["a","b","c"]
list2=[1,2,3,4,4,4]
for i in list2:
    list1.append(i)
print(list1)
a=list2.count(4)
print(a)
