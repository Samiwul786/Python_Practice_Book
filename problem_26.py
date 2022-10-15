

def minNum(myList):
    
    min = myList[0]
    
    
    for i in range(len(myList)):
        
        if myList[i] < min:
            min = myList[i]
            
    print(min)        
            
def maxNum(myList):
    
    max = myList[0]
    
    for i in range(len(myList)):
        
        if myList[i] > max:
            max = myList[i]
            
    print(max)                    

def minStr(myList):
    
    min = myList[0]
    
    
    for word in myList:
        
        if len(word) < len(min):
            min = word
            
    print(min)        
            
def maxStr(myList):
    
    max = myList[0]
    
    for word in myList:
        
        if len(word) > len(max):
            max = word 
            
    print(max)           
  


  
# myList = ["samiwul", "mussaweer", "sami"]
# minStr(myList)
# maxStr(myList)  

myNumList = [5,4,3,2,1]
maxNum(myNumList)
minNum(myNumList)
  


            