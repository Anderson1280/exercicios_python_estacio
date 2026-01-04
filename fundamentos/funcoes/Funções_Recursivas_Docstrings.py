#Função recursiva contagem recursiva
def regressiva(x):
    print(x)
    if x > 0:
        regressiva(x - 1)
    else:
        print("acabou")
    regressiva(10)

    #Não regressiva
    for i in range(10, -1, -1):
        print(i)
