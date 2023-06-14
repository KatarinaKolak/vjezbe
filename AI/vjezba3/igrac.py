import random

class Igrac:
    def __init__(self, ime):
        self.ime = ime
        self.stanje = {}
        
    def __str__(self):
        return self.ime
    
    # vraca odluku agenta tj indeks karte u ruci, nasumice se odabire 
    def akcija(self, stanje):
        mogucnosti = self.stanje["ruka"] # karte u ruci
        odabir = random.randint(0, len(mogucnosti)) # nasumicni odabir
        
        stanje["stol"].append(mogucnosti[odabir]) # baca na stol
        
        return mogucnosti[odabir] # indeks ili karata??
    
        
        