#Criando uma listas com alguns elementos
lista = [ 10, 20, 30, 40, 50]

#Acessando elementos individuais da lista
primeriro_elemento_da_lista = lista[0]
segundo_elemento_da_lista = lista[1]

#iimprimindo os elementso acessados
print(f"O primeiro elemento da lista {primeriro_elemento_da_lista}")
print(f"O segundo elemento da lista {segundo_elemento_da_lista}")

#Adicionando um elemento no final da lista
lista.append(60)
print(f"Lista após o elemento 60: {lista}")

#Inserindo um elemento num ponto especifico
lista.insert(25,2) #inserindo 25 na posição 2
print(f"Lista após inserir 25 elemento na posição 2 {lista}")

#Removendo um elemento da lista
lista.remove(40)
print(f"Lista após remover 40, {lista}") # posso ter mais de um 40 mais elimina o primeiro ue encontrar

#Removendo o ultimo elemento da lista
ultimo_elemento = lista.pop()
print(f"Removio ultimo elemento:")
print(f"Lista após remover o ultimo elemento:")

#Acessando um subgrupo da lista
sub_lista = lista[1:4]
print(f"Sub-lista (elemento de 1 a 3) {sub_lista} ")

#Ordenando a lista
lista.sort()
print(f"Lista ordenada: {lista}")

#Iterando sobre elementos da lista
for elemento in lista:
    print(elemento, end= ' ')




