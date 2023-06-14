from kolak_katarina_03 import isPrime
from kolak_katarina_03a import countPrime
from kolak_katarina_03b import nthPrime
from kolak_katarina_03c import findNumbers
from kolak_katarina_03d import findSum

# parni brojevi u rasponu
start = float(input("Unesite pocetak:"))
stop = float(input("Unesite kraj:"))

print(countPrime(start, stop))

# n-ti parni broj
n = int(input("Unesite n:"))
print(nthPrime(n))

#susjedni prosti do n
n = int(input("Unesite n:"))
print(findNumbers(n))

# zbroj dva parna broja
number = int(input("Unesite paran broj n:"))
while (number % 2 != 0):
    number = int(input("Unesite paran broj n:"))
    
findSum(number)