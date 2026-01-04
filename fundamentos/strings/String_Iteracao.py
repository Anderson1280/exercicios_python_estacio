import random


def exibir_menu():
    """Exibe o menu de opções do jogo"""
    print("\n" + "=" * 40)
    print("🎮 JOKENPÔ - PEDRA, PAPEL E TESOURA 🎮")
    print("=" * 40)
    print("Escolha sua jogada:")
    print("1 - 🪨 Pedra")
    print("2 - 📄 Papel")
    print("3 - ✂️  Tesoura")
    print("0 - 🚪 Sair do jogo")
    print("-" * 40)


def obter_jogada_usuario():
    """Obtém e valida a jogada do usuário"""
    while True:
        try:
            escolha = int(input("Digite sua escolha (0-3): "))
            if escolha in [0, 1, 2, 3]:
                return escolha
            else:
                print("❌ Opção inválida! Digite apenas 0, 1, 2 ou 3.")
        except ValueError:
            print("❌ Por favor, digite apenas números!")


def obter_jogada_maquina():
    """Gera jogada aleatória da máquina"""
    return random.randint(1, 3)


def converter_jogada_para_texto(jogada):
    """Converte número da jogada para texto"""
    opcoes = {
        1: "🪨 Pedra",
        2: "📄 Papel",
        3: "✂️ Tesoura"
    }
    return opcoes[jogada]


def determinar_vencedor(usuario, maquina):
    """Determina o vencedor da rodada"""
    # Empate
    if usuario == maquina:
        return "empate"

    # Vitórias do usuário
    vitorias_usuario = [
        (1, 3),  # Pedra vence Tesoura
        (2, 1),  # Papel vence Pedra
        (3, 2)  # Tesoura vence Papel
    ]

    if (usuario, maquina) in vitorias_usuario:
        return "usuario"
    else:
        return "maquina"


def exibir_resultado(jogada_usuario, jogada_maquina, resultado):
    """Exibe o resultado da rodada"""
    print(f"\n🎯 RESULTADO DA RODADA:")
    print(f"Você escolheu: {converter_jogada_para_texto(jogada_usuario)}")
    print(f"Máquina escolheu: {converter_jogada_para_texto(jogada_maquina)}")

    if resultado == "empate":
        print("🤝 EMPATE! Vocês escolheram a mesma jogada!")
    elif resultado == "usuario":
        print("🎉 VOCÊ VENCEU! Parabéns!")
    else:
        print("🤖 MÁQUINA VENCEU! Tente novamente!")


def exibir_placar(vitorias_usuario, vitorias_maquina, empates):
    """Exibe o placar atual"""
    print(f"\n📊 PLACAR ATUAL:")
    print(f"Você: {vitorias_usuario} vitórias")
    print(f"Máquina: {vitorias_maquina} vitórias")
    print(f"Empates: {empates}")
    print("-" * 40)


def exibir_placar_final(vitorias_usuario, vitorias_maquina, empates, total_rodadas):
    """Exibe estatísticas finais do jogo"""
    print("\n" + "=" * 40)
    print("📈 ESTATÍSTICAS FINAIS")
    print("=" * 40)
