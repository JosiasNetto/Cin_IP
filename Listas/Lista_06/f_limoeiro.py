def comando_fantasia(comando, nome_candidato_fantasia, dic_candidatos_fantasias, dic_rank):
    nome_candidato_fantasia = nome_candidato_fantasia.split(' - ')
    fantasia__reutilizada = False
    dono_fantasia_utilizada = ''

    for i in dic_candidatos_fantasias:
        if nome_candidato_fantasia[1] == dic_candidatos_fantasias[i]:
            fantasia__reutilizada = True
            dono_fantasia_utilizada = i

    if comando == 'Adicionar':
        if nome_candidato_fantasia[0] not in dic_candidatos_fantasias:
            if not fantasia__reutilizada:
                dic_candidatos_fantasias[nome_candidato_fantasia[0]] = nome_candidato_fantasia[1]
                print(f'{nome_candidato_fantasia[0]} é o novo participante do desfile!')
            else:
                print(f'Eita, parece que {nome_candidato_fantasia[0]} tentou usar a fantasia {nome_candidato_fantasia[1]} que ja está sendo utilizada por {dono_fantasia_utilizada }, ele deverá ser desqualificado por plágio')

        else:
            print(f'Opa, parece que {nome_candidato_fantasia[0]} ja consta aqui, voce quis dizer "Atualizar"?')

    elif comando == 'Remover':
        if dic_candidatos_fantasias.get(nome_candidato_fantasia[0], 0) != 0:
            del dic_candidatos_fantasias[nome_candidato_fantasia[0]]
            print(f'Parece que {nome_candidato_fantasia[0]} desistiu...')
        
        else:
            print(f'Hmmm não consegui achar {nome_candidato_fantasia[0]} no banco de dados...')
    
    elif comando == 'Atualizar':
        if dic_candidatos_fantasias.get(nome_candidato_fantasia[0], 0) != 0:
            dic_candidatos_fantasias[nome_candidato_fantasia[0]] = nome_candidato_fantasia[1]
            print(f'Fantasia de {nome_candidato_fantasia[0]} atualizada')

        else:
            print(f'Hmmm não consegui achar {nome_candidato_fantasia[0]} no banco de dados...')

    elif comando == 'Julgar previamente':
        lista_rank = calc_pontuacao(dic_candidatos_fantasias, dic_rank)
        if len(dic_rank) > 0:
            diferenca_pontos = lista_rank[0][1] - lista_rank[1][1]
            print(f'Até o momento, o primeiro colocado é {lista_rank[0][0]} com uma diferença de {diferenca_pontos} pontos para o segundo colocado')
    
    return

def calc_pontuacao(dic_candidatos_fantasias, dic_rank):
    alfabeto_consoantes = ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z')
    lista_rank = []
    

    for i in dic_candidatos_fantasias:
        list_expulsar = []
        contador_conssoantes = 0
        multp_soma = 0
        len_quadrado = len(dic_candidatos_fantasias[i])**2
        
        for j in dic_candidatos_fantasias[i]:
            if j.lower() in alfabeto_consoantes:
                posicao = alfabeto_consoantes.index(j.lower())
                multp_soma *= posicao
                contador_conssoantes += 1

        divisor = multp_soma**(1/contador_conssoantes)
        if divisor != 0:
            pontuacao = len_quadrado/divisor
            dic_rank[i] = pontuacao
        else:
            lista_rank.append(i)
        
    if len(list_expulsar) > 0:
        for i in list_expulsar:
            del dic_candidatos_fantasias[i]

    lista_rank = sorted(dic_rank.items(), key = lambda item : item[1])

    return lista_rank


def main():
    dic_candidatos_fantasias = {}
    dic_rank = {}

    comando = input()
    while comando != 'Fim do desfile':
        nome_candidato_fantasia = input()
        comando_fantasia(comando, nome_candidato_fantasia, dic_candidatos_fantasias, dic_rank)
        comando = input()

    lista_rank = calc_pontuacao(dic_candidatos_fantasias, dic_rank)
    print('=== RESULTADOS DO DESFILE ===')
    if len(dic_rank) > 0:
        for i in dic_rank:
            print(f'{i}---{dic_rank[i]:.1f}')
            print()
        print(f'PARABÉNS {lista_rank[0][0].upper()}!!! VOCÊ ACABA DE VENCER O PRIMEIRO DESFILE DO LIMOEIRO!!')
    
    else:
        print('Parece que não sobrou ninguem na disputa, que pena…')

main()