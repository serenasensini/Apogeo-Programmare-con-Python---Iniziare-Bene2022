# parola = "tigreeeeeee"
#
# # per ogni carattere della stringa..
# # se il carattere è una vocale, allora stampo un messaggio
# # altrimenti vado avanti
#
# for carattere in parola:
#     if carattere == 'a' or carattere == 'e' or carattere == 'i' or carattere == 'o' or carattere == 'u':
#         print("è una vocale")
#
# # per ogni posizione che va da zero (quindi dal primo carattere) fino alla fine della parola...
# for posizione in range(0, len(parola)):
#     if parola[posizione] == 'a' or parola[posizione] == 'e' or parola[posizione] == 'i' or parola[posizione] == 'o' or parola[posizione] == 'u':
#         print("è una vocale")
#
# # verificare se il secondo, terzo o quarto carattere della stringa è una vocale
# for carattere in parola[1:3]:
#     if carattere == 'a' or carattere == 'e' or carattere == 'i' or carattere == 'o' or carattere == 'u':
#         print("è una vocale")


# funzione somma

# a = 3
# b = 4
#
# risultato = a + b
# print(risultato)
#
# # def NOME_FUNZIONE(PARAMETRI):
# #      CORPO DELLA FUNZIONE
#
# def somma(x, y):
#     risultato = x + y
#     print(risultato)
#
# print("testo")
#
# somma(5,7)

# SCRIVERE UNA FUNZIONE CHE STAMPI I NUMERI PARI IN UN ARRAY

# lista = [4, 6, 7, 2, 9]
#
# def pari(elenco):
#     for numero in elenco:
#         if numero % 2 == 0:
#             print(numero)
#             # print("è pari")
#
# pari(lista)

# SOLUZIONE N.1

# limite = int(input("Inserisci il limite superiore"))
#
# somma = 0

'''
0+1=1
1+2=3
...
1=0+1
3=1+2
...
risultato = 0
1=risultato+1
3=risultato+2
...
risultato = 0
risultato=risultato+1
risultato=risultato+2
'''


# for numero in range(0, limite, 1):
#     # somma = somma + numero
#     somma += numero
#
# print(somma)

# SOLUZIONE N.3

# raggio = 4
#
# pi_greco = 3.14
#
# area = raggio * raggio * pi_greco
# print(area)

# def circonferenza(raggio):
#     pi_greco = 3.14
#     risultato = 2 * pi_greco * raggio
#     return risultato
#
#
# print(circonferenza(10))
#
#
# def area_cerchio(raggio):
#     pi_greco = 3.14
#     area = pi_greco * (raggio ** 2)
#     return area
#
#
# print(area_cerchio(10))

# SOLUZIONE N.6

'''
 ****                                                                   
 *   *                                                                  
 *   *                                                                  
 ****                                                                   
 *                                                                      
 *                                                                      
 *  
'''

# print("****")
# print("*   *")
# print("*   *")
# print("****")
# print("*")
# print("*")
# print("*")


# SOLUZIONE N.4
# import random
#
# # estrae un numero intero casuale tra 1 e 8
# answers = random.randint(1, 8)
#
# # STEP 1: chiedi all'utente di inserire una domanda per la palla magica
#
# domanda = input("Cosa vuoi chiedere alla palla magica? ")
#
# # STEP 2: tramite le istruzioni condizionali, scrivi delle possibili risposte per l'utente
#
# while domanda != "exit" or domanda != "":
#     if answers == 1:
#         print("Meglio non dirlo ora.")
#     elif answers == 2:
#         print("Ne sei sicuro?")
#     elif answers == 3:
#         print("Direi proprio di sì.")
#     elif answers == 4:
#         print("La mia risposta è no.")
#     elif answers == 5:
#         print("Chiedimelo più tardi.")
#     elif answers == 6:
#         print("Dovresti rifletterci di più.")
#     elif answers == 7:
#         print("Ci puoi contare.")
#     else:
#         print("Le mie fonti dicono di sì.")
#     domanda = input("Cosa vuoi chiedere alla palla magica? ")
#     answers = random.randint(1, 8)


# diz = {"Marco": 1234, "Alessio": 4567, "Claudio": 7894}
# print(diz)
#
# del diz['Marco']
# print(diz)
#
# lista = [1,2,3,4,5]
# del lista[5]
# print(lista)

fruits = {"apple", "banana", "cherry"}

fruits.add("pear")
fruits.add("pear")
fruits.add("pear")

print(fruits)

fruits.remove("pear")

print(fruits)
