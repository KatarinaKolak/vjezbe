import numbers 

def maxElementRek(myList, n):
    if n - 1 == 0:
        return myList[n-1]
    if isinstance(myList[n-1], numbers.Number):
        return max(myList[n-1], maxElementRek(myList, n - 1))
    
    return maxElementRek(myList, n - 1)
    

lst = [7, 18, 3, 'a', '122', (3,2)]
print(maxElementRek(lst, len(lst)))
