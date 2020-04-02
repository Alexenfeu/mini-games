import random as r

def main():    
    
    coeurCartes = ['1','2','3','4','5','6','7','8','9','10','V','D','R']
    piqueCartes = ['1','2','3','4','5','6','7','8','9','10','V','D','R']
    carreauCartes = ['1','2','3','4','5','6','7','8','9','10','V','D','R']
    trefleCartes = ['1','2','3','4','5','6','7','8','9','10','V','D','R']
    
    def resetCartes(coeurCartes, piqueCartes, carreauCartes, trefleCartes):
        coeurCartes.clear()
        piqueCartes.clear()
        carreauCartes.clear()
        trefleCartes.clear()
        coeurCartes.extend(['1','2','3','4','5','6','7','8','9','10','V','D','R'])
        piqueCartes.extend(['1','2','3','4','5','6','7','8','9','10','V','D','R'])
        carreauCartes.extend(['1','2','3','4','5','6','7','8','9','10','V','D','R'])
        trefleCartes.extend(['1','2','3','4','5','6','7','8','9','10','V','D','R'])
    
    
    
    def tirerCarte(coeurCartes, piqueCartes, carreauCartes, trefleCartes):
        couleur = r.randint(1,4)
        if (couleur == 1):
            index = r.randint(0,len(coeurCartes)-1)
            return coeurCartes.pop(index)
        if (couleur == 2):
            index = r.randint(0,len(piqueCartes)-1)
            return piqueCartes.pop(index)
        if (couleur == 3):
            index = r.randint(0,len(carreauCartes)-1)
            return carreauCartes.pop(index)
        if (couleur == 4):
            index = r.randint(0,len(trefleCartes)-1)
            return trefleCartes.pop(index)
        
    print(tirerCarte(coeurCartes, piqueCartes, carreauCartes, trefleCartes))
    print(coeurCartes)
    print(piqueCartes)
    print(carreauCartes)
    print(trefleCartes)
    resetCartes(coeurCartes, piqueCartes, carreauCartes, trefleCartes)
    print(coeurCartes)
    print(tirerCarte(coeurCartes, piqueCartes, carreauCartes, trefleCartes))

main()
