def lista_dastringa(testo):
    risultato = testo.split()
    return risultato

def unisci_stringa_dalista(testo):
    risultato = " ".join(testo)
    return risultato


# listaparole = ["Ciao", "questa", "e'", "una", "prova"]
# risultato = "-".join(listaparole)
# # print(f"{risultato}")
# # print(f"{' '.join(listaparole)}")
# print(risultato)

lista = lista_dastringa(input("inserisci il testo da inserire in una lista"))
print(lista)


operazione = unisci_stringa_dalista(lista)
print(operazione)
