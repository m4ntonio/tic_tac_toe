# CP02 - Python - Jogo da Velha (Tic Tac Toe) em Python

# --- Função para exibir o tabuleiro ---
def exibir_tabuleiro(tabuleiro):
    print("\n   0   1   2")
    for i, linha in enumerate(tabuleiro):
        print(f" {i}  " + " | ".join(linha))
        if i < 2:
            print("   ---+---+---")
    print()  # Quebra de linha após o tabuleiro

# --- Função para verificar se houve um vencedor ---
def verificar_vencedor(tabuleiro, jogador):
    # Verificar linhas e colunas
    for i in range(3):
        if all([tabuleiro[i][j] == jogador for j in range(3)]) or all([tabuleiro[j][i] == jogador for j in range(3)]):
            return True
    # Verificar diagonais
    if all([tabuleiro[i][i] == jogador for i in range(3)]) or all([tabuleiro[i][2-i] == jogador for i in range(3)]):
        return True
    return False

# --- Função para verificar empate ---
def verificar_empate(tabuleiro):
    return all([celula != " " for linha in tabuleiro for celula in linha])

# --- Função para verificar jogada válida ---
def jogada_valida(tabuleiro, linha, coluna):
    return 0 <= linha < 3 and 0 <= coluna < 3 and tabuleiro[linha][coluna] == " "

# --- Loop principal do jogo ---
def main():
    # Inicializa o tabuleiro vazio
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    while True:
        exibir_tabuleiro(tabuleiro)
        #print()
        entrada = input(f"Jogador {jogador_atual}, escolha a linha (0, 1, 2) ou 's' para sair: ").strip()
        if entrada.lower() == 's':
            print("Jogo encerrado pelo usuário.")
            break
        try:
            linha = int(entrada)
            coluna = int(input(f"Jogador {jogador_atual}, escolha a coluna (0, 1, 2) ou 's' para sair: ").strip())
        except ValueError:
            print("Entrada inválida. Tente novamente.")
            continue
        if not jogada_valida(tabuleiro, linha, coluna):
            print("Jogada inválida. Tente novamente.")
            continue
        tabuleiro[linha][coluna] = jogador_atual
        if verificar_vencedor(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print(f"Parabéns! Jogador {jogador_atual} venceu!")
            break
        if verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("Empate!")
            break

        # Alterna entre X e O
        jogador_atual = "O" if jogador_atual == "X" else "X"

if __name__ == "__main__":
    main()