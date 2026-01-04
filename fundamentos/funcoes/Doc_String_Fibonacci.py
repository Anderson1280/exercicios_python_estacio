def fibo(n):
    """
    Determina o n-ésimo termo da sequência de Fibonacci.

    A sequência de Fibonacci é: 0, 1, 1, 2, 3, 5, 8, 13, 21...
    Onde cada termo é a soma dos dois anteriores.

    Args:
        n (int): Posição do termo desejado na sequência

    Returns:
        int: O n-ésimo termo de Fibonacci
    """
    # ✅ Docstring correta: explica a função entre aspas triplas

    if n == 0:
        return 0  # ✅ F(0) = 0
    elif n == 1:
        return 1  # ✅ F(1) = 1
    else:
        return fibo(n - 1) + fibo(n - 2)  # ✅ Fórmula correta de Fibonacci
        # Soma dos dois termos anteriores


# Estas linhas estão FORA da função (sem indentação)
vfibo = fibo(6)  # ✅ Corrigido: nome correto e fora da função
# Calcula o 6º termo de Fibonacci
# F(6) = F(5) + F(4) = 5 + 3 = 8

print(vfibo)
# Imprime: 8

print(help(fibo))
# Mostra a documentação da função (a docstring)