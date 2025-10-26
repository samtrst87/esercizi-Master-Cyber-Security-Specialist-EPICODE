#Scrivere un programma in Python che genera un nome per una band musicale utilizzando due input forniti dall'utente:
# la città di origine e il nome del proprio animale domestico.

print("\nBenvenuti al generatore di nomi di band")
citta = input("inserisci il nome della citta di origine: ")
animale = input("inserisci il nome del tuo animale domestico: ")
band = citta + " " + animale
print("\nil nome ideale per la tua band e: ", band)
print("\nVisto il nome!! per l'amor del cielo!!! non suonare metal!!!")


# nel esercizio si evince dal esempio che ce uno spazio vuoto generato tra i due nomi che deve comparire nel risultato inseriti i due nomi
# [ stato aggiunto + " " alla variabile band per questo motivo