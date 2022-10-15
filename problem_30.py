

def duplicateValues(myList):
    
    
    seen = set()
    dup_nums = []
    
   
    
    for num in myList:
        
        if num in seen:
            dup_nums.append(num)
        else:    
            seen.add(num)

            
    print(dup_nums)
    
def duplicateValuesDemo2(mylist):
    
    print(set(mylist))    
    
myList = [1,2,1,3,2,5,5]
duplicateValues(myList)         
# duplicateValuesDemo2(myList)   