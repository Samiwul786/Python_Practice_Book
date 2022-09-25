

# Problem 10: What will be the output of the following program?

x = 1

def f():
    
    global x
    y = x
    x = 2
    return x + y

print(x) #Output: 1
print(f()) #Output: 3
print(x) #Output: 2

# Output: Causes an UnboundLocalError without line 9