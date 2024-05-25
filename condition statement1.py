#condition statement.py
#x=int(input("enter a number"))
#if x>0:
#     print("x is positive")
# elif x<0:
#     print("x is negative")
# else:
#     print("x is 0") 
# y=int(input("enter an even number"))
# if y%2==0:
#     print("y is even")
# else:
#     print("y is odd")  
#calculator
# x=int(input("enter first number:")) 
# y=int(input("enter second numbeer:"))
# z=input("enter a operatr")
# if z=='+':
#     sum=x+y
#     print(sum)
# elif z=='-':
#     diff=x-y
#     print(diff)
# elif z=='*':
#     diff=x*y
#     print(mul)
# elif z=='/':
#     div=x/y
#     print(div)
# else:
#     print("invalid operator") 
# #factorial
# a=int(input("enter a number"))
# fact=1
# while(a>1):
#     fact=fact*a
#     a=a-1
# print(fact)                    
  #fibanocci series
x=int(input("ener a number"))
a=0
b=1
print("fibanocci series")
for z in range(0,x):
    if z<=1:
        c=z
    else:
        c=a+b
        a=b
        b=c
    print(c,end='')


        
        
        
    
        
