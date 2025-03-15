# Nome e Cognome : Georgi Dimitrov
# Classi utili alla programmazione

class Menu:
    #Classe che è in grado di generare un menu e di prendere un opzione
    def __init__(self):
        #Costruttore: variabili di istanza
        self._opzioni = []
        self._scelta = ''
        self._contatore = 1

    def addOpzione(self,opzione):
        #Prende un'opzione
        self._opzioni.append(str(self._contatore) + '.' + opzione )
        self._contatore +=1

    def inputScelta(self):
        #Prende scelta
        self._scelta = input()
        return self._scelta

    def mostraMenu(self):
        #Mostra il menu
        for elem in self._opzioni :
            print(elem)
        
        
        
        
    
