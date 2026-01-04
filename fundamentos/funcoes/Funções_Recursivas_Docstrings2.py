def fatorial(n):
    # Define a função fatorial
    fat = 1
    # Inicializa variável com 1

    if n == 0 or n == 1:
        # Casos base: 0! = 1 e 1! = 1
        return fat
    else:
        # Para n >= 2, calcula o fatorial
        for x in range(2, n + 1):  # ✅ CORRIGIDO: n+1 para incluir n
            # Loop de 2 até n (incluindo n)
            fat = fat * x
            # Multiplica fat pelo número atual
        return fat
        # Retorna o resultado


# Estas linhas devem estar FORA da função (sem indentação)
vfat = fatorial(5)  # ✅ CORRIGIDO: nome da função e indentação
# Chama a função com argumento 5

print(f"Resultado iterativa: {vfat}")  # ✅ CORRIGIDO: {vfat} ao invés de [vfat]
# Imprime o resultado