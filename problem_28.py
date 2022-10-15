



def cumalative_product(myList):
    
    
    # Don't set up the product to be 1 because I am using the * operator (anything times 0 = 0)
    product = 1
    cumalative_list = []
    
    for i in range(0, len(myList)):
        
        product = product * myList[i]
        cumalative_list.append(product)
        
    print(cumalative_list) 
    
mylist = [4,3,2,1]
cumalative_product(mylist)    
       
    