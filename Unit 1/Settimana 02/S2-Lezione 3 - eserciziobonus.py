# Traccia: Si scriva i seguenti programmi in Python: 
# Esercizio 1: Calcolo della media mobile.
# Scrivi una funzione che calcoli la media mobile di una lista di numeri.
# La media mobile di un elemento è definita come la media degli ultimi n elementi della lista, inclusi l'elemento corrente.
# 
# Suggerimenti: 
# ● Usa slicing per ottenere gli ultimi n elementi. 
# ● Usa la funzione sum() per calcolare la somma degli elementi e poi dividi per n. 
# 
# Esempio di input:
# numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# n = 3 

# Esempio di output: 
# [1, 1.5, 2, 3, 4, 5, 6, 7, 8, 9]

#esercizio 2
#Scrivi una funzione che analizzi una stringa di testo e restituisca un dizionario con il conteggio delle occorrenze di ciascuna parola.
#Ignora la punteggiatura e considera le parole in modo case-insensitive

def media_mobile():
    n_num = int(input("Calcolo della media mobile\nQuanti numeri vuoi inseri nella lista? (almeno 5): "))
    if n_num <= 4:
        print("hai inserito troppi pochi elementi")
    else:
        listanumeri = []
        selezionato = 0

        for numero in range(n_num):
            numeroinput = (int(input("inserisci un numero nella lista: ")))
            listanumeri.append(numeroinput)
        print(listanumeri)
        numero_media = int(input("inserisci il numero di elementi da tenere in considerazione per la media mobile: "))
        if n_num < numero_media and numero_media > 1:
            print("\n ***ERRORE*** numero invalido, il numero degli elementi da considerare per fare la media non puo' essere superiore o uguale algli elementi presenti nella lista")
        else:
            elemento = int(input("digita il numero del elemento della lista da selezionare: "))
            selezionato = listanumeri[elemento-1]
            considerazione = listanumeri[-1:-numero_media:1]
            print("selezionato", selezionato)
            print("considerzione", considerazione)
            risultato = (selezionato) + float(considerazione)/numero_media
            print(risultato)

def conta_parole(): #funzione del esercizio 2
    caratteri_validi = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    testo_spulciato = ""
    testo_scartato = ""
    def lista_dastringa(testo):
        risultato = testo.split()
        return risultato

    parole = input("inserisci il testo da scomporre in parole per poi contarle: ")
    parole_low = parole.lower()
    for c in parole_low:
        if c not in caratteri_validi:
            testo_scartato += c
        else:    
            testo_spulciato += c

    lista = lista_dastringa(testo_spulciato)

    dizionario = {} # creiamo un dizionario per ospitare il conteggio delle parole nel valore chiave
    for parola in lista:          # per ogni parola della lista
        if parola in dizionario:    #se la parola  e' nel dizionario
            dizionario[parola] += 1 #imposto il valore della chiave della parola del dizionario "aumenta di 1"
        else:
            dizionario[parola] = 1  #altrimenti imposta il valore della chiave della parola del dizionario a 1, difatto "creandola" dichiarando e inizializzando l-elemento
    print(dizionario)
    return dizionario

while True:
    try:        
        scelta = int(input("\nscegliere tra esercizio 1 e 2: "))
        if scelta == 1:
            media_mobile()

        elif scelta == 2:
            conta_parole()   
            
        else:
            print("errore")

    except:
        print("errore catasfericoloso! grida aiuto tre volte per sbloccare")
        time.spleep(5) # test pausa suspence

