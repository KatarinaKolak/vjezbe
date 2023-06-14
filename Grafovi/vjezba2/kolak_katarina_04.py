import collections

def reverseDict(myDict):
    newDict = {}
    keysList = []
    for key, values in myDict.items():
        for element in values:
            if element in newDict.keys():
                newDict[element].append(key)
            else:
                keysList.append(key)
                newDict[element] = keysList
                keysList = []
                
    return collections.OrderedDict(sorted(newDict.items()))

myDict = {1:[2, 3, 5], 2:[1, 4], 3:[1, 2]}
print(reverseDict(myDict))