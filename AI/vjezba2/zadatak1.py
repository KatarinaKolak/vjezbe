def predikat(element):
    return True if element % 2 == 0 else False

def count_iter(lst, predikat):
    counter = 0
    
    for element in lst:
        if predikat(element):
            counter += 1
    
    return counter

def count_rek(lst, predikat):
    if len(lst) == 0:
        return 0
       
    return predikat(lst[0]) + count_rek(lst[1:], predikat)
    

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("ITERATIVNO Broj parnih elemenata je: ", count_iter(lst, predikat))

print("REKURZIVNO Broj parnih elemenata je: ", count_rek(lst, predikat))