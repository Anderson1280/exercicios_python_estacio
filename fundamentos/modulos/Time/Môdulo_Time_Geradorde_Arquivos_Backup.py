import time


def criar_backup():
    agora = time.localtime()

    # Cria nome único com data e hora
    nome_arquivo = f"backup_{agora.tm_year}{agora.tm_mon:02d}{agora.tm_mday:02d}_{agora.tm_hour:02d}{agora.tm_min:02d}.zip"

    print(f"📦 Criando: {nome_arquivo}")
    # Aqui viria o código real de backup


criar_backup()
# Saída: backup_20251010_1430.zip