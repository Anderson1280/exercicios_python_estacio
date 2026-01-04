idade = int(input("Digite sua idade: "))
if  idade < 10:
    prin("Você é uma criança.")
elif idade >= 10 and idade <= 15:
    print("Você é um adolescente.")
elif idade >= 16 and idade <=18:
    print("Você é menor de idade.")
elif idade >= 18 and idade <=65:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")