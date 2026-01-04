def calculo_imc(peso, altura):
    return peso / (altura ** 2)

def classificacao_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidade grau I"
    elif 35 <= imc < 40:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III (mórbida)"

peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

imc = calculo_imc(peso, altura)
categoria = classificacao_imc(imc)

print(f"IMC = {imc:.2f}")
print(f"Classificação: {categoria}")