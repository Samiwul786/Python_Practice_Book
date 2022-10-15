

# Problem 25: Write a function reverse to reverse a list. Can you do this without using list slicing?

def reverse(values:list):
    
    reversed_list = []
    
    for i in values:
        # print(values[-i])
        reversed_list.append(values[-i])
            
    return reversed_list    

def hello():
    print("Hello world")

print(reverse([1,2,3,4]))        
        