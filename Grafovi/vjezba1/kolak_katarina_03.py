def isPrime(number):
    if number <= 1:
        return 0
    for i in range(2, number):
        if number % i == 0:
            return 0   
    return 1    
