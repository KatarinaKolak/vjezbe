from kolak_katarina_03 import isPrime

def findSum(number):
    for i in range(2, number):
        if isPrime(i) == 1 and isPrime(number - i):
            print(i, "+", number - i)
       
    
def main():
    number = int(input("Unesite paran broj n:"))
    while (number % 2 != 0):
        number = int(input("Unesite paran broj n:"))
    
    findSum(number)
   
    
if __name__ == "__main__":
    main()
    

