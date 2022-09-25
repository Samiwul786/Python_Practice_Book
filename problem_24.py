
# Problem 24: Write a function factorial to compute factorial of a number. Can you use the product function defined in the previous example to compute factorial?

def factorial(num:int):
    
    factorial_total = 1
    
    
    for i in range(1, num + 1):
        factorial_total = factorial_total * i
        
    return factorial_total


print(factorial(7))     
        