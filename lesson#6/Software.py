class Software:

    def __init__(self, p_tipo, p_marca):
        self.tipo = p_tipo
        self.marca = p_marca

    def __repr__(self):
        print("il tipo del software è:", self.tipo)
        print("la marca del software è", self.marca)

    def get_tipo(self):  # restituisce il valore
        return self.tipo

    def set_tipo(self, nuovo_tipo):  # modifica il valore
        self.tipo = nuovo_tipo


class Browser(Software):
    pass

my_software = Software("Edge", "Microsoft")

my_software.__repr__()