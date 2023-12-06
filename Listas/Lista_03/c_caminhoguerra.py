#Variaveis auxilio codigo
itens_achados_missao = []
itens_faltam_missao = []
achou_algo = False
#Recebendo os itens que percy quer, e os que achou, e transformando em listas
itens_desejo = input().split(", ")
itens_achados = input().split(", ")

#Loop que passa por cada item que percy deseja
for item in itens_desejo:
    #Verificanção se o item que deseja esta na lista dos que achou
    if item in itens_achados:
        #Se achar, adciona a lista de itens achados e que precisa usar
        itens_achados_missao.append(item)
        #itens_para_missao += itens_desejo.pop(itens_desejo.index(item))
        achou_algo = True
    else:
        #Se não estiver, adciona na lista de itens que faltam
        itens_faltam_missao.append(item)

#Verificação para ver se achou algum item
if achou_algo:

    #Imprimindo todos os itens que achou e ira usar
    print("Estes são os itens que já tenho no Acampamento Meio-Sangue:")
    for i in range(len(itens_achados_missao)):
            print(f"{i + 1}º item: {itens_achados_missao[i]}")

    #Verificando se falta algum item, e imprimindo a fala dependendo da situação
    ##Se a lista de faltar for vazia, não falta nenhum item
    if itens_faltam_missao == []:
        print(f"Perfeito, encontrei todos os {len(itens_achados_missao)} itens aqui no Acampamento Meio-Sangue!")

    else:
        print(f"Vou precisar adquirir {len(itens_faltam_missao)} itens antes da batalha!")

else:
    print(f"Hmm, preciso visitar um vendedor ambulante! Não encontrei nenhum dos {len(itens_desejo)} itens aqui no Acampamento Meio-Sangue.")

#Imprimindo mensagem final
print(f"Estou pronto para a batalha! Que comece a guerra contra os Titãs!")