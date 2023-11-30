nome_amigo = ""
local_show = ""
valor_ingresso = 0
valor_carteira = 0
tempo_grad = 0
numero_amigos = 0
melhor_computador_ingresso = 0
melhor_posicao_ingresso = 1000
numero_ingressos = 0
posicao_fila = 0
amigo_terminou = False

computadores_disponiveis = int(input())
valor_carteira = int(input())
tempo_grad = int(input())

while nome_amigo != "end" and numero_amigos < computadores_disponiveis:
    nome_amigo = input()
    if nome_amigo != "laura" and nome_amigo != "carlos" and nome_amigo != "roberto" and nome_amigo != "end":
        numero_amigos += 1
  

if numero_amigos > 0:
    print(f"Bom começo! Consegui {numero_amigos} amigos que podem me ajudar a comprar o ingresso")
    
    for i in range(1,numero_amigos + 1):
        valor_ingresso = 0
        local_show = ""
        amigo_terminou = False
        while not amigo_terminou and local_show != "end":            
            valor_ingresso = int(input())
            local_show = input()
            if local_show == "rio de janeiro" or local_show == "são paulo" or local_show == "buenos aires":
                print("Consegui um ingresso em um local que João possa ir! Agora temos que ver o preço")

                if valor_ingresso <= valor_carteira:
                    print("Consegui o dinheiro! Agora só falta ver a minha colocação na fila dos ingressos...")
                    posicao_fila = int(input())
                    amigo_terminou = True
        
                    if (posicao_fila / 160) <= tempo_grad:
                        print("ISSOOO, conseguimos um ingresso!!!")
                        numero_ingressos += 1
                        if posicao_fila < melhor_posicao_ingresso:
                            melhor_computador_ingresso = i
                            melhor_posicao_ingresso = posicao_fila
                    else:
                        print(f"Caramba, essa foi quase! Mas infelizmente não consegui um bom lugar na fila dos ingressos no computador de número {i}")
                else:
                    print("Caramba! Só tinha ingresso para a pista vip, que está bem acima do meu orçamento.")
                    amigo_terminou = True
    if numero_ingressos >= 1:
        print(f"Consegui o ingresso! Com {int((numero_ingressos/numero_amigos)*100)}% de aproveitamento da ajuda dos meus amigos. E a fila escolhida para comprar o ingresso foi do computador número {melhor_computador_ingresso}. Rumo ao show da Taylor!!!")
    elif (computadores_disponiveis / 2) < numero_amigos:
        print("Não acredito que tive amigos para ocuparem mais da metade dos computadores, e ainda assim não consegui um ingresso...")
    else:
        print("Poxa, não acredito que não consegui o ingresso, acho que eu devia ter chamado mais amigos para ajudar.")

else:
    print("Ah não! João não conseguiu nenhum amigo que o ajudasse. Agora ele vai ter que contar com a sorte para pegar um bom lugar na fila, usando apenas seu computador.")