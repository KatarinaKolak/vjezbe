import random
import time

def generateList():
    lst = []
    floor = int(input("Input number of elements:"))
    for i in range (floor):
        l = random.randint(1, 20)
        h = random.randint(1, 20)
        r = random.randint(l+1, 30)
        lst.append((l, h, r))
    lst.sort()
    return lst

def general(prevBuilding, nextBuilding):  # opceniti slucaj kad je sljedeca zgrada veca od prethodne 
    return nextBuilding[1] > prevBuilding[1] and nextBuilding[0] > prevBuilding[0]

# (lst[i][2] - lst[i][0]) > (lst[i + 2][2] - lst[i + 2][0]
    
def nextBuilding(lst, i): # ako ima zgrada cija se duzina proteze kroz druge 
    return lst[i] if lst[i][1] > lst[i + 1][1] and lst[i + 1][1] < lst[i + 2][1] and lst[i + 2][0] - lst[i][2] > 0 else 0
        
def prevBuilding(lst, i):  # trazi ima li neka zgrada vece duljine prije trenutne zgrade 
    for j in range(i-1, 0, -1):
        if lst[j][2] > lst[i][2]:
            return lst[j]
    return 0

def checkLast(lst):
    return ((lst[len(lst) - 1][2], 0)) if prevBuilding(lst, len(lst) - 1) == 0 else ((prevBuilding(lst, len(lst) - 1)[2], 0))  #za zadnji element 
        
        
def findOutlines(lst):
    outlineList = []
    
    outlineList.append(((lst[0])[0], (lst[0])[1]))  # prvi element 
    
    for building in range (len(lst)-1):
        if general(lst[building], lst[building + 1]) and outlineList[len(outlineList) - 1][1] < lst[building + 1][1]:
            outlineList.append((lst[building + 1][0], lst[building + 1][1]))
            
        elif building + 2 < len(lst) - 1 and nextBuilding(lst, building) != 0:
            outlineList.append(((nextBuilding(lst, building)[2], lst[building + 1][1])))
            
        elif prevBuilding(lst, building) != 0:  # prekalapanje sa prethodnim 
             outlineList.append((lst[building][2], prevBuilding(lst, building)[1]))
             outlineList.append((lst[building + 1][0], lst[building + 1][1]))
             
        elif lst[building + 1][0] > lst[building][2]:  #slucaj sa nulom
            outlineList.append((lst[building][2], 0))
            outlineList.append((lst[building + 1][0], lst[building + 1][1]))
     
    outlineList.append(checkLast(lst))
    
    return outlineList

def main():
    lst = generateList()
    print(lst)
    #lst = [(1,11,5), (2,6,7), (3,13,9), (12,7,16), (14,3,25), (19,18,22), (23,13,29), (24,4,28)]
    start = time.perf_counter()
    print(findOutlines(lst))
    stop = time.perf_counter()
    
    print()
    print("Time:", stop - start)


#lst = [(1,11,5), (2,6,7), (3,13,9), (12,7,16), (14,3,25), (19,18,22), (23,13,29), (24,4,28)]
#output ((1,11), (3,13), (9,0), (12,7), (16,3), (9,18), (22,3),(23,13), (29,0))
    
if __name__=='__main__':
    main()