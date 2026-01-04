#Criando uma lista com alguns elementos
lista = [10, 20, 30, 40, 50]

#Acessando elementos individuais da lista
primeiro_elemento = lista[0]
segundo_elemento = lista[1]

#Impriminto os elementos acessados
print(f'O primeito elemento da lista é {primeiro_elemento}')
print(f'O segundo elemento da lista é {segundo_elemento}')

#Adicionando um elemento ao final da lista
lista.append(60)
print(f'Lista após adicionaar 60, {lista}')

#Inserndo um elemento em uma posição especifica
lista.insert(2, 25) # Inserindo 25 na posição 2
print(f'Lista após inserir 25 na posição 2: {lista}')

#Removendo um elemento da lista
lista.remove(40) # Remove o primeiro valor encontrado
print(f'Lista após remover 40: {lista}')

#Removendo o último elemento da lista
ultimo_elemento = lista.pop()
print(f'Elememto removido: {ultimo_elemento}')
print(f'Lista após remover o último elemento: {lista}')

#Acessando um subgrupo da lista (fatiamento)
sub_lista = lista[1:4]
print(f'Sub-lista (elementos de indice 1 a 3: {sub_lista}')

#Ordenando a lista
lista.sort()
print(f'lista ordenada: {lista}')

#iterando sobre os elementos da lista
print('Iterando sobre a lista: ')
for elemento in lista:
    print(elemento)



