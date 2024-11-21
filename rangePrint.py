import os
import time
import subprocess

# Funzione per stampare un'immagine utilizzando GIMP print
def stampa_immagine(nome_file):
    try:
        subprocess.run(["gimp-print", "-P", nome_file], check=True)
        print(f"Stampato con successo: {nome_file}")
    except subprocess.CalledProcessError as e:
        print(f"Errore durante la stampa di {nome_file}: {e}")

# Cartella contenente le immagini da stampare
cartella_immagini = "/percorso/alla/cartella"

# Intervallo di tempo in minuti
intervallo_minuti = 30

# Ciclo infinito per stampare ogni tot minuti
while True:
    # Elenco dei file nella cartella
    elenco_file = os.listdir(cartella_immagini)
    
    # Filtraggio dei file per estensione (puoi modificare questo filtro)
    immagini_da_stampare = [file for file in elenco_file if file.endswith(('.jpg', '.jpeg', '.png'))]
    
    if immagini_da_stampare:
        for immagine in immagini_da_stampare:
            percorso_immagine = os.path.join(cartella_immagini, immagine)
            stampa_immagine(percorso_immagine)
    else:
        print("Nessuna immagine trovata nella cartella.")
    
    time.sleep(intervallo_minuti * 60)  # Converti i minuti in secondi

