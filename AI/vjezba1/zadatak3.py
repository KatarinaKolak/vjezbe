from random import randint

rand_num = randint(0,1000)
print(rand_num)

while True:
    guess_num = int(input("Enter number:"))
    
    if rand_num == guess_num:
        print("Pogodak")
        break
    
    print("Veci") if rand_num > guess_num else print("Manji")
    

    
