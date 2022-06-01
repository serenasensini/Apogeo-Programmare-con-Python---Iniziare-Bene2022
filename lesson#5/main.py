# come si chiama la classe? Cane
# quali proprietà generali ha un cane? nome, stazza, num_zampe, abbaia, razza

class Cane:

    def __init__(self, p_nome, p_stazza, p_num_zampe, p_abbaia, p_razza, p_lunghezza_pelo):
        self.nome = p_nome
        self.stazza = p_stazza
        self.num_zampe = p_num_zampe
        self.abbaia = p_abbaia
        self.razza = p_razza
        self.lunghezza_pelo = p_lunghezza_pelo

    def __repr__(self):
        print("Nome:", self.nome)
        print("stazza:", self.stazza)
        print("num_zampe:", self.num_zampe)
        print("abbaia:", self.abbaia)
        print("razza:", self.razza)

    def get_nome(self):
        return self.nome

    def set_nome(self, nuovo_nome):
        self.nome = nuovo_nome

# l'oggetto è un'istanza della classe = è un oggetto reale che è nato grazie al modello (classe)
birillo = Cane("Birillo", "Grande", 4, True, "Meticcio", "Lungo")

# birillo.__repr__()

birillo.set_nome("Pluto")

# birillo.__repr__()

print(birillo.get_nome())
