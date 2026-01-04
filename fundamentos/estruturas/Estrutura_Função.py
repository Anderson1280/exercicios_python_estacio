escolha = input("Escolha uma opção de função: 1 ou 2\n")
if escolha == "1":
    def func1(x):
        return x + 1
    s = func1(10)
else:
    def func2(x):
        return x + 2
    s = func2(10)
print(s)

"""#A linha 1 solicita ao usuário que 
escolha entre duas opções de função."""

"""#Se o usuário escolher "1", a função func1 é 
definida e chamada com o argumento 10, retornando 11."""

"""Se o usuário escolher outra opção, a função func2 é
definida e chamada com o argumento 10, retornando 12."""

#A linha final imprime o resultado da função escolhida.

