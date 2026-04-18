class Animal:
    def __init__(self, nome, especie, raca, dono):
        self.nome = nome
        self.especie = especie
        self.raca = raca
        self.dono = dono

    def exibir_ficha(self):
        print("-" * 30)
        print(f"Nome do Animal : {self.nome}")
        print(f"Espécie        : {self.especie}")
        print(f"Raça           : {self.raca}")
        print(f"Dono           : {self.dono}")
        print("-" * 30)
