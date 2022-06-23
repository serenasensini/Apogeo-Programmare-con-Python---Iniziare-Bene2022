# import sys
# print(sys.path)

myfile = open("C:\\Users\\seren\\PycharmProjects\\Apogeo-Programmare-con"
              "-Python---Iniziare-Bene2022\\lesson#8\\test.txt", "r")

# open("test.txt", "w")
#
# open("test.txt", "r")
# open("test.txt")
#
# open("test.txt", "wb")
# myfile.close()

# alternativa

# with open("test.txt", "w") as file:
#     pass

# contenuto = myfile.read()
# print(contenuto)

# for line in myfile:
#     print(line)
#     lettera = "P"
#     if lettera == line[0]:
#         print(True)


# se la riga è tutta maiuscola, la stampo, altrimenti no

# for line in myfile:
#     if line.isupper():
#         print(line)


myfile = open("C:\\Users\\seren\\PycharmProjects\\Apogeo-Programmare-con"
              "-Python---Iniziare-Bene2022\\lesson#8\\nuovo_file.txt",
              "w")
#
# myfile.write("\ntest di prova")
#
# myfile.close()

myfile = open("C:\\Users\\seren\\PycharmProjects\\Apogeo-Programmare-con"
              "-Python---Iniziare-Bene2022\\lesson#8\\test.txt",
              "r")

# print(type(myfile))
# contenuto = myfile.read()
# print(contenuto)
#
# contenuto = myfile.readlines()
# print(contenuto)

# leggi una specifica riga
# count = 0
# for line in myfile:
#     if count == 2:
#         print(line)
#     else:
#         count += 1
#

# import os
#
# out = os.path.isdir("C:\\Users\\seren\\PycharmProjects\\Apogeo"
#                     "-Programmare-con-Python---Iniziare-Bene2022"
#                     "\\lesson#8")
# print(out)
#
# cwd = os.getcwd()
# print(cwd)
#
# os.chdir('../lesson#8')
#
# nuovo_file = open("file_post_chdir.txt", "w")
# nuovo_file.write("test")
# nuovo_file.close()


# SOLUZIONE N.1

# Aprire il file nella cartella data/lorem.txt, scriverci
# dentro una frase e poi chiuderlo.

# nuovo_file = open("data/lorem.txt", "w")
# nuovo_file.write("ciao")
# nuovo_file.close()

# SOLUZIONE N.3

# Aprire il file nella cartella data/cupcake.txt,
# leggerlo e contare il numero di occorrenze
# delle seguenti parole, inserendole all'interno
# di un dizionario:
# - cupcake
# - chocolate
# - donut


# lista = ["cupcake", "jelly", "gingerbread", "jelly", "donut"]

dizionario = {
    "cupcake": 0,
    "donut": 0,
    "chocolate": 0
}

cupcake = open("data/cupcake.txt", "r")
# contenuto = cupcake.read()
# print(contenuto)
contenuto = cupcake.readlines()
print(contenuto)

dolci = []
# per ogni riga del file...
for linea in contenuto:
    # separo le singole parole della riga...
    parole = linea.split()
    # .. e le aggiungo alla lista usando il metodo extend()
    dolci.extend(parole)
print(dolci)

# per ogni parola di quelle presenti nel file...
for parola in dolci:
    # ... la riduco in maiuscolo...
    parola = parola.lower()
    # ... e se poi corrisponde a una di quelle cercate, aggiorno il
    # dizionario!
    if "cupcake" == parola:
        dizionario["cupcake"] = dizionario["cupcake"] + 1
    elif "chocolate" == parola:
        dizionario["chocolate"] = dizionario["chocolate"] + 1
    elif "donut" == parola:
        dizionario["donut"] = dizionario["donut"] + 1

print(dizionario)