
# Nome e Cognome: Georgi Dimitrov
#Funzioni di ricerca
#TNT Village

from Grafica import separatore
from ClassiUtili import Menu
import re

def RicercaCategoria():
    categoria = input("Scegli categoria: ")
    while not (categoria.isdecimal() and 0 < int(categoria) <= 37):
        #Controllo della scelta
        categoria = input("ERRORE! Scelta categoria non prevvista dal programma.\nInserisci la categoria nel formato descritto nelle istruzioni:")
        
    lista_relese = []
    csv_relese = open('dump_release_tntvillage_2019-08-30/dump_release_tntvillage_2019-08-30.csv','r',encoding = 'utf-8')
    csv_relese.readline()
    print("Quale metodo preferisci per cercare la tua relese?")
    ordine = input("\n1.In ordine alfabetico\n2.Scelta una di una lettera\n\nInserisci scelta: ")
    while ordine not in '12':
        #Controllo della scelta del metodo di ricerca
        ordine = input("\nERRORE! Scelta non prevvista!\nDigita nuovamente la scelta: ")
    if ordine == '2':
        lettera = input("Inserisci lettera[A-Z]: ")
        while lettera.upper() not in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            #Controllo lettera
            lettera = input("ERRORE!Non hai inserito una lettera.\nPer favore inserisci una lettera: ")
        
        for relese in  csv_relese:
            #Ciclo su tutte le relese 
            relese = relese.strip().split(',')
            titolo = relese[5]
            if relese[8] == categoria and titolo[1] == lettera.upper():
                #Filtro per la categoria e la lettera
                lista_relese.append(relese)
    else:
        for relese in  csv_relese:
            #Ciclo su tutte le relese 
            relese = relese.strip().split(',')
            if relese[8] == categoria:
                lista_relese.append(relese)
    csv_relese.close()
    print("\n")
    separatore()
    return OrdinamentoAlfabetico(lista_relese)

def RicercaTitolo():
    lista_relese = []
    nome_relese = input("Inserisci il nome della relese: ")
    nome_relese = nome_relese.strip().split()
    csv_relese = open('dump_release_tntvillage_2019-08-30/dump_release_tntvillage_2019-08-30.csv','r',encoding = 'utf-8')
    pattern = '.*'
    for parole in nome_relese:
        pattern += parole + '.*'
    for relese in csv_relese:
        relese = relese.strip().split(',')
        trovato = re.search(pattern , relese[5] , flags = re.IGNORECASE ) # Serve per cercare con l'oggetto inserito in input fa parte di un titolo
        if trovato:
            #Se appartiene a un titolo inserirlo in una lista
            lista_relese.append(relese)
    csv_relese.close()
    return OrdinamentoAlfabetico(lista_relese)

def VisualizzaRelese(lista):
    #Funzione che fa visualizzare le relese
    indice = 0
    fine = 20
    risposta = 'SI'
    while risposta.upper() == 'SI':
        while indice < fine and indice < len(lista):
            titolo = lista[indice][5]
            sito = 'https://web.archive.org/web/http://forum.tntvillage.scambioetico.org/index.php?showtopic=' + lista[indice][2]
            HASH = lista[indice][1]
            autore = lista[indice][4]
            cat = lista[indice][8]
            print("Titolo: ",titolo)
            print("Sito descrizione: ",sito)
            print("Autore: ",autore)
            print("HASH: ",HASH)
            print("Categoria: ",cat)
            indice += 1
            separatore()
        if indice < len(lista)-1:
            risposta = input("Vuoi proseguire alle prossime relese?\nRisposta[SI/NO]: ")
            while not (risposta.upper() == 'SI' or risposta.upper() == 'NO'):
                risposta = input("\nERRORE!\nPer favore digitare la risposta bene: ")
            fine +=20
            separatore()
            separatore()
            separatore()
        else:
            risposta = 'NO'



def OrdinamentoAlfabetico(matrice):
    for i in range(len(matrice)):
        for j in range(i+1,len(matrice)):
            if matrice[i][5] > matrice[j][5]:
                riga= matrice[i].copy()
                matrice[i] = matrice[j].copy()
                matrice[j] = riga.copy()
    return matrice

                
                




        
        
        
        
    
