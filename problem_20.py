

# Problem 20: What will be the output of the following program?

x = [0, 1, [2]]
x[2][0] = 3
print(x) #Output: [0,1,[3]]

x[2].append(4)
print(x) #Output: [0,1,[3,4]]

x[2] = 2
print(x) #Output: [0,1,2]

