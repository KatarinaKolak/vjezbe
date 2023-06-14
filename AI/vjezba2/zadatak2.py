def check_string(element, lst):
    if len(lst) == 0:
        return False
    
    if element == lst[0]:
        return True
    
    return check_string(element, lst[1:])

def compare_strings(first, second):
    first = str(first)
    second = str(second)
    
    if len(first) == 0:
        return True
    
    if not check_string(first[0], second):
        return False
        
    return compare(first[1:], second)
    
def compare(first, second):
    if compare_strings(first, second) and compare_strings(second, first):
        return True
    else:
        return False
    
first = 32251 
second = 25923


print(compare(first, second))