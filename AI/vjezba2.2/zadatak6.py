def is_zero(lst):
    if sum(lst) == 0:
        return True
    
    result = 0
    
    for index in range(len(lst)):
        
        