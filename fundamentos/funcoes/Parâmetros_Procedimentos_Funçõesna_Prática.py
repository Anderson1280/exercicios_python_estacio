def validar_cpf(cpf):
    # Define uma função chamada validar_cpf que recebe um CPF como parâmetro

    # Removendo caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))
    # filter(str.isdigit, cpf) → filtra apenas os dígitos numéricos do CPF
    # ''.join(...) → junta os dígitos em uma string sem separadores
    # Exemplo: "123.456.789-09" vira "12345678909"

    # Verificando se o CPF possui 11 dígitos
    if len(cpf) != 11:
        # len(cpf) → conta quantos caracteres tem na string
        # Se não tiver exatamente 11 dígitos, o CPF é inválido
        return False
        # Retorna False (falso) e encerra a função

    # Verificando se todos os dígitos são iguais (caso raro, mas inválido)
    if cpf == cpf[0] * 11:
        # cpf[0] → pega o primeiro dígito
        # cpf[0] * 11 → repete esse dígito 11 vezes (ex: "1" * 11 = "11111111111")
        # Isso invalida CPFs como 111.111.111-11 ou 000.000.000-00
        return False
        # Retorna False pois CPFs com todos os dígitos iguais são inválidos

    # Calculando o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    # range(9) → gera números de 0 a 8 (os primeiros 9 dígitos do CPF)
    # cpf[i] → pega cada dígito na posição i
    # int(cpf[i]) → converte o dígito de string para número
    # (10 - i) → peso que decresce: 10, 9, 8, 7, 6, 5, 4, 3, 2
    # Multiplica cada dígito pelo seu peso e soma tudo
    # Exemplo: se CPF = "12345678909"
    # soma = 1*10 + 2*9 + 3*8 + 4*7 + 5*6 + 6*5 + 7*4 + 8*3 + 9*2

    resto = soma % 11
    # % 11 → calcula o resto da divisão da soma por 11
    # Exemplo: se soma = 210, então 210 % 11 = 1

    if resto < 2:
        digito_verificador_1 = 0
        # Se o resto for 0 ou 1, o primeiro dígito verificador é 0
    else:
        digito_verificador_1 = 11 - resto
        # Se o resto for 2 ou mais, subtrai o resto de 11
        # Exemplo: se resto = 1, então 11 - 1 = 10 (mas como resto < 2, será 0)

    # Verificando o primeiro dígito verificador
    if int(cpf[9]) != digito_verificador_1:
        # cpf[9] → pega o 10º dígito (índice 9) que é o primeiro verificador
        # Compara o dígito verificador calculado com o dígito informado
        return False
        # Se forem diferentes, o CPF é inválido

    # Calculando o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    # range(10) → agora usa os primeiros 10 dígitos (incluindo o 1º verificador)
    # (11 - i) → pesos: 11, 10, 9, 8, 7, 6, 5, 4, 3, 2
    # Calcula a soma ponderada dos 10 primeiros dígitos

    resto = soma % 11
    # Calcula o resto da divisão por 11 novamente

    if resto < 2:
        digito_verificador_2 = 0
        # Se resto < 2, o segundo dígito verificador é 0
    else:
        digito_verificador_2 = 11 - resto
        # Caso contrário, subtrai o resto de 11

    # Verificando o segundo dígito verificador
    if int(cpf[10]) != digito_verificador_2:
        # cpf[10] → pega o 11º dígito (índice 10) que é o segundo verificador
        # Compara com o dígito verificador calculado
        return False
        # Se forem diferentes, o CPF é inválido

    # CPF válido
    return True
    # Se passou por todas as verificações, o CPF é válido


# Testando a função
cpf = input(f"Digite seu CPF: ")
# Define uma variável com um CPF de exemplo

if validar_cpf(cpf):
    # Chama a função validar_cpf com o CPF de exemplo
    # Se retornar True, executa o bloco abaixo
    print(f"O CPF {cpf} é válido.")
    # f"..." → f-string que permite inserir variáveis com {cpf}
    # Imprime mensagem dizendo que o CPF é válido
else:
    # Se retornar False, executa este bloco
    print(f"O CPF {cpf} é inválido.")
    # Imprime mensagem dizendo que o CPF é inválido
