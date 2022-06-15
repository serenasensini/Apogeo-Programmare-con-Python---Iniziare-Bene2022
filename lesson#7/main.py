# numero = input("Inserisci un numero:")
#
# try:
#     # se non il tipo di (numero) è un intero
#     # =
#     # se il tipo di numero non è un intero
#     if not type(numero) is int:
#         raise TypeError("L'input non è numerico")
#
# except ZeroDivisionError as e:
#     print(e)

import random

numero_casuale = random.randint(0, 10)
# print(numero_casuale)

numero_random = random.random()
# print(numero_random)

import sys

# print(sys.version)
# print(sys.platform)
# print(sys.path)

import platform as pf


# print(pf.version())
# print(pf.platform())
# print(pf.system())
# print(pf.architecture())
# print(pf.machine())

# raggruppamento di più eccezioni allo stesso tempo
# try:
#     name = "Daniele"
#     name += 5
# except (NameError, TypeError) as error:
#     print(error)

# def somma(*pippo):
#     result = 0
#     for x in pippo:
#         result += x
#     return result


# print(somma(1, 2, 3))
# print(somma())


# def concatenate(**kwargs):
#     result = ""
#     for arg in kwargs.values():
#         result += arg
#     return result
#
# print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))

# def get_temperature_info(**diz):
#     for key in diz.keys():
#         print(diz[key])
#
# get_temperature_info(meas="Celsius", temp=15)

# class Pippo:
#
#     def __init__(self, *args):
#         self.args = args
#         self.nome = ''
#
#     # def __init__(self, nome=None):
#     #     self.nome = nome

print("hello", "world", "python", "!", sep="\n")