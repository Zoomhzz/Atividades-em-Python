class Dono:
    def __init__(self, cpf, nome, pet, telefone):
        self.nome = nome
        self.cpf = cpf
        self.pet = pet
        self.telefone = telefone

    def exibir_ficha(self):
        print("-" * 30)
        print(f"Nome do Dono   : {self.nome}")
        print(f"CPF            : {self.cpf}")
        print(f"Pet            : {self.pet}")
        print(f"Telefone       : {self.telefone}")
        print("-" * 30)
