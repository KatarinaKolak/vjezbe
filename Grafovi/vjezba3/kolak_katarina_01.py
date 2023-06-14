def findSum(lst):
    newList = [int(element) for element in lst if element.isnumeric() or '-' in element or '\n' in element]
    return sum(newList)

def sumMatrix():
    sumList = []
    with open("matrica.txt",'r') as f:
        for line in f:
            line = line.split(' ')
            sumList.append(findSum(line))
    return sumList

def main():
    print(sumMatrix())
    

if __name__=='__main__':
    main()