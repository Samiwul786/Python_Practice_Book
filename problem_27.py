


def cumalative_sum(myList):
    
    sum = 0
 
    cumalative_list = []
    
    for i in range(0, len(myList)):
        
        sum = sum + myList[i]
        cumalative_list.append(sum)
        
        
        
    print(cumalative_list)
    

myList = [1,2,3,4]    
cumalative_sum(myList)        