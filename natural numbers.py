#sum of n natural numbers
def sum_of_n_natural_numbers(n):
    return(n*(n+2//2))
n=10
print(sum_of_n_natural_numbers(n))
#using lambda
sum_of_n_natural_numbers=lambda n:n*(n+1)//2
print(sum_of_n_natural_numbers(10))


#sum of squares of natural number
def sum_of_squares_of_natural_numbers(n1):
    return(n1*(n1+1)*(2*(n+1))//6)
n=10
print(sum_of_squares_of_natural_numbers(n))
#using lambda
sum_of_squares_of_natural_numbers=lambda n:(n*(n+1)*(2*(n+1))//6)
print(sum_of_squares_of_natural_numbers(10))

#factorial using function
def factorial(x):
    if x==0:
        return 1
    else:
        return(x*factorial(x-1))
x=5
print(factorial(x))

#fibonacci series using function
def fibonacci(n):
    fib1 = [0,1]
    for i in range(2,n):
        fib2 = fib1[-1] + fib1[-2]
        fib1.append(fib2)
    return fib1[:n]
n=10
print(fibonacci(n))
    
