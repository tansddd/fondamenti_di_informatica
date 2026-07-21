# Analisi Dati in Python - Fondamenti di Informatica

Progetto sviluppato in Python in ambiente VS Code per il corso di Fondamenti di Informatica (Laurea Magistrale in Data Science, Calcolo Scientifico e AI).

L'obiettivo e la risoluzione di tre quesiti di analisi dati (A2, B3 e C1) elaborando set di dati in formato CSV **senza l'utilizzo di librerie esterne**.

## Gestione dei Dati e Codice

* Parsing personalizzato (funzione divisione): Implementato un parser ad hoc per gestire i file CSV in codifica latin-1. L'algoritmo separa correttamente i dati ignorando le virgole presenti all'interno di stringhe racchiuse tra virgolette doppie.
* Pre-processing e Pulizia (funzione riempimento_file): Funzioni dedicate per filtrare i dati irrilevanti, gestire variabili fisse (es. piattaforme implicite) e generare file di output intermedi formattati.
* Strutture Dati: Utilizzo strategico di dizionari (anche con chiavi composte), liste e set per aggregare, sommare e analizzare le informazioni in modo efficiente.

## Sintesi dei Quesiti Risolti

* Quesito A2: Generazione di un dataset unificato (giochi_EU_JP.csv) e calcolo del gioco piu venduto in Europa e Giappone tramite aggregazione delle vendite multi-piattaforma.
* Quesito B3:
1. Identificazione del genere di gioco con il maggior volume di vendite in Nord America.
2. Individuazione dello sviluppatore con il maggior numero di titoli pubblicati.


* Quesito C1: Analisi temporale della diversita dei generi pubblicati per anno, identificando l'anno con la maggiore varieta di generi.

## Complessita Algoritmica

* Complessita Temporale: **O(N) (Lineare)**.
* I cicli di elaborazione sono sequenziali. Il parsing della singola riga analizza una lunghezza di caratteri limitata e costante, garantendo un'efficienza O(N) sia nel caso medio che nel caso pessimo rispetto al numero totale di record.
