import random


def carregar_palavras():
    with open("palavras.txt", 'r') as arquivo:
        return arquivo.read().split()

def jogo_da_forca():
    palavras = carregar_palavras()
    palavras = random.choice(palavras).upper()
    letras_descobertas = ['_'for _ in palavra]
    tentativas = 7
    letras_erradas = [ ]

    letra = input("Digie uma letra: ").upper()

    if letra in palavra:
        for i, char in enumerate (palavra):
            if char == letra:
                letras_descobertas [i] = letra

    else:
        if letra not in letras_descobertas:
            letras_erradas.append(letra)
            tentativas = -1

    if '_' not in letras_descobertas:
        print(f"\nParabéns. Você acertou: {palavras}")
    else:
        print(f"\nGame over! A palavra era: {palavra}")

    if __name__ == "__main__":
        jogar_forca()
