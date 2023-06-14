def generate_lst(length, string="", lst = []):
    if len(string) == length:
        lst.append(string)
        return 
    
    generate_lst(length, string + 'A', lst)
    generate_lst(length, string + 'B', lst)
    generate_lst(length, string + 'C', lst)
    
    return lst
    
    
    
print(generate_lst(2))