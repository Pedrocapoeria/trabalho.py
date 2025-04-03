import random

class JogoForca:
    def __init__(self):
        self.palavras = ['python', 'desenvolvimento', 'jogo', 'programacao', 'inteligencia']
        self.palavra_secreta = random.choice(self.palavras)
        self.tentativas = 6  # número de tentativas permitidas
        self.letras_corretas = ['_'] * len(self.palavra_secreta)
        self.letras_erradas = []

    def mostrar_estado(self):
        print("Palavra: " + ' '.join(self.letras_corretas))
        print(f"Tentativas restantes: {self.tentativas}")
        print(f"Letras erradas: {', '.join(self.letras_erradas)}")

    def jogar(self):
        self.jogar_recursivo()

    def jogar_recursivo(self):
        # Se o jogador não tiver mais tentativas, o jogo acaba
        if self.tentativas <= 0:
            print("Você perdeu! A palavra era:", self.palavra_secreta)
            return

        # Verifica se o jogador adivinhou a palavra
        if '_' not in self.letras_corretas:
            print("Parabéns! Você acertou a palavra:", self.palavra_secreta)
            return

        self.mostrar_estado()
        letra = input("Digite uma letra: ").lower()

        # Verifica se a letra já foi tentada
        if letra in self.letras_corretas or letra in self.letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            self.jogar_recursivo()
            return

        # Verifica se a letra está na palavra secreta
        if letra in self.palavra_secreta:
            print("Boa! A letra está na palavra.")
            for i in range(len(self.palavra_secreta)):
                if self.palavra_secreta[i] == letra:
                    self.letras_corretas[i] = letra
        else:
            print("A letra não está na palavra.")
            self.letras_erradas.append(letra)
            self.tentativas -= 1

        # Chama a função recursiva para o próximo ciclo
        self.jogar_recursivo()

# Rodando o jogo
if __name__ == "__main__":
    jogo = JogoForca()
    jogo.jogar()

