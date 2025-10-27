d = {"marca":"fender", "modello":"telecaster", "prezzo": 1000}
d2 = {"marca":"ibanez"}
d3 = {}
print(d)

d["modello"] = "strato"
print(d)

d["anno"] = 2010
print(d)

print(dir(d))

print(d["prezzo"])
print(d.get("prezzo"))
primoprezzo = d.get("prezzo")
primoprezzo = primoprezzo + 1
print(primoprezzo)
marche = [d.get("marca")+" "+d2.get("marca")]
d3.setdefault("condizioni", "pessime")
print(marche)
print(d3)
d3.clear()
print(d3)

l = [1, 2, 3]
m = l.copy()
print(type(l))
print(l)
l.clear()
print(l)
del l
# print(l)
print(m)

# il metodo pop rimuove la coppia chiave valore passata in argomento, restituisce il valore della chiave eliminata
# il metodo.popitem elimina l'ultima coppia chiave valore
# d1 = {}
# d2 = {}
# d1.update(d2) FA UN MERGE dei 2 dizionari


d = {"marca":"fender", "modello":"telecaster", "prezzo": 1000}
print(d)
d["stao"] = "pessimo"
print(d.values())
print(d.keys())
e = [d.keys()]
print(e)
d = {"marca":"fender", "modello":"telecaster", "prezzo": 1000}
for coppia in d.items():
    print(coppia)

for key, value in d.items():
    print(key)
    print(value)