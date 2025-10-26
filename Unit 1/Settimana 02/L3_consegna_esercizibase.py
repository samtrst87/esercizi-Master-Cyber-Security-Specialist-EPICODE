
print("\nBenvenuto alla consegna esercizi base (l3), seleziona da 1 a 6 l'esercizio desiderato: ")
print("\nEsercizio 1: Numero pari o dispari. Scrivi un programma che chieda un numero all'utente e determini se è pari o dispari.")
print("\nEsercizio 2: Calcolo della media. Scrivi un programma che chieda tre numeri all'utente e calcoli la loro media.")
print("\nEsercizio 3: Tabellina di un numero. Scrivi un programma che chieda un numero all'utente e stampi la sua tabellina fino a 10.")
print("\nEsercizio 4: Contare vocali in una stringa. Scrivi un programma che chieda una stringa e conti il numero di vocali presenti.")
print("\nEsercizio 5: Trova il massimo in una lista. Scrivi un programma che chieda all'utente una lista di numeri e trovi il massimo..")
print("\nEsercizio 6: Invertire una stringa. Scrivi un programma che chieda una stringa e la stampi al contrario. ")

while True:
 
    comando = int(input("\ninserisci il numero del esercizio (1-6, 0 per uscire): "))
 
    if comando == 1:
        numero = int(input("inserisci un numero per determinare se il numero sara pari o dispari: "))
        if numero % 2 == 0:
            print(f"il numero {numero} e pari")
        else:
            print(f"il numero {numero} e dispari")
    elif comando == 2:
        print("\nCalcolo della media tra tre numeri")
        media = (int(input("inserisci il primo numero: "))+int(input("inserisci il secondo numero: "))+int(input("inserisci il terzo numero: ")))/3
        print("\nLa media tra i tre numeri e: ", media)
    elif comando == 3:
        numero = int(input("\nInserisci un numero per avere la sua tabellina: "))
        for i in range(1,11,1):  # uso star stop step !!
            risultato = numero * i
            # print(f"\n{numero}*{i}={risultato}")
            print(risultato)
    elif comando == 4:  
        parola = input("\nInserisci una parola per contare il numero di vocali: ")
        # vocali = parola.count("a") + parola.count("e") + parola.count("i") + parola.count("o") + parola.count("u")
        # print(vocali)
        a = parola.count("a")
        e = parola.count("e")
        i = parola.count("i")
        o = parola.count("o")
        u = parola.count("u")
        print(f"Le vocali nella stringa sono {a+e+i+o+u}, {a} lettere A, {e} lettere E, {i} lettere I, {o} lettere O, {u} lettere U")
    elif comando == 5:
        lista = []
        maggiore = 0 ## variabile che conterra' il numero maggiore momentaneo da confrontare con il successivo
        n = int(input("Trova il numero maggiore in una lista, quanti numeri vuoi inserire?: \n"))
        for i in range(n):  ##il metodo append inserisce solo un parametro, quindi sono obbligato ad usare un ciclo per inserire i numeri nella lista in questa caso
            num = float(input("Inserisci un numero: "))
            lista.append(num)
            if num > maggiore and num != 0:
                maggiore = num
        print(f"Tra {lista}, il numero maggiore e': {maggiore}")
    elif comando == 6:
        # testo = input("inserisci del testo per invertirlo: ")
        # invertito = testo[::-1]    ## usiamo lo step in negativo per invertire la posizione delle lettere della stringa
        # print(invertito)
        def inverti_testo(t):
            return t[::-1]
        testoinvertito = inverti_testo(input("\ninserisci il testo da invertire: "))
        print(testoinvertito)
    elif comando == 0:
        break
    else:
        print("scelta invalida, seleziona una opzione dal elenco")