from igrac import Igrac

#naslijediti klasu igrac i override metodu akcija
class Human(Igrac):
    def akcija(self, stanje):
        mogucnosti = self.stanje["ruka"] # karte u ruci igraca
        
        print("Unesite redni broj karte koju zelite baciti: ")
        
        for indeks in range(len(mogucnosti)):
            print(indeks, ": ", mogucnosti[indeks])
            
        odabir = int(input("Vas odabir: "))
        
        stanje["stol"].append(mogucnosti[odabir]) # baca na stol kartu 
        
        return odabir # indeks ili karta??
    