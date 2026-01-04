#While

print('antes while')
palavra = input("Entre com uma palavra: ")
while palavra != "sair":
    print("dentro do while")
    palavra = input("Digite sair para encerrar o laça.")
print("Você, digitou sair e agora esta fora do laço.")

#While, if, break, else...

while true:
    print('Você está no primeiro laço.')
    opcao1 = input('Deseja sair dele? Digite SIM para isso. \n')
    if opcao1 == 'SIM':
        break  # este break é do primeiro laço
    else:
        while true:
            print('Você está no segundo laço.')
            opcao2 = input('Deseja sair dele? Digite SIM para isso. \n')
            if opcao2 == 'SIM':
               break  # este break é do segundo laço
        print('Você saiu do segundo laço.')


#for, range, if, continue, break
for num in range (1,11):
    if num == 5:
        continue
    else:
        print(num)
print("Laço encerrado.")

for num in range (1,11):
    if num % 2 == 0:
        pass
    else:
        print(num)
print("LAÇO ENCERRADO.")

