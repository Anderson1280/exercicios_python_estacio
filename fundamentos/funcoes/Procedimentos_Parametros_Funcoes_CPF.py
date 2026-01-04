def validar_cpf(cpf):
    # Removendo caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verificando se o CPF possui 11 dígitos
    if len(cpf) != 11:
        return False

    # Verificando se todos os dígitos são iguais (caso raro, mas inválido)
    if cpf == cpf[0] * 11:
        return False
