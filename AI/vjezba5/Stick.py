class Stick:
    def __init__(self):
        self.sticks = 11
        self.turn = "Human"
        self.options = [1, 2]
        
    def __str__(self):
        return "Sticks number: " + str(self.sticks) + " Winner: " + self.get_winner() + " Loser: " + self.get_loser()
    
    def get_turn(self):
        self.turn
        
    def get_options(self):
        return self.options
    
    def get_sticks(self):
        return self.sticks
    
    def move(self, number):
        self.sticks -= number
        self.turn = "Computer" if self.turn == "Human" else "Human"
    
    def undo(self, number):
        self.sticks += number
        self.turn = "Computer" if self.turn == "Human" else "Human"
        
    def get_loser(self):
        return "Computer" if self.turn == "Computer" else "Human" 
    
    def get_winner(self):
        return "Human" if self.turn == "Computer" else "Computer" 
    
    def game_over(self):
        if self.sticks < 0:
            return self.turn
        elif self.sticks == 0:
            return self.turn
        elif self.sticks < 2:  # ako je manje od 2 stapica  
            return "Human" if self.turn == "Computer" else "Computer" 
        
        return "play"
    
    '''
    def check_sticks_and_num(self, num):
        if num > self.get_sticks():
            print("Game over!")
            #self.turn = "Computer" if game.turn == "Human" else "Computer" 
            return self.turn
        elif num == self.get_sticks():
            print("FINISH")
            self.turn = "Computer" if self.turn == "Human" else "Computer" 
            return self.turn
        
        return "play"    
    '''
    
    