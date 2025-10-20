# ordem das embarcações: (nome, tamanho, quantidade)
ordem = [
    ("porta-aviões", 4, 1),
    ("navio-tanque", 3, 2),
    ("contratorpedeiro", 2, 3),
    ("submarino", 1, 4)
]

# dicionário da frota
frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": []
}

for nome, tamanho, quantidade in ordem:
    for i in range(quantidade):
        print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")

        valido = False  

        while not valido:
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))

            if nome == "submarino":
                orientacao = "vertical"  
            else:
                orientacao_num = int(input("[1] Vertical [2] Horizontal >"))
                if orientacao_num == 1:
                    orientacao = "vertical"
                else:
                    orientacao = "horizontal"

            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                valido = True  
            else:
                print("Esta posição não está válida!")

print(frota)
