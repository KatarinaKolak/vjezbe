import numbers 

def maxElement(myList):
    maxE = myList[0]
    
    for i in myList:
        if isinstance(i, numbers.Number) and i > maxE:
            maxE = i
    return maxE

lst = [7, 18, 3, 'a', True, (2,3)]
print(maxElement(lst))