def comando_fantasia(comando, nome_candidato_fantasia, dic_candidatos_fantasias):   

    if comando == 'Adicionar' or comando == 'Atualizar':
        nome_candidato_fantasia = nome_candidato_fantasia.split(' - ')
        

    if comando == 'Adicionar':
        if nome_candidato_fantasia[0] not in dic_candidatos_fantasias:
            if not verifica_fantasia_reutilizada(dic_candidatos_fantasias, nome_candidato_fantasia):
              dic_candidatos_fantasias[nome_candidato_fantasia[0]] = nome_candidato_fantasia[1]
              print(f'{nome_candidato_fantasia[0]} é o novo participante do desfile!')

        else:
            print(f'Opa, parece que {nome_candidato_fantasia[0]} ja consta aqui, voce quis dizer "Atualizar"?')

    elif comando == 'Remover':
        if dic_candidatos_fantasias.get(nome_candidato_fantasia, 0) != 0:
            del dic_candidatos_fantasias[nome_candidato_fantasia]
            print(f'Parece que {nome_candidato_fantasia} desistiu...')
        
        else:
            print(f'Hmmm não consegui achar {nome_candidato_fantasia} no banco de dados...')
    
    elif comando == 'Atualizar':
        if dic_candidatos_fantasias.get(nome_candidato_fantasia[0], 0) != 0:
            if not verifica_fantasia_reutilizada(dic_candidatos_fantasias, nome_candidato_fantasia):
                dic_candidatos_fantasias[nome_candidato_fantasia[0]] = nome_candidato_fantasia[1]
                print(f'Fantasia de {nome_candidato_fantasia[0]} atualizada')

            else:
                del dic_candidatos_fantasias[nome_candidato_fantasia[0]]
                
        else:
            print(f'Hmmm não consegui achar {nome_candidato_fantasia[0]} no banco de dados...')

    elif comando == 'Julgar previamente':
        lista_rank = calc_pontuacao(dic_candidatos_fantasias)
        if len(lista_rank) > 0:
            diferenca_pontos = lista_rank[0][1] - lista_rank[1][1]
            print(f'Até o momento, o primeiro colocado é {lista_rank[0][0]} com uma diferença de {diferenca_pontos:.1f} pontos para o segundo colocado')
    
    return

def  verifica_fantasia_reutilizada(dic_candidatos_fantasias, nome_candidato_fantasia):
    fantasia__reutilizada = False
    dono_fantasia_utilizada = ''
    for i in dic_candidatos_fantasias:
        if nome_candidato_fantasia[1] == dic_candidatos_fantasias[i]:
            fantasia__reutilizada = True
            dono_fantasia_utilizada = i
    
    if  fantasia__reutilizada:
        print(f'Eita, parece que {nome_candidato_fantasia[0]} tentou usar a fantasia {nome_candidato_fantasia[1]} que ja está sendo utilizada por {dono_fantasia_utilizada }, ele deverá ser desqualificado por plágio')

    return fantasia__reutilizada


def calc_pontuacao(dic_candidatos_fantasias):
    alfabeto_consoantes = ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z')
    alfabeto_total = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    lista_rank = []
    list_expulsar = []
    dic_rank = {}
    

    for i in dic_candidatos_fantasias:
        contador_conssoantes = 0
        multp_soma = 1
        len_quadrado = len(dic_candidatos_fantasias[i])**2
        
        for j in dic_candidatos_fantasias[i]:
            if j.lower() in alfabeto_consoantes:
                posicao = alfabeto_total.index(j.lower()) + 1
                multp_soma = multp_soma * posicao
                contador_conssoantes += 1

        if contador_conssoantes != 0:
            divisor = multp_soma**(1/contador_conssoantes)
            pontuacao = len_quadrado/divisor
            dic_rank[i] = pontuacao 
        else:
            list_expulsar.append(i)
        
    if len(list_expulsar) > 0:
        for i in list_expulsar:
            del dic_candidatos_fantasias[i]

    lista_rank = sorted(dic_rank.items(), key = lambda item : item[1], reverse=True)

    return lista_rank

def verificando_empate(lista_rank):
    contador = 0
    for i in range(1,len(lista_rank)):
        if lista_rank[i][1] == lista_rank[0][1]:
            contador += 1
    
    lista_rank_aux = sorted(lista_rank[:contador + 1], reverse= True)
    for i in range(len(lista_rank_aux)):
        lista_rank[i] = lista_rank_aux[i]

    return


def main():
    dic_candidatos_fantasias = {} #Dicionario que guardara o nome do candidato e sua fantasia
    nome_candidato_fantasia= ''

    comando = input() #Recebendo o primeiro comando
    while comando != 'Fim do desfile':  #Loop que so acaba quando a msgde fim eh enviada
        if comando != 'Julgar previamente': #Verifica se não é o comando de julgar, para assim ler o nome do participante
            nome_candidato_fantasia = input() #Recebe o nome e fantasia do participante
        comando_fantasia(comando, nome_candidato_fantasia, dic_candidatos_fantasias)  #Executa a funçao que executa o comando pedido
        comando = input() #Recebe o prox comando

    lista_rank = calc_pontuacao(dic_candidatos_fantasias)
    print('=== RESULTADOS DO DESFILE ===')
    if len(lista_rank) > 0:
        if len(lista_rank) > 1:
            verificando_empate(lista_rank)
        contador = 1
        for i in range(len(lista_rank)):
            print(f'{i + 1}. {lista_rank[i][0]} --- {lista_rank[i][1]:.1f}')
            print()
            contador += 1
        print(f'PARABÉNS {lista_rank[0][0].upper()}!!! VOCÊ ACABA DE VENCER O PRIMEIRO DESFILE DO LIMOEIRO!!')
    
    else:
        print('Parece que não sobrou ninguem na disputa, que pena…')

main()