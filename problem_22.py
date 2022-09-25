

# Problem 22: What happens when the above sum function is called with a list of strings? Can you make your sum function work for a list of strings as well.

def sum(values:list):
    
    total = ""
    
    for i in values:
        total = total + i 
        
    return total


words_total = sum(["Hello", "World"])     
words_total2 = sum(["aa", "bb", "cc"])  
print(words_total)
print(words_total2)
