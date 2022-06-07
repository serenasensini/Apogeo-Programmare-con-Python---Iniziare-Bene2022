class MezziTrasporto:

    def __init__(self, tipo, num_posti, num_ruote):
        self.tipo = tipo
        self.num_posti = num_posti
        self.num_ruote = num_ruote

    def __repr__(self):
        print('tipo:', self.tipo)
        print('numero_posti:', self.num_posti)
        print('numero_ruote:', self.num_ruote)

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, nuovo_tipo):
        self.tipo = nuovo_tipo


mia_auto = MezziTrasporto("Auto", 4, 4)

mia_auto.__repr__()