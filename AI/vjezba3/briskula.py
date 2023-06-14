from igrac import Igrac 
import karte
    
class Briskula:
    def __init__(self, igrac1 = Igrac("igrac1"), igrac2 = Igrac("igrac2")):
        self.igrac1 = igrac1  # igra prvi
        self.igrac2 = igrac2
        
        self.bodovi = {1: 11, 3: 10, 2: 0, 4: 0, 5: 0, 6: 0, 7: 0, 11: 2, 12: 3, 13: 4} # bod svake karte 
        #self.snaga = {1: 11, 3: 10, 2: 0, 4: 0, 5: 0, 6: 0, 7: 0, 11: 2, 12: 3, 13: 4} # snaga broja karte 
        self.stanje_igre = {} # stanje igre
        
    # ispisuje stanje igre: broj karata u spilu, briskulu, karte na stolu i karte u rukama igraca
    def __str__(self):
        for key, values in self.stanje_igre.items():
            print(key, ": ", values)
            
    # vraca stanje za metodu akcija svakog agenta
    def stanje(self):
        return self.stanje_igre
    
    def vrati_vrijednost(self):
        for broj, bod in self.bodovi.items():
            if self.broj == broj:
                return bod
    
    # za konacno stanje partije vrati: 1 igrac1 je pobjedio, 2 igrac2 je pobjedio ili 0 nerjeseno
    #def rezultat(self):   ?????????
    
    # odigraj ruku odigraju mehanike igre pitajuci igraca za akciju
    def odigraj_ruku(self):
        odabir1 = self.igrac1.akcija(self.stanje) # odreduje zog ruke
        odabir2 = self.igrac2.akcija(self.stanje)
        
        if odabir2.zog != self.stanje_igre["briskula"] and odabir2.zog != odabir1.zog:
            self.igrac1.stanje["dobivene"].append(odabir1)
            self.igrac1.stanje["dobivene"].append(odabir2)
            
        elif odabir2.zog == odabir1.zog:
            if odabir1.vrijednost() > odabir2.vrijednost():
                self.igrac1.stanje["dobivene"].append(odabir1)
                self.igrac1.stanje["dobivene"].append(odabir2)
            else:
                self.igrac2.stanje["dobivene"].append(odabir1)
                self.igrac2.stanje["dobivene"].append(odabir2)
                
        elif odabir2.zog == self.stanje_igre["briskula"]:
            self.igrac2.stanje["dobivene"].append(odabir1)
            self.igrac2.stanje["dobivene"].append(odabir2)
        
        
    # odigraj partiju odigraju mehanike igre pitajuci igraca za akciju
    def odigraj_partiju(self):
        spil = karte.Spil()
        print(spil)
        
        self.stanje_igre["briskula"] = spil.sjeci().zog
        
        for i in range(3): # peskaju 3 karte 
            self.igrac1.stanje["ruka"].append(spil.peskaj())
            self.igrac2.stanje["ruka"].append(spil.peskaj())
    
        self.stanje_igre["briskula"] = spil.karte[34]
        spil.karte[34], spil.karte[0] = spil.karte[0], spil.karte[34]
        
        while spil:
            self.odigraj_ruku()
            
            self.igrac1.stanje["ruka"].append(spil.peskaj())
            self.igrac2.stanje["ruka"].append(spil.peskaj())
        
        
    
        
        
    