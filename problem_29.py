

def uniqValues(myList):
    
    uniq_nums = []
    
   # num = myList[0]
    
    for item in (myList):
        
        if (item not in uniq_nums):
            uniq_nums.append(item)
                 
    print(uniq_nums)
    

def uniqValues2(myList):
    
    print(set(myList))
    
myList = [1,2,1,3,2,5]
uniqValues(myList)         
uniqValues2(myList) 
             