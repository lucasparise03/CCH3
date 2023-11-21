from abc import ABC, abstractmethod

class ConstrutorDeCarro(ABC):
    def construir_carro(self):
        self.construir_chassi()
        self.instalar_motor()
        self.pintar_carro()

    @abstractmethod
    def construir_chassi(self):
        pass

    @abstractmethod
    def instalar_motor(self):
        pass

    def pintar_carro(self):
        print("Pintando o carro com a cor padrão.")

class ConstrutorDeCarroEsportivo(ConstrutorDeCarro):
    def construir_chassi(self):
        print("Construindo o chassi de um carro esportivo.")

    def instalar_motor(self):
        print("Instalando um motor esportivo.")

    def pintar_carro(self):
        print("Pintando o carro esportivo de preto fosco.")

class ConstrutorDeCarroLuxo(ConstrutorDeCarro):
    def construir_chassi(self):
        print("Construindo o chassi de um carro de luxo.")

    def instalar_motor(self):
        print("Instalando um motor potente para um carro de luxo.")

if __name__ == "__main__":
    construtor_esportivo = ConstrutorDeCarroEsportivo()
    construtor_esportivo.construir_carro()

    print("\n")

    construtor_luxo = ConstrutorDeCarroLuxo()
    construtor_luxo.construir_carro()
