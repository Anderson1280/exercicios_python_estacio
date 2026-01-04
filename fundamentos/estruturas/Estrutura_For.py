for item in range(2,9,3):
    print(item)
#-------------------------------
name = input("Digite um nome: ")
for letra in name:
    print(letra, end= '')
"""----------------------------------------
-------------------"""
nome = ['Andressa', 'Anderson', 'Ana']
for nomes in nome:
    print(nomes)
"""----------------------------------
--------------------"""
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    quadrado = numero ** 2
    print(f'O quadrado de {numero} é {quadrado}')
    pass
"""-------------------------------------
---------------------------"""

numeros = [1, 2, 3, 4, 5]
soma = 0
for numero in numeros:
    soma += numero
print(f"A soma de todos os numeros é {soma}")
#print(f"A soma de todos os numeros é {soma}")
"""----------------------------
_____________---"""

texto = "programação"
letra_para_contar = "r"
contador = 0

for letra in texto:
    if letra == letra_para_contar:
        contador += 1

print(f"A letra {letra_para_contar} aparece {contador} vezes na palavra {texto}")
"""------------------------------------
-----------------------"""
nome = input("Digite seu nome: \n")
for letra in nome:
    print(letra, end='')
"""-----------------------
-------------------"""

texto = "programação"
letra_para_contar = "a"
contador = 0

for letra in texto:
    if letra == letra_para_contar:
        contador += 1

print(f"A letra '{letra_para_contar}' aparece {contador} vezes na palavra '{texto}'.")

s = 0
for i in range(5):
    s += 3 * i
print(s)
