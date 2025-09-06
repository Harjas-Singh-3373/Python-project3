#Task 1 

n=int(input("Enter any number:"))
def factorial(n):
    if n<2:
     return 1 
    else:
     return n * (factorial(n-1))
result = factorial(n)
print("Factorial of" , n ,"is" , result )

#Task 2 
a=int(input("Enter a number: "))
import math
print(f"Square root :" , math.sqrt(a))
print(f"Logarithm : ", math.log(a))
print(f"Sine :  ", math.sin(a))