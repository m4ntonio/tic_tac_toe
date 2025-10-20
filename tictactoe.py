# CP02 - Python - Jogo da Velha (Tic Tac Toe) em Python

# Cores para o terminal
COR_VERMELHA = '\033[91m'
COR_VERDE = '\033[92m'
COR_AMARELA = '\033[93m'
COR_RESET = '\033[0m'

# Função para exibir o tabuleiro
def exibir_tabuleiro(tabuleiro):
    print("\n    0   1   2")
    for i, linha in enumerate(tabuleiro):
        print(f" {i}  " + " | ".join(linha))
        if i < 2:
            print("   ---+---+---")
    print()

# Funções de verificação
def verificar_vencedor(tabuleiro, jogador):
    for i in range(3):
        if all([tabuleiro[i][j] == jogador for j in range(3)]) or all([tabuleiro[j][i] == jogador for j in range(3)]):
            return True
    if all([tabuleiro[i][i] == jogador for i in range(3)]) or all([tabuleiro[i][2-i] == jogador for i in range(3)]):
        return True
    return False

def verificar_empate(tabuleiro):
    return all([celula != " " for linha in tabuleiro for celula in linha])

# A função jogada_valida agora só precisa checar se a célula está vazia,
# pois a validação do número (0-2) será feita antes.
def posicao_esta_livre(tabuleiro, linha, coluna):
    return tabuleiro[linha][coluna] == " "

# FUNÇÃO PARA OBTER E VALIDAR A JOGADA
def obter_jogada_valida(jogador, tipo_jogada):
    while True:
        prompt = f"Jogador {jogador}, escolha a {tipo_jogada} (0, 1, 2) ou 's' para sair: "
        entrada = input(prompt).strip().lower()

        if entrada == 's':
            return None  # Sinaliza que o jogador quer sair

        # Tenta converter para número e validar o intervalo
        try:
            numero = int(entrada)
            if 0 <= numero <= 2:
                return numero  # Retorna o número válido
            else:
                # O número está fora do intervalo permitido (0, 1, 2)
                print(f"\n{COR_VERMELHA}Jogada inválida. Por favor, escolha um número entre 0 e 2.{COR_RESET}")
        except ValueError:
            # A entrada não era um número
            print(f"\n{COR_VERMELHA}Entrada inválida. Por favor, digite um NÚMERO (0, 1 ou 2).{COR_RESET}")

# Loop principal do jogo
def main():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    while True:
        exibir_tabuleiro(tabuleiro)
        
        # OBTENDO E VALIDANDO A JOGADA
        while True:
            linha = obter_jogada_valida(jogador_atual, "linha")
            if linha is None: # Se o jogador digitou 's'
                break

            coluna = obter_jogada_valida(jogador_atual, "coluna")
            if coluna is None: # Se o jogador digitou 's'
                break

            # Agora que temos certeza que linha e coluna são 0, 1 ou 2,
            # só precisamos verificar se a posição está livre.
            if posicao_esta_livre(tabuleiro, linha, coluna):
                tabuleiro[linha][coluna] = jogador_atual
                print(f"\nJogador {jogador_atual} jogou na linha {linha} e coluna {coluna}")
                break # Sai do loop de tentativa de jogada e continua o jogo
            else:
                print(f"\n{COR_VERMELHA}Posição ({linha}, {coluna}) já está ocupada. Tente novamente.{COR_RESET}")
                # Continua no loop para pedir uma nova jogada
        
        # Se o jogador pediu para sair em qualquer um dos inputs
        if linha is None or coluna is None:
            print(f"\n{COR_AMARELA}Jogo encerrado pelo usuário.{COR_RESET}")
            break

        # VERIFICANDO O ESTADO DO JOGO
        if verificar_vencedor(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print(f"\n{COR_VERDE}Parabéns! Jogador {jogador_atual} venceu!{COR_RESET}")
            break
            
        if verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print(f"\n{COR_AMARELA}Empate!{COR_RESET}")
            break

        # Alterna entre X e O
        jogador_atual = "O" if jogador_atual == "X" else "X"

if __name__ == "__main__":
    main()
