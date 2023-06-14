def findElements(list1, list2):
    set1 = set(list1)
    set2 = (list2)
    
    
    return list(set1.union(set2))


list1 = [2, 3, 4]
list2 = [3, 4, 5]

print(findElements(list1, list2))