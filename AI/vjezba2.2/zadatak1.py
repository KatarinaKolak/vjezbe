def predikat(element):
    return True if element > 5 else False

def count_iter(lst, predikat):
    lst = [1 for element in lst if predikat(element)]
    
    return len(lst)

def count_rek(lst, predikat, counter = 0):
    if len(lst) == 0:
        return counter
    
    if predikat(lst[0]):
        counter += 1
        
    return count_rek(lst[1:], predikat, counter)
    

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(count_rek(lst, predikat))