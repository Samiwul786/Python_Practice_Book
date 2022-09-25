


# Problem 7: How many multiplications are performed when each of the following line is executed

numcalls = 0

def square(x):
    global numcalls
    numcalls += 1
    return x * x

print(square(5))
print(square(2*3))
print(numcalls)
