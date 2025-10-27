# Si scriva un programma in Python che in base alla scelta dellʼutente permetta di calcolare il perimetro di diverse figure geometriche 
# (scegliete pure quelle che volete voi). Per la risoluzione dellʼesercizio abbiamo scelto: 
# ● Quadrato (perimetro = lato*4
# ● Cerchio (circonferenza = 2*pi greco*r).
# ● Rettangolo (perimetro= base*2 + altezza*2

def perimetro_quadrato(lato):
    risultato= lato * 4
    return risultato

def circonferenza(r):
    risultato = + 2 * 3.14* r
    return risultato

def perimetro_rettangolo(base, altezza):
    risultato = (base*2)+(altezza*2)
    return risultato

while True:
    scelta = int(input("\nScegli l'operazione da effettuare, \n1 per calcolare il Perimetro del Quadrato\n2 per calcolare la Circonferenza del cerchio\n3 per calcolare il Perimetro del Rettangolo\n4 per terminare il programma\n"))

    if scelta == 1:
        print("\nHai selezionato il Perimetro del quadrato")
        lato = float(input("inserisci il valore del lato del quadrato: "))
        risultato = perimetro_quadrato(lato)
        print(f"\nil perimetro del quadrato e': {risultato}")

    elif scelta == 2:
        print("\nHai selezionato il Circonferenza del cerchio")
        r = float(input("inserisci il valore del raggio del cerchio: "))
        risultato = circonferenza(r)
        print(f"\nla circonferenza del cerchio e' : {risultato}")

    elif scelta == 3:
        print("\nHai selezionato il Perimetro del rettangolo")
        base = int(input("\ninserire il valore della base: "))
        altezza = int(input("inserisci il valore dell'altezza"))
        risultato = perimetro_rettangolo(base, altezza)
        print(f"\nil perimetro del rettangolo e': {risultato}")

    elif scelta == 4:
        break

    else:
        print("scelta non valida, ricomincia!")


# ho utilizzato le funzioni anche se non necessarie per allenarmi ad utilizzarle