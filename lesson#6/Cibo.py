class Cibo:

    def __init__(self, p_cottura, p_salato, p_dolce, p_temperatura=None):
        self.cottura = p_cottura
        self.salato = p_salato
        self.dolce = p_dolce
        self.temperatura = p_temperatura

    def __repr__(self):
        print('Cotto o crudo?', self.cottura)
        print('Salato:', self.salato)
        print('Dolce:', self.dolce)
        print('Caldo o freddo?', self.temperatura)

    def get_cottura(self):
        return self.cottura

    def set_cottura(self, nuova_cottura):
        self.cottura = nuova_cottura

    def get_salato(self):
        return self.salato

    def set_salato(self, nuovo_salato):
        self.salato = nuovo_salato

    def get_dolce(self):
        return self.dolce

    def set_dolce(self, nuovo_dolce):
        self.dolce = nuovo_dolce

    def get_temperatura(self):
        return self.temperatura

    def set_temperatura(self, nuova_temperatura):
        self.temperatura = nuova_temperatura

class Pizza(Cibo):

    def __init__(self, p_cottura, p_salato, p_dolce, p_temperatura, p_gusto):
        super().__init__(p_cottura, p_salato, p_dolce, p_temperatura)
        self.gusto = p_gusto

    def __repr__(self):
        super().__repr__()
        print("Il gusto è:", self.gusto)

pasta = Cibo("Cotta", "Yes", "No", "Calda")
# pasta.__repr__()

margherita = Pizza("Veloce", "Yes", "No", None, "Margherita")

print(margherita.get_salato().lower())

margherita.__repr__()

print(type(margherita))

print(type(Pizza))

print(type(Cibo))
