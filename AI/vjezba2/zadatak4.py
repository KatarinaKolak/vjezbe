def merge(lsta, lstb):
    if len(lsta) == 0 and len(lstb) == 0:
        return []
    
    if len(lsta) == 0:
        return [ lstb[0] ] + merge(lsta, lstb[1:])
    elif len(lstb) == 0:
        return [ lsta[0] ] + merge(lsta[1:], lstb)
    elif lsta[0] < lstb[0]:
        return [ lsta[0] ] + merge(lsta[1:], lstb)
    else:
        return [ lstb[0] ] + merge(lsta, lstb[1:])
    
lsta = [1, 3, 5, 7]
lstb = [2, 4, 6]
print(merge(lsta, lstb))
