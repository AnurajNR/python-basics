# import math
# #surface area of a circle
# r=int(input("enter radius of a circle"))
# area_of_a_circle=math.pi*r**2
# print(area_of_a_circle)

# #surface area of sphere
# r1=int(input("enter radius of sphere"))
# area_of_sphere=math.pi*r1**2
# print(area_of_sphere)

# #surface area of cone
# r2=int(input("enter radius of cone"))
# h=int(input("enter height of cone"))
# L="slant height of cone"
# L=math.sqrt(r2**2+h**2)
# area_of_cone=math.pi*r2**2+math.pi*r2*L
# print(area_of_cone) 

# prime numbers
# x=int(input("enter a number"))
# for i in range (2,x):
#     if x%i==0:
#         print("not prime")
#     break
# else:
#     print("it is prime")    
# # leapyear
year=int(input("enter the year : "))
import calendar
if calendar.isleap(year):
    print("it is a leap year")
else:
    print("it is not a leap year")    


    
    

      