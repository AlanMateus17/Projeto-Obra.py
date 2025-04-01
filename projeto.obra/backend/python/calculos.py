class Parede:
    def _init_(self, largura, altura):
        """Inicializa a parede com largura e altura."""
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        """Calcula e retorna a área da parede."""
        return self.largura * self.altura

class Tijolo:
    def _init_(self, altura, largura):
        """Inicializa o tijolo com altura e largura."""
        self.altura = altura
        self.largura = largura

    def calcular_area(self):
        """Calcula e retorna a área do tijolo."""
        return self.altura * self.largura

def main_parede_tijolo():
    """Função principal para calcular a quantidade de tijolos necessários para uma parede."""
    # Solicita ao usuário as dimensões da parede
    largura_parede = float(input("Digite a largura da parede (em metros): "))
    altura_parede = float(input("Digite a altura da parede (em metros): "))

    # Cria uma instância da classe Parede
    parede = Parede(largura_parede, altura_parede)

    # Calcula e exibe a área da parede
    area_parede = parede.calcular_area()
    print(f"A área da parede é: {area_parede:.2f} m²")

    # Solicita ao usuário as dimensões do tijolo
    altura_tijolo = float(input("Digite a altura do tijolo (em metros): "))
    largura_tijolo = float(input("Digite a largura do tijolo (em metros): "))

    # Cria uma instância da classe Tijolo
    tijolo = Tijolo(altura_tijolo, largura_tijolo)

    # Calcula e exibe a área do tijolo
    area_tijolo = tijolo.calcular_area()
    print(f"A área do tijolo é: {area_tijolo:.2f} m²")

    # Calcula a quantidade de tijolos necessários
    quantidade_tijolos = area_parede / area_tijolo
    print(f'A quantidade de tijolos necessários para cobrir a parede é: {quantidade_tijolos:.2f}')

class Viga:
    def _init_(self, altura, largura, profundidade):
        """Inicializa a viga com altura, largura e profundidade."""
        self.altura = altura
        self.largura = largura
        self.profundidade = profundidade

    def calcular_area(self):
        """Calcula e retorna a área da viga."""
        return self.altura * self.largura

    def calcular_volume(self):
        """Calcula e retorna o volume da viga."""
        return self.altura * self.largura * self.profundidade

def main_viga():
    """Função principal para calcular a área e o volume de uma viga."""
    # Solicita ao usuário as dimensões da viga
    altura_viga = float(input("Digite a altura da viga (em metros): "))
    largura_viga = float(input("Digite a largura da viga (em metros): "))
    profundidade_viga = float(input("Digite a profundidade da viga (em metros): "))

    # Cria uma instância da classe Viga
    viga = Viga(altura_viga, largura_viga, profundidade_viga)

    # Calcula e exibe a área da viga
    area_viga = viga.calcular_area()
    print(f"A área da viga é: {area_viga:.2f} m²")

    # Calcula e exibe o volume da viga
    volume_viga = viga.calcular_volume()
    print(f"O volume da viga é: {volume_viga:.2f} m³")

class Contraviga:
    def _init_(self, altura, largura, profundidade):
        """Inicializa a contraviga com altura, largura e profundidade."""
        self.altura = altura
        self.largura = largura
        self.profundidade = profundidade

    def calcular_area(self):
        """Calcula e retorna a área da contraviga."""
        return self.altura * self.largura

    def calcular_volume(self):
        """Calcula e retorna o volume da contraviga."""
        return self.altura * self.largura * self.profundidade

def main_contraviga():
    """Função principal para calcular a área e o volume de uma contraviga."""
    # Solicita ao usuário as dimensões da contraviga
    altura_contraviga = float(input("Digite a altura da contraviga (em metros): "))
    largura_contraviga = float(input("Digite a largura da contraviga (em metros): "))
    profundidade_contraviga = float(input("Digite a espessura da contraviga (em metros): "))

    # Cria uma instância da classe Contraviga
    contraviga = Contraviga(altura_contraviga, largura_contraviga, profundidade_contraviga)

    # Calcula e exibe a área da contraviga
    area_contraviga = contraviga.calcular_area()
    print(f"A área da contraviga é: {area_contraviga:.2f} m²")

    # Calcula e exibe o volume da contraviga
    volume_contraviga = contraviga.calcular_volume()
    print(f"O volume da contraviga é: {volume_contraviga:.2f} m³")

if _name_ == "_main_":
    main_parede_tijolo()
    main_viga()
    main_contraviga()