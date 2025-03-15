## TNT Village Search Engine

## Descrizione del Progetto

Il **TNT Village Search Engine** è un software progettato per cercare release nel database rilasciato pubblicamente dal sito **TNT Village**. Il programma offre un'interfaccia testuale intuitiva, dotata di istruzioni dettagliate per l'uso. Ogni release trovata è associata a un sito web per una breve descrizione e un codice, che può essere utilizzato in un client torrent (come BitTorrent) per scaricare la release desiderata.

## Funzionalità Principali

- Ricerca di release nel database pubblico di TNT Village.
- Interfaccia testuale semplice e intuitiva.
- Collegamento a una breve descrizione della release.
- Generazione di un codice per il download tramite client torrent.

## Setup del Progetto

Per configurare e avviare il progetto, segui questi passaggi:

1. Clona il repository:
   
   ```bash
   git clone https://github.com/GeoDimi99/TNT-Village-Search-Engine.git
   ```

2. Accedi alla cartella del progetto:
   
   ```bash
   cd TNT-Village-Search-Engine/
   ```

3. Scarica il database delle release:
   
   ```bash
   wget https://archive.org/download/dump_release_tntvillage_2019-08-30/dump_release_tntvillage_2019-08-30.zip
   ```

4. Estrai il file ZIP e rimuovi l'archivio:
   
   ```bash
   unzip dump_release_tntvillage_2019-08-30.zip && rm dump_release_tntvillage_2019-08-30.zip
   ```

## Avvio del Programma

Per avviare il programma, esegui il seguente comando:

```bash
python main.py
```



Di seguito sono riportati due screenshot del programma in esecuzione:

![Screenshot 1](C:\Users\dimit\Projects\Personal%20Projects\TNT-Village-Search-Engine\screenshot\screenshot1.jpg)  
*Homepage*

![Screenshot 2](C:\Users\dimit\Projects\Personal%20Projects\TNT-Village-Search-Engine\screenshot\screenshot2.jpg)  
*Search by name option*

## Note

- Assicurati di avere Python installato sul tuo sistema.
- Il database delle release è stato aggiornato al 30 agosto 2019.

## Autore

Il progetto è stato sviluppato da **Georgi Dimitrov**.  
Per ulteriori informazioni, visita il repository su GitHub: [TNT-Village-Search-Engine](https://github.com/GeoDimi99/TNT-Village-Search-Engine).

# 
