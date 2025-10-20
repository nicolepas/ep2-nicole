def define_posicoes(linha,coluna,orientacao,tamanho):
    posicoes = []
    
    if orientacao == "vertical":
        for i in range(tamanho):
            posicoes.append([linha + i, coluna])
    elif orientacao == "horizontal":
        for i in range(tamanho):
            posicoes.append([linha, coluna + i])
    
    return posicoes

def preenche_frota(frota,nome,linha,coluna,orientacao,tamanho):
    posicoes = define_posicoes(linha,coluna,orientacao,tamanho)

    if nome not in frota:
        frota[nome] = []

    frota[nome].append(posicoes)
    return frota


def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

def posiciona_frota(frota):
    tabuleiro = []
    for i in range(10):
        tabuleiro.append([0] * 10)

    for navios in frota.values():
        for posicoes in navios:
            for linha, coluna in posicoes:
                tabuleiro[linha][coluna] = 1  
                
    return tabuleiro


def afundados(frota,tabuleiro):
    qnt = 0

    for navios in frota.values():          
        for navio in navios:                 
            acertos = 0                      
            for linha,coluna in navio:      
                if tabuleiro[linha][coluna] == 'X':
                    acertos += 1
            if acertos == len(navio):        
                qnt += 1

    return qnt

def posicao_valida(frota,linha,coluna,orientacao,tamanho):
    novo = define_posicoes(linha,coluna,orientacao,tamanho)

    for posicao in novo:
        l, c = posicao
        if l < 0 or l > 9 or c < 0 or c > 9:
            return False  

    for lista in frota.values():
        for navio in lista:
            for posicao in navio:
                for nova_posicao in novo:
                    if posicao == nova_posicao:
                        return False  

    return True


