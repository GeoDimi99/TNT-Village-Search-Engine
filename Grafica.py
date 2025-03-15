# Nome e Cognome : Georgi Dimitrov
# Programma TNT Village v.Alfa
from ClassiUtili import Menu

#_Grafica

def titolo():
    #Titolo del programma .
    print() 
    print("-------------    -----    ----    -------------")
    print("|           |    |    \   |   |   |            |")
    print("|           |    |     \  |   |   |            |")
    print(" ---      ---    |      \ |   |    ---      ---")
    print("    |     |      |       \|   |       |     |")
    print("    |     |      |   |\       |       |     |")
    print("    |     |      |   | \      |       |     |")
    print("    |     |      |   |  \     |       |     |")
    print("    -------      -----   ------       -------","  VILLAGE")
    print()

def separatore():
    #Un separatore che aiuta nella leggibilità del programma
    print("---------------------------------------------------------------------")

def crediti():
    #Informazioni riguardanti il produttore del software
    print("Proggettista software : \tGeorgi Dimitrov")
    print("Programmatore software: \tGeorgi Dimitrov")
    print("Anno inizio sviluppo:\t\t2020")
    print("Anno fine sviluppo :\t\t2020")
    print("Versione software:\t\t??????")
def istruzioni():
    #Manuale per l'uso dell programma
    print("Salve! Questo programma è stato progettato per rendere la ricerca di\n\
relese più facile e intuitiva.Si ricorda all'utente finale che scaricare\n\
è illegale se non si è in possesso di una copia originale dell'oggetto.\n\
\n\
ISTRUZIONI PER L'USO:\n\
1.Ricerca:\n\
La ricerca di una relese può avvenire essere fatta attraverso i metodi definite\n\
nel menù:\n\
\ta)Inserendo il titolo(preciso!) della relese cercata\n\
\tb)Inserendo tra le seguenti catergorie: \n\
\t\t1  = Film TV e programmi\n\
\t\t2  = Musica\n\
\t\t3  = E Books\n\
\t\t4  = Film\n\
\t\t6  = Linux\n\
\t\t7  = Anime\n\
\t\t8  = Cartoni\n\
\t\t9  = Macintosh\n\
\t\t10 = Windows Software\n\
\t\t11 = Pc Game\n\
\t\t12 = Playstation\n\
\t\t13 = Students Releases\n\
\t\t14 = Documentari\n\
\t\t21 = Video Musicali\n\
\t\t22 = Sport\n\
\t\t23 = Teatro\n\
\t\t24 = Wrestling\n\
\t\t25 = Varie\n\
\t\t26 = Xbox\n\
\t\t27 = Immagini sfondi\n\
\t\t28 = Altri Giochi\n\
\t\t29 = Serie TV\n\
\t\t30 = Fumetteria\n\
\t\t31 = Trash\n\
\t\t32 = Nintendo\n\
\t\t34 = A Book\n\
\t\t35 = Podcast\n\
\t\t36 = Edicola\n\
\t\t37 = Mobilee\n\
Tutte le categorie possono essere ordinate in ordine alfabetico , oppure si può\n\
scegliere se mostrare una detterminata lettera.\n\
\n\
2.Download:\n\
Per poter scaricare l'oggetto scelto bisogna copiare il codice HASH del relativo oggetto\n\
e inserirlo nel proprio client torrent. In oltre per maggiri dettagli sull'oggetto si può\n\
accedere al sito indicato. (ATTENZIONE! Non si puo scaricare dal sito.)")

#Menu
def MenuProgramma():
    #Funzione che genera un menu
    print("MENU:\n")
    menu = Menu()
    menu.addOpzione("RICERCA DAL TITOLO")
    menu.addOpzione("RICERCA PER CATEGORIA")
    menu.addOpzione("ISTRUZIONI")
    menu.addOpzione("ESCI")
    menu.mostraMenu()

    print("\nInserisci scelta: ",end='')
    return menu.inputScelta()

    
    


    
