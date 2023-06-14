def merge(lsta, lstb, new_lst = []):
    if len(lsta) == 0 and len(lstb) == 0:
        return new_lst
    
    if len(lsta) == 0:
        new_lst.append(lstb[0])
        return merge(lsta, lstb[1:], new_lst)
    elif len(lstb) == 0:   
        new_lst.append(lsta[0])
        return merge(lsta[1:], lstb, new_lst)
    elif lsta[0] < lstb[0]:
        new_lst.append(lsta[0])
        return merge(lsta[1:], lstb, new_lst)
    else:            
        new_lst.append(lstb[0])
        return merge(lsta, lstb[1:], new_lst)


lsta = [2, 4, 6, 8]
lstb = [1, 3, 5, 7]
print(merge(lsta, lstb))

