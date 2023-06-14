def check_numbers(first, second, flag = True):
    if len(first) == 0:
        return True if flag == True else False
    
    if first[0] not in second:
        flag = False
        
    return check_numbers(first[1:], second, flag)
    
if check_numbers(str(1225) , str(1234)) and check_numbers(str(1225)[::-1], str(1234)):
    print("ISTE SU")
else:
    print("NISU ISTE")
    
    
