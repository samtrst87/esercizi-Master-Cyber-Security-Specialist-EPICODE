
# 🔹 Operatori logici (per condizioni multiple)
# Operatore	Nome	Esempio
# and	E logico	x > 0 and x < 10
# or	O logico	x < 0 or x > 100
# not	Negazione	not x == 5

# 🔹 Operatori di confronto (per filtrare elementi)
# Operatore	Nome	Esempio
# ==	Uguaglianza	x == 3
# !=	Diverso da	x != 0
# <	Minore di	x < 10
# <=	Minore o uguale a	x <= 10
# >	Maggiore di	x > 0
# >=	Maggiore o uguale a	x >= 0
# in	Presenza in una sequenza	x in [1, 2, 3]
# not in	Assenza in una sequenza	x not in a
# is	Identità (stesso oggetto)	x is y
# is not	Non identico	x is not y

# 🔹 Operatori aritmetici (se vuoi trasformare gli elementi)
# Operatore	Nome	Esempio
# +	Addizione	x + 1
# -	Sottrazione	x - 2
# *	Moltiplicazione	x * 2
# /	Divisione	x / 3
# //	Divisione intera	x // 2
# %	Modulo	x % 2
# **	Potenza	x ** 2



# ✅ Esempi di list comprehension

#     Filtrare numeri pari:

# [x for x in range(10) if x % 2 == 0]

#     Numeri compresi tra 5 e 10:

# [x for x in range(20) if x >= 5 and x <= 10]

#     Numeri non presenti in una lista:

# [x for x in range(10) if x not in [2, 4, 6]]

#     Applicare operazioni:

# [x * 2 for x in range(5)]  # [0, 2, 4, 6, 8]

lista = [[1,2,3],[4,5,6],[7,8,9]]
print("elementi in lista: ", len(lista))

for lista_innestata in lista:
    print(lista_innestata)

for lista_innestata in lista:
    for num in lista_innestata:
        print(num)

l = []
for lista_innestata in lista:
    for num in lista_innestata:
        l.append(num)
        print(l)
l= [num for lista_innestata in lista for num in lista_innestata]
print(l)

n = [num for num in range(0,3)]
print(n)


l = []
l = [[num for num in range(0,3)] for iterazione in range(0,3)]
    
print(l)


nome = "Samuel"
eta = 25
print(f"Ciao {nome}, hai {eta} anni")

from datetime import datetime

data = datetime.now()
print(data)
ora = data.strftime("%H:%M")

print(ora)

print(data.year)     # 2025
print(data.month)    # 7
print(data.day)      # 13
print(data.hour)     # 19
print(data.weekday()) # 0 = lunedì, 6 = domenica
