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

lista = [4, 6, 7, 2, 9]

def pari(elenco):
    for numero in elenco:
        if numero % 2 == 0:
            print(numero)
            # print("è pari")

pari(lista)