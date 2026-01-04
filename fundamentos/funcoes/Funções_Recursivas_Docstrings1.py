def fatorial(n):  # ✅ CORRIGIDO: "def" completo (estava "ef")
    # Define uma função chamada "fatorial" que recebe um parâmetro "n"
    # Esta função calcula o fatorial de um número usando recursão
    # Fatorial de 5 (5!) = 5 × 4 × 3 × 2 × 1 = 120

    if n == 0 or n == 1:
        # Verifica se n é igual a 0 OU se n é igual a 1
        # Esta é a CONDIÇÃO DE PARADA da recursão
        # Por definição matemática: 0! = 1 e 1! = 1
        # "or" significa que basta UMA das condições ser verdadeira

        return 1
        # Se n for 0 ou 1, retorna 1 e ENCERRA a função
        # Isso impede que a recursão continue infinitamente

    else:
        # Se n não for 0 nem 1 (ou seja, n >= 2)
        # Executa o bloco abaixo

        return n * fatorial(n - 1)
        # AQUI ACONTECE A RECURSÃO (a função chama ela mesma)
        # Multiplica n pelo fatorial de (n-1)
        # Exemplo com n=5:
        # fatorial(5) = 5 * fatorial(4)
        # fatorial(4) = 4 * fatorial(3)
        # fatorial(3) = 3 * fatorial(2)
        # fatorial(2) = 2 * fatorial(1)
        # fatorial(1) = 1 (condição de parada)
        # Então: 5 * 4 * 3 * 2 * 1 = 120

# Estas linhas estão FORA da função (sem indentação)

vfat = fatorial(5)
# Chama a função fatorial passando o número 5 como argumento
# A função executa e retorna 120
# O valor 120 é armazenado na variável "vfat"

print(f"Recursiva {vfat}")
# f"..." é uma f-string (formatted string)
# {vfat} insere o valor da variável vfat na string
# Imprime: "Recursiva 120"