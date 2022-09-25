


# Problem 23: Implement a function product, to compute product of a list of numbers.

def product(values:list):
    
    product_total = 1
    
    for i in values:
        
        product_total = i * product_total
        
    return product_total

full_product = product([2,2,2])
print(full_product)    