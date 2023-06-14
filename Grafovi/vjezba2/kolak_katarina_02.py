import random

def reverse(players):
    return (players[1], players[0])

def game():
    options = {0:"kamen", 1:"skare", 2:"papir"}
    rules = [(0,1), (1, 2), (2, 0)]
    players = (1, 2)
    resultH = 0
    resultC = 0
    
    end = int(input("Unesite do koliko se igra:"))
    
    while (resultC < end and resultH < end):
        if (players[0] == 1):
            choiceH = int(input("Unesite broj od 0 do 2:(0 je kamen, 1 su skare i 2 papir):"))
            choiceC = random.randint(0,2)
            #print("Racunalo:", choiceC)
        else:
            choiceC = random.randint(0,2)
            #print("Racunalo:", choiceC)
            choiceH = int(input("Unesite broj od 0 do 2:(0 je kamen, 1 su skare i 2 papir):"))
            
        for score in rules:
            if choiceH == score[0] and choiceC == score[1]:
                resultH += 1
                break
            elif choiceC == score[0] and choiceH == score[1]:
                resultC += 1
                break
            else:
                continue
   
        players = reverse(players)
        for key, values in options.items():
            if choiceH == key:
                print("Igrac: ",  values)
            if choiceC == key:
                print("Racunalo: ", values)
        if choiceH not in options.keys() or choiceC not in options.keys():
            print("Mogucnosti su od 0 do 2")
        print("Rezultat je: ", resultH, ":", resultC)
        
    if resultH > resultC:
        print("Pobjednik je igrac")
    else:
        print("Pobjednik je racunalo")
        
game()