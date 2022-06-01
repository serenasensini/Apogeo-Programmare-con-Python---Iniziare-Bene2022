# esempio liste

# thislist = ["apple", "banana", "cherry"]
# print("Initial list", thislist)

# thislist.append("strawberry")
# print("Updated list:", thislist)
# print("Index of 'banana: ", thislist.index("banana"))
# print("Index of an unknown element: ", thislist.index("dog"))
# print("Get element with negative index:", thislist[-2])

# new_list = ["mango", "papaya"]
# thislist.extend(new_list)
# print("Updated list:", thislist)

## esercizi n.15

'''
Scrivi un programma che, passata come parametro una
lista di interi, fornisce in output il maggiore tra
i numeri contenuti nella lista.
'''

# lista = [4, 6, 10, 19, 2]
#
# max = 0
#
# # per ogni (for) numero presente nella (in) lista
# for numero in lista:
#     if numero >= max:
#         max = numero
#
# print(max)
#
# lista.sort()
# print(lista)

# tuple

# tupla x
# x = ("apple", "banana", "cherry")
# # trasformo la tupla x in lista y
# y = list(x)
# print(type(y))
# y[1] = "pear"
# y.insert(1, "mango")
# print(y)
# x = tuple(y)
#
# print(x)

# prezzi_frutta = {'mela':1.99, 'pera':2.49, 'uva':2.99, 'mela':2.99}
# print(prezzi_frutta['mela'])

# prezzi_frutta['melone'] = 0.99
# prezzi_frutta['fragole'] = 2.29
# prezzi_frutta['pera'] = 1.99

# del prezzi_frutta['pera']
# print(prezzi_frutta)
# print(len(prezzi_frutta))
#
# prezzi_frutta.update({"'mela'": "2.19"})
#
#
#

## set

# fruits = {"apple", "banana", "cherry"}
# print(fruits)

# fruits = {"apple", "banana", "cherry", "apple"}
# print(fruits)

# fruits.add("pear")

# print(fruits)

# fruits.remove("banana")

# print(fruits)

# Correzione esercizi

# n.1
# nomi = ('Numa', 'Tullio', 'Anco')
# cognomi = ('Pompilio', 'Ostilio', 'Marzio')

# print(nomi)
# print(cognomi)

# n.3

# anagrafica = {"nome": "Giuseppe", "cognome": "Figlia"}
#
# anagrafica["matricola"] = 123456
#
# esame1 = {"nome": "Informatica", "voto": 24}
# esame2 = {"nome": "Analisi I", "voto": 26}
#
# anagrafica["esami"] = [esame1, esame2]
#
# print(anagrafica)
#
# print(anagrafica["esami"][0]["voto"])
#

# def somma(a,b):
#     print(a+b)
#
# somma([2,1])

# SOLUZIONE N.1

# nomi = ("Numa", "Tullio", "Anco")
# cognomi = ("Pompilio", "Ostilio", "Marzio")
#
# nomi_aggiornati = list(nomi)
#
# print(nomi_aggiornati)
#
# # nomi_aggiornati[3] = "Romolo"
# nomi_aggiornati.append("Romolo")
#
# print(nomi_aggiornati)
#
# nomi = tuple(nomi_aggiornati)
#
# print(nomi)
#
# print(cognomi)

# SOLUZIONE n.3

# studente = {"nome": "Alessio", "cognome": "Gava"}
#
# studente["matricola"] = 12345
# # dizionario["matematica"] = 28
# # dizionario["italiano"] = 24
# # dizionario["informatica"] = 18
#
# esami = {"matematica": 28, "italiano": 24, "informatica": 18}
# studente["esami"] = esami
# print(studente)
# # print(esami)
#
# print(studente["esami"])
# print(studente["esami"]["matematica"])
#
# studente["esami"]["informatica"] = 30
#
# print(studente)

# SOLUZIONE N.8

testo = "Contacaratteri"

# {"c":2, "o":1, "n":1, "t":3, "a":3, "r":2, "i":1, "e":1}

# {}
# {"c":1}
# {"c":1, "o":1}
# {"c":1, "o":1, "n":1}
# {"c":1, "o":1, "n":1, "t":1}
# {"c":1, "o":1, "n":1, "t":1, "a":1}
# {"c":1+1, "o":1, "n":1, "t":1, "a":1}
# ...

# conteggio = {}
# for carattere in testo:
#     print("Carattere", carattere)
#     print("Prima del conteggio", conteggio)
#     if carattere in conteggio:
#         conteggio[carattere] = conteggio[carattere] + 1
#     else:
#         conteggio[carattere] = 1
#     print("Dopo il conteggio", conteggio)
#
# print(conteggio)

# SOLUZIONE N.13

stringa = "ciao"
# c i a o
# 0 1 2 3

# for-each == for ... in range...
# for
# while


# def reverse(s):
#     for carattere in range(len(s)-1, -1, -1):
#         print(s[carattere])
#
# reverse(stringa)