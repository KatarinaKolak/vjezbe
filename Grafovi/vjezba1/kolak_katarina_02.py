def drawTriangle(n):
    for i in range(n+1):
        for j in range(i * 2 - 1):
            if j < i:
                print((j + i) % 10, end = " ")
            elif i == j:
                print((i + j - 2) % 10, end = " ")
            else:
                print((((i + (j - (j - i)) - 2) % 10) - (j - i)) % 10, end = " ")
        print()
        
        
n = int(input("Unesite n:"))
while n > 20:
    n = int(input("Unesite n:"))
    
drawTriangle(n)