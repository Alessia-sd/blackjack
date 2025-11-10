# Atividade Gestão de dados e programação com classes

class Carta:
    naipes = ['?', 'Paus', 'Ouros', 'Copas', 'Espadas']
    valores = ['?', 'Ás', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Rainha', 'Rei']

    def __init__(self, naipe, valor):
        self.naipe = naipe
        self.valor = valor
        self.ordem = (self.naipe - 1) * 13 + self.valor

    # 2 - Movido para dentro da classe Carta
    def __str__(self):
        return self.valores[self.valor] + ' de ' + self.naipes[self.naipe]

    # 3 - Movido para dentro da classe Carta
    def __lt__(self, outro):
        return self.valor < outro.valor or (self.valor == outro.valor and self.naipe < outro.naipe)

    def __gt__(self, outro):
        return self.valor > outro.valor or (self.valor == outro.valor and self.naipe > outro.naipe)

#4

import random

class Baralho:
    def __init__(self):
        self.cartas = [Carta(naipe, valor) for naipe in range(1, 5) for valor in range(1, 14)]
        self.cartas_removidas = []

    # 5 - Movido para dentro da classe Baralho
    def baralhar(self):
        random.shuffle(self.cartas)

    # 6 - Movido para dentro da classe Baralho
    def ordenar(self):
        self.cartas.sort(key=lambda carta: carta.ordem)

    # 7 - Movido para dentro da classe Baralho
    def retirar(self):
        if self.cartas:
            carta = self.cartas.pop()
            self.cartas_removidas.append(carta)
            return carta
        return None

    # 8 - Movido para dentro da classe Baralho
    def restaurar(self):
        self.cartas.extend(self.cartas_removidas)
        self.cartas_removidas.clear()

    # 9 - Movido para dentro da classe Baralho
    def __str__(self):
        return "\n".join(str(carta) for carta in self.cartas)

#10

def pontua(jogador, cartas):
    total = sum(11 if carta.valor == 1 else min(carta.valor, 10) for carta in cartas)
    ases = sum(1 for carta in cartas if carta.valor == 1)

    while total > 21 and ases:
        total -= 10
        ases -= 1

    print(f"\n{jogador}: {total} pontos")
    for carta in cartas:
        print(f" {carta}")

    return total

def blackjack():
    b = Baralho()
    b.baralhar()

    cartas_dealer = [b.retirar(), b.retirar()]
    cartas_player = [b.retirar(), b.retirar()]

    print(f"Dealer: ?? pontos\n\n {cartas_dealer[0]}\n -Carta Escondida-\n")
    pontos_player = pontua("Player", cartas_player)

    if pontos_player > 21:
        print("\n PERDEU!")
        return

    print("\n*******")

    while True:
        pontos_dealer = pontua("Dealer", cartas_dealer)

        if pontos_dealer > 21:
            print("\nGANHOU!")
            return
        elif pontos_dealer > pontos_player:
            print("\nPERDEU! ")
            return
        elif pontos_dealer == pontos_player and pontos_dealer == 21:
            print("\nEMPATE!")
            return
        elif pontos_dealer <= pontos_player and pontos_dealer < 21:
            cartas_dealer.append(b.retirar())

# Adição da função main
def main():
    """Função principal para iniciar o jogo de Blackjack."""
    blackjack()

# Estrutura de execução da função main
if __name__ == "__main__":
    main()