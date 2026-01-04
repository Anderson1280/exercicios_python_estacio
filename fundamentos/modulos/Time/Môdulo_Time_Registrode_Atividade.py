import time


def registrar_atividade(acao):
    momento = time.localtime()

    log = f"[{momento.tm_year}-{momento.tm_mon:02d}-{momento.tm_mday:02d} "
    log += f"{momento.tm_hour:02d}:{momento.tm_min:02d}:{momento.tm_sec:02d}] "
    log += f"{acao}"

    print(log)
    # Aqui você salvaria em um arquivo


registrar_atividade("Usuário fez login")
registrar_atividade("Usuário acessou relatório")
registrar_atividade("Usuário fez logout")