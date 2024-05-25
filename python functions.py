def malin():
    print("hgcfjchjb")
malin()
#arbitrary arguments
def numbers(*x):
    print(x[5])
numbers(1,2,3,4,9,0,6)
#keyword arguments
def names(a,b,c):
    print(b)
names(a="aa",b="bb",c="cc")
#arbitrary keyword arguments
def letters(**x):
    print(x["y"])
letters(y=4) 
#default paramete value
def mycountry(country="india"):
    print(country)
mycountry("pakistan")
mycountry("usa")
mycountry()
#retrn statement
def car(x):
    return 10+x
print(car(9)) 
def numb(x,y):
    return x+y
print(numb(10,11))
#pass statement
def bike():
    pass
#lambda function
x=lambda a:a+10
print(x(5))  
a=lambda x,y,z:x+y+z
print(a(5,6,7))    