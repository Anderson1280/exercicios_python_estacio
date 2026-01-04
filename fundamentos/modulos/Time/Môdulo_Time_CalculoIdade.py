import time


def calcular_idade(ano_nasc, mes_nasc, dia_nasc):
    hoje = time.localtime()

    idade = hoje.tm_year - ano_nasc

    # Verifica se já fez aniversário este ano
    if (hoje.tm_mon < mes_nasc) or (hoje.tm_mon == mes_nasc and hoje.tm_mday < dia_nasc):
        idade -= 1

    print(f"Você tem {idade} anos")

    # Dias até próximo aniversário
    if hoje.tm_mon > mes_nasc or (hoje.tm_mon == mes_nasc and hoje.tm_mday >= dia_nasc):
        proximo_aniver = time.struct_time((hoje.tm_year + 1, mes_nasc, dia_nasc, 0, 0, 0, 0, 0, 0))
    else:
        dias_faltam = (mes_nasc - hoje.tm_mon) * 30 + (dia_nasc - hoje.tm_mday)
        print(f"Faltam aproximadamente {dias_faltam} dias para seu aniversário! 🎂")


calcular_idade(1980, 2, 12)