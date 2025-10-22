from funcoes import define_posicoes,preenche_frota,faz_jogada,posiciona_frota, afundados,posicao_valida, monta_tabuleiros

navios = [
    ("porta-aviões", 4, 1),
    ("navio-tanque", 3, 2),
    ("contratorpedeiro", 2, 3),
    ("submarino", 1, 4)
]

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": []
}

for n, t, q in navios:
    i = 0
    while i < q:
        print(f"Insira as informações referentes ao navio {n} que possui tamanho {t}")
        linha = int(input("Linha: "))
        col = int(input("Coluna: "))

        if linha < 0 or linha > 9 or col < 0 or col > 9:
            print("Posição fora do tabuleiro!")
        else:
            linha = int(linha)
            col = int(col)
            if linha < 0 or linha > 9 or col < 0 or col > 9:
                print("Valores fora do tabuleiro!")
            else:
                if t == 1:
                    d = "horizontal"
                    if posicao_valida(frota, linha, col, d, t):
                        preenche_frota(frota, n, linha, col, d, t)
                        i = i + 1
                    else:
                        print("Esta posição não está válida!")
                else:
                    direcao = input("[1] Vertical [2] Horizontal >").strip()
                    if direcao == "1":
                        d = "vertical"
                    elif direcao == "2":
                        d = "horizontal"
                    else:
                        print("Entrada inválida para orientação!")
                        d = ""
                    if d != "":
                        if posicao_valida(frota, linha, col, d, t):
                            preenche_frota(frota, n, linha, col, d, t)
                            i = i + 1
                        else:
                            print("Esta posição não está válida!")

print(frota)

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}


tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)

total_navios = 0
for lista in frota_oponente.values():
    total_navios = total_navios + len(lista)

acabou = False
while not acabou:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    linha = int(input("Linha do ataque: "))
    while linha < 0 or linha > 9:
        print("Linha inválida!")
        linha = int(input("Linha do ataque: "))


    coluna = int(input("Coluna do ataque: "))
    while coluna < 0 or coluna > 9:
        print("Coluna inválida!")
        coluna = int(input("Coluna do ataque: "))

    if tabuleiro_oponente[linha][coluna] == 'X' or tabuleiro_oponente[linha][coluna] == '-':
        print("A posição linha", linha, "e coluna", coluna, "já foi informada anteriormente!")
    else:
        tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

        if tabuleiro_oponente[linha][coluna] == 'X':
            print("Você acertou um navio!")
        else:
            print("Você errou o tiro!")

        if afundados(frota_oponente, tabuleiro_oponente) == total_navios:
            print("Parabéns! Você derrubou todos os navios do seu oponente!")
            acabou = True
