#esercizio 2
#Scrivi una funzione che analizzi una stringa di testo e restituisca un dizionario con il conteggio delle occorrenze di ciascuna parola.
#Ignora la punteggiatura e considera le parole in modo case-insensitive

def conta_parole(): #funzione del esercizio
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
            print("esercizio1")

        elif scelta == 2:
            conta_parole()
        
        else:
            print("errore")

    except:
        print("inserisci un numero porco cane")
        continue

