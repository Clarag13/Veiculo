from carro import *

class Teste:
    def _init_(self):
        pass

    def executar(self):
        # Criando uma instância de Carro
        carro1 = Carro('Toyota', 'Corolla', 'Prata')

        # Acessando e modificando atributos
        print('Informações antes da alteração:')
        carro1.exibir_informacoes()

        carro1.alterar_modelo('Camry')
        carro1.alterar_ano(2023)

        print('\nInformações após a alteração:')
        carro1.exibir_informacoes()


# Testando as classes
if _name_ == "_main_":
    teste = Teste()
    teste.executar()
