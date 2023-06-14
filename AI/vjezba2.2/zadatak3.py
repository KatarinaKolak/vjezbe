def binary_search(lst, number, high, low = 0):
    if high >= low:
        if lst[(low + high) // 2] == number:
            return (low + high) // 2
        elif lst[(low + high) // 2] > number:
            return binary_search(lst, number, ((low + high) // 2) - 1, low)
        else:
            return binary_search(lst, number, high, ((low + high) // 2) + 1)
    else:
        return -1
    
    
lst = [2, 3, 4, 10, 40]
if binary_search(lst, 11, len(lst) - 1) == -1:
    print("Nema")
else:
    print("IMA")