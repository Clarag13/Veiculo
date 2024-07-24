class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca            
        self._modelo = modelo         
        self.__ano = None            

    def consultar_modelo(self):
        return self._modelo          

    def alterar_modelo(self, novo_modelo):
        self._modelo = novo_modelo   

    def consultar_ano(self):
        return self.__ano            

    def alterar_ano(self, novo_ano):
        self.__ano = novo_ano        


class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor                

    def exibir_informacoes(self):
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.consultar_modelo()}')
        print(f'Cor: {self.cor}')
