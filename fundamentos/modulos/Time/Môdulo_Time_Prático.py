import time

# Obtém o tempo atual local
agora = time.localtime()

print(f"Ano: {agora.tm_year}")
print(f"Mês: {agora.tm_mon}")
print(f"Dia: {agora.tm_mday}")
print(f"Hora: {agora.tm_hour}:{agora.tm_min}:{agora.tm_sec}")
print(f'Local: {agora.tm_zone}')
# Também pode acessar por índice
print(f"Ano (por índice): {agora[0]}")