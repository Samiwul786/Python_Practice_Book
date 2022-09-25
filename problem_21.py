

# Problem 21: Python has a built-in function sum to find sum of all elements of a list. Provide an implementation for sum.

def sum(values:list):
    
    total = 0
    for i in values:
        total = total + i
    
    return total

full_sum = sum([1,2,5])     
print(full_sum)   