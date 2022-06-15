# Scrivere una classe Personaggio, che fa parte di un gioco con diversi
# personaggi magici. Ognuno di loro ha un nome, un potere ed una
# citazione preferita. I personaggi possono essere maghi o streghe:
# i maghi, se salutati, restituiscono il saluto, mentre le streghe
# maledicono chi li saluta.
# Inoltre, il mago ha degli oggetti magici da donare che sono contenuti
# in una sacca. Creare le funzioni appropriate a rappresentare i
# requisiti sopra citati, inizializzando gli opportuni oggetti per
# testare la classe.

class Personaggio:

    def __init__(self, p_nome, p_potere, p_citazione):
        self.nome = p_nome
        self.potere = p_potere
        self.citazione = p_citazione

    def __repr__(self):
        print("Mi chiamo:", self.nome)
        print("Il mio potere è", self.potere)
        print(self.citazione)

    def get_nome(self):
        return self.nome

    def get_potere(self):
        return self.potere

    def get_citazione(self):
        return self.citazione

    def set_nome(self, nuovo_nome):
        self.nome = nuovo_nome

    def set_potere(self, nuovo_potere):
        self.potere = nuovo_potere

    def set_citazione(self, nuova_citazione):
        self.citazione = nuova_citazione
'''
mago = Personaggio("Manto", "Fascio di luce stellato", "Sono il mago "
                                                       "Manto, "
                                                       "dove vado "
                                                       "canto!")

mago.__repr__()
'''

class Mago(Personaggio):

    def __init__(self, p_nome, p_potere, p_citazione, p_saluto):
        super().__init__(p_nome, p_potere, p_citazione)
        self.saluto = p_saluto
        self.oggetti = []

    def __repr__(self):
        super().__repr__()
        print(self.saluto)
        for oggetto in self.oggetti:
            oggetto.__repr__()

    def set_oggetti(self, nuovi_oggetti):
        self.oggetti = nuovi_oggetti

    def add_oggetto(self, nuovo_oggetto):
        self.oggetti.append(nuovo_oggetto)

mago = Mago("Manto", "Fascio di luce stellato", "Sono il mago "
                                                       "Manto, "
                                                       "dove vado "
                                                       "canto!",
            "Ricambio con ossequi il tuo saluto!")

mago.__repr__()

# oggetti = ["Bacchetta magica", "Cappello"]
# mago.set_oggetti(oggetti)

# mago.__repr__()

# mago.add_oggetto("Anacleto")

# mago.__repr__()

class Oggetto:

    def __init__(self, p_nome, p_peso):
        self.nome = p_nome
        self.peso = p_peso

    def __repr__(self):
        print("Il nome dell'attrezzo è", self.nome)
        print(self.nome, "pesa", self.peso, "kg")

    def get_nome(self):
        return self.nome

    def get_peso(self):
        return self.peso

    def set_nome(self, p_nome):
        self.nome = p_nome

    def set_peso(self, p_peso):
        self.peso = p_peso

bacchetta_magica = Oggetto("Bacchetta magica", 1)
cappello = Oggetto("Cappello", 3)

mago.add_oggetto(bacchetta_magica)
mago.add_oggetto(cappello)

# in alternativa

# mago.set_oggetti([bacchetta_magica, cappello])

mago.__repr__()