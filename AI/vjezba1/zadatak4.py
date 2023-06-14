from random import randint

guess_number = int(input("Unesite zamisljeni broj:"))
limit = 1000

while True: 
    print("Limit: ", limit)
    computer_choice = randint(1, limit)  
    print("Racunalo bira: ", computer_choice)
    
    if computer_choice < limit:
        limit = computer_choice
    
    if computer_choice == guess_number:
        print("Pogodak")
        break
    
    print("Veci") if guess_number > computer_choice else print("Manji")
    
   