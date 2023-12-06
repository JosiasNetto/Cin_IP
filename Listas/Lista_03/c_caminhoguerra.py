itens_desejo = input().split(", ")
itens_achados = input().split(", ")
itens_para_missao = []
itens_faltam = []
num_item = 1

for item in itens_desejo:
    if item in itens_achados:
        itens_para_missao = itens_desejo.pop(itens_desejo.index(item))

for i in range(len(itens_para_missao)):
    print(f"{i}º item: {itens_para_missao[i]}")