from kolak_katarina_03 import isPrime

def nthPrime(n):
    counter = 0
    number = 2
    while True:
        if isPrime(number) == 1 and counter < n:
            counter += 1
        if counter == n:
            return number
        number += 1


def main():
    n = int(input("Unesite n:"))
    print(nthPrime(n))
   
if __name__ == "__main__":
    main()
    
