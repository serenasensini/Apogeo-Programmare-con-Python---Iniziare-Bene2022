# Usa questo file per testare il tuo codice!
'''
numero = 0



if numero == 0:
    print("Il numero è uguale a 0.")
elif numero < 0 and numero % 2 == 0:
    print("Il numero è negativo e pari.")
elif numero % 2 != 0 and numero < 0:
    print("Il numero è dispari e negativo.")
elif numero > 0 and numero % 2 == 0:
    print("Il numero è pari e positivo")
else:
    print("Il numero è positivo e dispari.")

'''






# testo = "CIAO21212"
#
# if testo.islower():
#     print("Il testo è tutto minuscolo")
# elif testo.isupper():
#     print("Il testo è tutto maiuscolo")
# else:
#     print("Il testo è misto.")





#
# numero = 49
#
# if numero % 7 == 0 and numero % 5 != 0:
#     print("La condizione è soddisfatta")
# else:
#     print("La condizione non è soddisfatta")



# x = 1
#
# if x < 0:
#     print("numero negativo")
# elif x % 2 != 0:
#     print("numero dispari")
# elif x % 2 == 0:
#     print("numero pari")

# start_number = 10
# per ogni numero i nell'intervallo (0, start_number, +1)
# forma esplicita (start, end, step)
# for numero in range(0, start_number):
    # esegui la stampa
    # print(numero)

# print(numero)
# forma implicita
# for i in range(start_number):
#     # esegui la stampa
#     print(i)


# vediamo se x è divisibile y e qual è il resto

# 12 - 5 = 7
# 7 > 5 ? sì
# 7 - 5 = 2
# 2 > 5 = no
# 2 è il resto
x = 12
y = 5
resto = 12
while resto > y:
    resto = resto - y
    print(resto)