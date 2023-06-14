from kolak_katarina_03 import isPrime
            
def countPrime(start, stop):
    counter = 0
    for i in range(int(min(start, stop)) + 1, int(max(start, stop)) + 1):
        if (isPrime(i) == 1):
            counter += 1
    return counter


def main():
    start = float(input("Unesite pocetak:"))
    stop = float(input("Unesite kraj:"))

    print(countPrime(start, stop))
    
if __name__ == "__main__":
    main()
    
