from kolak_katarina_03 import isPrime

def findNumbers(n):
    primeList = []
    
    for i in range(2, n):
        for j in range(i + 1, n):
            if isPrime(i) == 1 and isPrime(j) == 1 and j - i == 2:
                primeList.append((i,j))
                print(i, j)
    return primeList
        
        

def main():
    n = int(input("Unesite n:"))
    print(findNumbers(n))
  
if __name__ == "__main__":
    main()
