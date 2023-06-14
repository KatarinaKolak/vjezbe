from copy import deepcopy

class State:
    def __init__(self):
        self.state = list("VOKB || ----")   # V, O, K, B  SVI SU NA LIJEVOJ STRANI
        
    def __str__(self):  #prikaz na ekran ili kljuc u algoritmima
        state_str = ''.join([str(elem) for elem in self.state])  # ispis u string obliku 
        return state_str
    
    def find_char_index(self, char):  # dohvati indeks slova 
        for i in range(len(self.state)):
            if self.state[i] == char:
                return i
            
    def all_actions(self): 
        states = ['V', 'O', 'K', 'B']
        next_actions = []
        
        for char in states:
            if self.find_char_index(char) >= 8 and self.state[-1] == 'B' : # ako je slovo desno 
                next_actions.append(char)
            if self.find_char_index(char) < 4 and self.state[3] == 'B': # ako je slovo lijevo
                next_actions.append(char)
            
        return next_actions
    
    def next_states(self): # proseta kroz stanje i generira novo 
        actions = []
        
        for action in self.all_actions():
            potential_state = self.copy()
            
            potential_state.action(action)
            actions.append(potential_state)
            
        return actions
    
    def is_solved(self):  #True ako je stanje rjesenje zagonetke 
        return True if self.state == list("---- || VOKB") else False  # svi su desno
        
    def is_terminal(self): #True ako je stanje konacno(izgubljeno ili rijeseno) vuk i ovca ili ovca i kupus ne smiju biti na istoj strani
        if self.state == list("VO-- || --KB") or self.state == list("--KB || VO--")  or self.state == list("-OK- || V--B") or self.state == list("V--B || -OK-") or self.state == list("VOK- || ---B"):
            return True 
        else:
            return False
    
    def action(self, char): # primi slovo i napravi akciju za to slovo 
        index = self.find_char_index(char)  # da se moze azurirat stanje preko indeksa 
        self.state[index] = '-'
        
        if index + 8 < len(self.state):
            self.state[index + 8] = char
            self.state[-1] = 'B'
            self.state[3] = '-'
        else:
            self.state[index - 8] = char
            self.state[3] = 'B'
            self.state[-1] = '-'
    
    def undo_action(self, char): #ponistava se akcija i vraca se u stanje prije akcije
        self.action(char)  # nije potreban stack jer znamo koji je prethodni
        return self.state
    
    def copy(self): #vrati kopiju stanja (deepcopy iz copy biblioteke)
        return deepcopy(self)
            
        
if __name__ == '__main__':
    new_object = State()
    print(new_object.state)
    new_object.state = 'VO-- || --KB'
    print(new_object.all_actions())

    '''print("PRIJE: ", new_object.state)
    
    new_object.next_states()
    new_object.action(new_object.all_states[0])
    
    print("POSLIJE: ", new_object.state)
    
    new_object.undo_action()

    print("NAKON UNDA: ", new_object.state)
    
    print(new_object.all_actions())'''
    #for element in new_object.all_states:
     #   print(element)