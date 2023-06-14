def generate_list(lst, sum_element = 0):
    if len(lst) == 0:
        return [ sum_element ]
    
    return generate_list(lst[1:], sum_element + lst[0]) + generate_list(lst[1:], sum_element + (0 - lst[0]))
    
def check_list(lst):
    if len(lst) == 0:
        return False
    
    return True if lst[0] == 0 else check_list(lst[1:])

def is_zero(lst):
    return True if check_list(generate_list(lst)) else False
    

lst = [ 1, 4, 5, 2, 4 ]
print(is_zero(lst))