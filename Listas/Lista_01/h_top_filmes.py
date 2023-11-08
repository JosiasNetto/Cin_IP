#Recebendo nome, nota e critica de 3 filmes e ja calculando sua nota final
nome_filme1 = (input())
pontuacao_global_filme1 = int(input())
critica_filme1 = input()

nome_filme2 = (input())
pontuacao_global_filme2 = int(input())
critica_filme2 = input()

nome_filme3 = (input())
pontuacao_global_filme3 = int(input())
critica_filme3 = input()

#Calculando Notas Finais
if critica_filme1 == "boa":
    pontuacao_global_filme1 *= 1.25

elif critica_filme1 == "media":
    pontuacao_global_filme1 *= 1

elif critica_filme1 == "ruim":
    pontuacao_global_filme1 *= 0.75

elif critica_filme1 == "pessima":
    pontuacao_global_filme1 = 0

#Calculando Nota Final 2
if critica_filme2 == "boa":
    pontuacao_global_filme2 *= 1.25

elif critica_filme2 == "media":
    pontuacao_global_filme2 *= 1

elif critica_filme2 == "ruim":
    pontuacao_global_filme2 *= 0.75

elif critica_filme2 == "pessima":
    pontuacao_global_filme2 = 0

#Calculando Nota Final 3
if critica_filme3 == "boa":
    pontuacao_global_filme3 *= 1.25

elif critica_filme3 == "media":
    pontuacao_global_filme3 *= 1

elif critica_filme3 == "ruim":
    pontuacao_global_filme3 *= 0.75

elif critica_filme3 == "pessima":
    pontuacao_global_filme3 = 0

#Calculando Ranking dos Filmes
top1 = str()
top2 = str()
top3 = str()

#Se o filme eh maior que algum dos 2 comparados, ele é automaticamente o top 2, se ele for maior que os 2, sera o top1
if pontuacao_global_filme1 > pontuacao_global_filme2 or pontuacao_global_filme1 > pontuacao_global_filme3:
    if pontuacao_global_filme1 > pontuacao_global_filme2 and pontuacao_global_filme1 > pontuacao_global_filme3:
        top1 = nome_filme1
    else:
        top2 = nome_filme1
else:
    top3 = nome_filme1

if pontuacao_global_filme2 > pontuacao_global_filme1 or pontuacao_global_filme2 > pontuacao_global_filme3:
    if pontuacao_global_filme2 > pontuacao_global_filme1 and pontuacao_global_filme2 > pontuacao_global_filme3:
        top1 = nome_filme2
    else:
        top2 = nome_filme2
else:
    top3 = nome_filme2

if pontuacao_global_filme3 > pontuacao_global_filme1 or pontuacao_global_filme3 > pontuacao_global_filme2:
    if pontuacao_global_filme3 > pontuacao_global_filme1 and pontuacao_global_filme3 > pontuacao_global_filme2:
        top1 = nome_filme3
    else:
        top2 = nome_filme3
else:
    top3 = nome_filme3

#Imprimindo Ranking dos filmes e se tem algum pessimo
print("**** TOP 3 FILMES ****")

print(f"{top1} está em 1° lugar")
print(f"{top2} está em 2° lugar")
print(f"{top3} está em 3° lugar")
if critica_filme1 == "pessima" or critica_filme2 == "pessima" or critica_filme3 == "pessima":
    print(f"{top3} teve uma crítica péssima")
