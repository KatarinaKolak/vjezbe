from Stick import Stick

def minimax(game):
    if game.game_over() == "Human":
        return 100, 0  
    elif game.game_over() == "Computer":
        return -100, 0  
        
    if game.turn == "Human":
        maxi, num = -1000, 0  # min vrijednosti za sljedeci potez
        for number in game.get_options():
            game.move(number)
            vmax = minimax(game)[0]
            game.undo(number)
            
            if vmax > maxi:
                maxi, num = vmax, number
                
        return maxi, num  # vratimo i broj stapica (1 ili 2)
    else:
        mini, num = 1000, 0
        for number in game.get_options():
            game.move(number)
            vmin = minimax(game)[0]
            game.undo(number)
            
            if vmin < mini:
                mini, num = vmin, number
                
        return mini, num

if __name__ == "__main__" :
    game = Stick()
    while game.game_over() == "play":
        print("Sticks number: ", game.get_sticks(), "\n")
        
        if game.turn=="Human":
            m = int(input("Enter 1 or 2 sticks: "))
            
            while m not in game.get_options():
                m=int(input("Enter 1 or 2 sticks: "))
            
            #if game.check_sticks_and_num(m) != "play":
                #break
            
            print("Player choice:",m)
            
        else:
            v, m = minimax(game)
            #if game.check_sticks_and_num(m) != "play":
                #break
            
            print("Computer choice:", m, "\n")
            
        game.move(m)
    print()
    
    print(game.__str__())

    