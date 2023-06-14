def check(a, b, c):
    if a**2 + b**2 == c**2:
        return 1
    else:
        return 0
    
while True:
    a = int(input("Unesite prvi broj:"))
    b = int(input("Unesite drugi broj:"))
    c = int(input("Unesite treci broj:"))
    
    if a <= 0 or b <= 0 or c <= 0:
        break
    
    myTuple = sorted((a,b,c))

    if check(myTuple[0], myTuple[1], myTuple[2]) == 1:
        print("Pitagorejski")
    else:
        print("Nije pitagorejski")

        