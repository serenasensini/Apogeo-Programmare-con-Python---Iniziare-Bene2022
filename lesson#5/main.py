# # come si chiama la classe? Cane
# # quali proprietà generali ha un cane? nome, stazza, num_zampe, abbaia, razza
#
# class Cane:
#
#     def __init__(self, p_nome, p_stazza, p_num_zampe, p_abbaia, p_razza, p_lunghezza_pelo):
#         self.nome = p_nome
#         self.stazza = p_stazza
#         self.num_zampe = p_num_zampe
#         self.abbaia = p_abbaia
#         self.razza = p_razza
#         self.lunghezza_pelo = p_lunghezza_pelo
#
#     def __repr__(self):
#         print("Nome:", self.nome)
#         print("stazza:", self.stazza)
#         print("num_zampe:", self.num_zampe)
#         print("abbaia:", self.abbaia)
#         print("razza:", self.razza)
#
#     def get_nome(self):
#         return self.nome
#
#     def set_nome(self, nuovo_nome):
#         self.nome = nuovo_nome
#
# # l'oggetto è un'istanza della classe = è un oggetto reale che è nato grazie al modello (classe)
# birillo = Cane("Birillo", "Grande", 4, True, "Meticcio", "Lungo")
#
# # birillo.__repr__()
#
# birillo.set_nome("Pluto")
#
# # birillo.__repr__()
#
# print(birillo.get_nome())


class Smartphone:

    def __init__(self, s_marca, s_modello, s_processore, s_schermo,
                 s_connettività, s_prezzo, s_os):
        self.marca = s_marca
        self.modello = s_modello
        self.processore = s_processore
        self.schermo = s_schermo
        self.connettività = s_connettività
        self.prezzo = s_prezzo
        self.os = s_os

    def __repr__(self):
        print("La marca è:", self.marca)
        print("Il modello è:", self.modello)
        print("Il processore è:", self.processore)
        print("Lo schermo è:", self.schermo)
        print("La connettività è:", self.connettività)
        print("Il prezzo è:", self.prezzo)
        print("Il sistema operativo è:", self.os)

    def get_marca(self):
        return self.marca

    def set_marca(self, nuova_marca):
        self.marca = nuova_marca

    def get_modello(self):
        return self.modello

    def set_modello(self, nuovo_modello):
        self.modello = nuovo_modello

    def get_processore(self):
        return self.processore

    def set_processore(self, nuovo_processore):
        self.processore = nuovo_processore

    def get_connettività(self):
        return self.connettività

    def set_connettività(self, nuova_connettività):
        self.connettività = nuova_connettività

    def get_schermo(self):
        return self.schermo

    def set_schermo(self, nuovo_schermo):
        self.schermo = nuovo_schermo

    def get_prezzo(self):
        return self.prezzo

    def set_prezzo(self, nuovo_prezzo):
        self.prezzo = nuovo_prezzo

    def get_sistema_operativo(self):
        return self.os

    def set_sistema_operativo(self, nuovo_sistema_operativo):
        self.os = nuovo_sistema_operativo


mio_cellulare = Smartphone("Samsung", "S21", "Snapdragon", "5\"", "4G", 600, "Android")

print("Il mio cellulare", mio_cellulare.get_marca())
mio_cellulare.__repr__()

tuo_cellulare = Smartphone("Xiaomi", "Red mi note 8", "Snapdragon", "6\"", "5G", 400, "Android")

if mio_cellulare.get_marca() == tuo_cellulare.get_marca():
    print("Sono della stessa marca")
else:
    print("Non sono della stessa marca")