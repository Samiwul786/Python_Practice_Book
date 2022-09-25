
# Problem 13: Write a function istrcmp to compare two strings, ignoring the case.


def istrcmp(word1:str, word2:str):
    
    
    if word1.casefold() == word2.casefold():
        return True    
    else:
        return False
    

result = istrcmp('hwloo', 'Python')
print(result)   
 