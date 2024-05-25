#python functions
def anu():
    print("abcdef")
anu()  
#arbitary functions
def numbers(*x):
      print(x[5])
numbers(1,2,3,4,5,6,7)  
#keyword arguments
def names(a,b,c):
     print(c) 
names(a="aa",b="bb",c="cc") 
#keyword arbitary arguments
def letters(**x):
     print(x["y"])
letters(y=4) 
#default parameter value
def myplace(place="kollam"):
     print(place)
myplace("tvm")
myplace()
#return statement
def car(x):
     return 10+x
print(car(10)) 
def numb(x,y):
     return x+y
print(numb(10,11)) 
#pass statement
def lorry():
     pass
#lambda functions
x=lambda b:b+10
print(x(6))
b=lambda x,y,z:x+y+z
print(b(2,3,4))



    




