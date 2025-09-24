"""
Revisão (Instância de uma Classe):
- Criação.
- O construtor é responsável por receber a própria instância e 
os valores a serem introduzidos nos atributos da instância.
- Os métodos sem decoradores serão por padrão métodos de 
instância.
"""
class carro:
    rodas = 4

def _init_(self, marca, ano):
    self.marca = marca
    self.ano = ano


def ligar(self):
    print(f"O carro {self.marca} {self.ano} está ligado!")

@classmethod

def mudar_numero_rodas(cls, novas_rodas):
    cls.rodas = novas_rodas
    print(f"Agora todos os carros tem {novas_rodas} rodas!")

@staticmethod

def calcular_idade(ano_fabricacao, ano_atual):
    return ano_atual - ano_fabricacao