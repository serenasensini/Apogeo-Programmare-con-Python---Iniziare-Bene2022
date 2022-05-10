# Usa questo file per testare il tuo codice!

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








testo = "CIAO21212"

if testo.islower():
    print("Il testo è tutto minuscolo")
elif testo.isupper():
    print("Il testo è tutto maiuscolo")
else:
    print("Il testo è misto.")