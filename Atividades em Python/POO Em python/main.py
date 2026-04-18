import Animais
import Donos

x = input("Digite 1 para exibir a ficha do animal, Digite 2 para exibir a ficha do dono: ")

match x:
    case "1":
        animal = Animais.Animal('Nina', 'Cachorro', 'SRD', 'Rodrigo')
        animal.exibir_ficha()
    case "2":
        dono = Donos.Dono('12345-00', 'Rodrigo', 'Nina', '123')
        dono.exibir_ficha()
    case _:
        print("Opção inválida.")
