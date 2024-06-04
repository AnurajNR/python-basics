#class 
# class malin:
#     x=10
# y=malin()
# print(y.x)
# # malin.__init__


# class person:
#     def __init__(self,name,age) -> None:
#         self.name=name
#         self.age=age
# z=person("malin",15)
# print(z.name)
#print(z.age)

#inheritance
class person:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
    def anuraj(self):
        
        (self.name,self.age)
class student(person):
    pass
b=student("abhiram",27)
b.anuraj()     

#polymorphism
#function polymorphism
x=[2,4,6,8]
print(len(x))
y=tuple(x)
print(type(y))
z="malin"
print(len(z))
y1={"name":"anuraj"}
print(len(y1))
y2={"malin","anuraj","kannanunni","abhiram"}
print(len(y2))
print("anuraj"*3)