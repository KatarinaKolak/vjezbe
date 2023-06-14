def binary_search(number, lst, high, low = 0):
    if high >= low:
        if lst[(high + low) // 2] == number:
            return (high + low) // 2
        elif lst[(high + low) // 2] > number:
            return binary_search(number, lst, ((high + low) // 2), low)
        else:
            return binary_search(number, lst, high, ((high + low) // 2) + 1)
        
    else:
        return -1
    
    
lst = [1, 2, 3, 4, 5, 6]
if binary_search(9, lst, len(lst)-1) != -1:
    print("Broj je u listi")
else:
    print("Broj nije u listi")
    
        
