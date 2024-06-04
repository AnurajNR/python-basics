try:
    print(x)
except:
    print("error occured")


try:
    print(x)
except NameError:
    print("x is not defined")
except:
    print("something else is not defined")  


try:
    print(10)
except:
    print("error occured")          
else:
    print("no error") 
finally:
    print("finished")       

y=-8
if y<0:
    raise Exception("no numbers below 0 allowed")           
       
