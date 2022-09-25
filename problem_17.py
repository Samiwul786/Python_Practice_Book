


# Problem 17: What happens when the following code is executed? Will it give any error? Explain the reasons.

"""The following code will not cause an error
because the if statement is true"""
"""When the else part of the code is executed this will cause an error as the 
variable y is undefined (not created)"""

x = 2

if x == 2:
    print(x)
else:
    print(y)    