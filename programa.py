from funcoes import define_posicoes,preenche_frota,faz_jogada,posiciona_frota, afundados,posicao_valida

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
