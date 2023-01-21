# Nome e Cognome : Georgi Dimitrov
# Data inizio: 09/02/2020
# Programma TNT Village v.Alfa


#_Main Programm
from Grafica import *
from ClassiUtili import *
from Ricerca import *

#Variabili

#Interfaccia iniziale
separatore()
titolo()
separatore()
crediti()
separatore()

#Menu
scelta = MenuProgramma()
while not (scelta.isdecimal() and 0 < int(scelta) <= 4):
    #Controllo errore
    scelta = input("\nERRORE! Scelta inserita non prevvista dal programma!\nInserisci scelta corretta: ")
separatore()    

#Scelta e ricerca
while not scelta == '4':
    if scelta == '1':
        rel = RicercaTitolo()
        VisualizzaRelese(rel)
    elif scelta == '2':
        rel = RicercaCategoria()
        VisualizzaRelese(rel)
    else:
        istruzioni()

    separatore()
    scelta = MenuProgramma()
    while not (0 < int(scelta) <= 4):
        #Controllo errore
        scelta = input("\nERRORE! Scelta inserita non prevvista dal programma!\nInserisci scelta corretta: ")
    separatore()



