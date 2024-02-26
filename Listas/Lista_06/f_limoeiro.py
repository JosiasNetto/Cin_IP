def comando_fantasia(comando, nome_candidato_fantasia, dic_candidatos_fantasias): #Função que recebe o comando, e faz o solicitado

    if comando == 'Adicionar' or comando == 'Atualizar':  #Verifica se o comando é atlz ou add, para separar o nome e a fantasia do candidado
        nome_candidato_fantasia = nome_candidato_fantasia.split(' - ')  #Separa o nome e fantasia do candidato em uma lista
        
    if comando == 'Adicionar':  #Verifica se o comando é add
        if nome_candidato_fantasia[0] not in dic_candidatos_fantasias:  #Verifica se o nome do candidato ainda não esta na lista dos atuais
            if not verifica_fantasia_reutilizada(dic_candidatos_fantasias, nome_candidato_fantasia):  #Executa a função que verifica se esta plagiando a fantasia de alguem
              dic_candidatos_fantasias[nome_candidato_fantasia[0]] = nome_candidato_fantasia[1] #Declara o nome como chave e a fantasia como valor no dicionario dos candidatos
              print(f'{nome_candidato_fantasia[0]} é o novo participante do desfile!')  # Imprimi que o participante foi adcionado

        else: #Caso o nome ja esta na lista, printa a respectiva msg
            print(f'Opa, parece que {nome_candidato_fantasia[0]} ja consta aqui, voce quis dizer "Atualizar"?')

    elif comando == 'Remover':  #Verifica se o comando é remover
        if dic_candidatos_fantasias.get(nome_candidato_fantasia, 0) != 0: #Verifica se o nome esta na lista dos candidatos, se não estiver retorna 0 e vai para o else
            del dic_candidatos_fantasias[nome_candidato_fantasia] #Deleta o participante da lista
            print(f'Parece que {nome_candidato_fantasia} desistiu...')  #Printa a msg de delete
        
        else: #Caso o nome não esteja na lista, printa a respectiva msg
            print(f'Hmmm não consegui achar {nome_candidato_fantasia} no banco de dados...')
    
    elif comando == 'Atualizar':  #Verifica se o comando é atualizar
        if dic_candidatos_fantasias.get(nome_candidato_fantasia[0], 0) != 0:  #Verifica se o nome esta na lista, caso não esteja retorna 0 e vai para o else
            if not verifica_fantasia_reutilizada(dic_candidatos_fantasias, nome_candidato_fantasia):  #Executa a função e verifica se a fantasia ja foi utilizada
                dic_candidatos_fantasias[nome_candidato_fantasia[0]] = nome_candidato_fantasia[1] #Atualiza a fantasia do candidato
                print(f'Fantasia de {nome_candidato_fantasia[0]} atualizada') #Imprimi a msg de atlz

            else: #Caso seja uma fantasia ja usada, exclui o participante
                del dic_candidatos_fantasias[nome_candidato_fantasia[0]]
                
        else: #Caso o candidato não esteja na lista do concurso, printa a respectiva msg
            print(f'Hmmm não consegui achar {nome_candidato_fantasia[0]} no banco de dados...')

    elif comando == 'Julgar previamente': #Verifica se o comando é o de julgar
        lista_rank = calc_pontuacao(dic_candidatos_fantasias) #Executa a função que retorna a lista com o rank dos candidatos
        if len(lista_rank) > 0: #Vericica se a lista do rank é maior que 0
          diferenca_pontos = lista_rank[0][1] - lista_rank[1][1]  #Calc diferença pontos entre o 1 e o 2
          print(f'Até o momento, o primeiro colocado é {lista_rank[0][0]} com uma diferença de {diferenca_pontos:.1f} pontos para o segundo colocado')  #Printa a msg da posição
    
    return

def  verifica_fantasia_reutilizada(dic_candidatos_fantasias, nome_candidato_fantasia):  #Função que verifica se a fantasia ja esta sendo usada
    fantasia__reutilizada = False #Caso base, a fantasia não esta sendo usada
    dono_fantasia_utilizada = ''
    for i in dic_candidatos_fantasias:  #Loop que passa pelos candidatos do concurso
        if nome_candidato_fantasia[1] == dic_candidatos_fantasias[i]: #Verifica se a fantasia verificada é igual a fantasia do candidato i
            #Se sim, declara a var como true e salva o nome do dono da fantasia
            fantasia__reutilizada = True  
            dono_fantasia_utilizada = i
    
    if  fantasia__reutilizada:  #Se a fantasia ja estiver sendo utilizada, printa a respectiva msg
        print(f'Eita, parece que {nome_candidato_fantasia[0]} tentou usar a fantasia {nome_candidato_fantasia[1]} que ja está sendo utilizada por {dono_fantasia_utilizada }, ele deverá ser desqualificado por plágio')

    return fantasia__reutilizada  #Retorna a variavel bool que diz se ja esta sendo usada


def calc_pontuacao(dic_candidatos_fantasias): #Função que calcula a pontuação de cada candidato e retorna a lista do rank
    #Declarando variaveis Aux
    alfabeto_consoantes = ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z')
    alfabeto_total = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    lista_rank = []
    list_expulsar = []
    dic_rank = {}
    
    for i in dic_candidatos_fantasias:  #Loop que por cada candidato da competição
        #Declarando variaveis aux para a conta da pontuação
        contador_conssoantes = 0  
        multp_soma = 1

        len_quadrado = len(dic_candidatos_fantasias[i])**2  #Calculando o dividendo da conta(tamanho da str fantasia ao quadrado)
        
        for j in dic_candidatos_fantasias[i]: #Loop que itera as letras da fantasia do candidato atual do loop
            if j.lower() in alfabeto_consoantes:  #Verifica se a letra é uma conssoante
                posicao = alfabeto_total.index(j.lower()) + 1 #Verifica qual a posição da conssoante no alfabeto
                multp_soma = multp_soma * posicao #Multiplica o numero a ser dividido atual, pela posição da conssoante
                contador_conssoantes += 1 #Aumenta 1 no contador de conssoantes

        if contador_conssoantes > 0:  #Verifica se o num de conssoantes é maior que 0 
            divisor = multp_soma**(1/contador_conssoantes)  #Tira a raiz da mult obtida, sendo esse num o divisor
            pontuacao = len_quadrado/divisor  #Calcula a pontuação
            dic_rank[i] = pontuacao #Atribui a pontuação a um dic com a chave nome
        
        else: #Caso não tenha conssoantes, adciona na lista de candidatos a serem expulsos
            list_expulsar.append(i)
        
    if len(list_expulsar) > 0:  #Verifica se existem canidatos para expulsar
        for i in list_expulsar: #Loop que passa pela lista dos expulsos e deleta cada um da lista geral
            del dic_candidatos_fantasias[i]

    lista_rank = sorted(dic_rank.items(), key = lambda item : (-item[1], item[0]))  #Recebe uma lista de tuplas da pessoa com maior pontuação a menor, caso empate, verifica a lexicografia

    return lista_rank #Retorna a lista do rank


def main():
    dic_candidatos_fantasias = {} #Dicionario que guardara o nome do candidato e sua fantasia
    nome_candidato_fantasia= ''

    comando = input() #Recebendo o primeiro comando
    while comando != 'Fim do desfile':  #Loop que so acaba quando a msgde fim eh enviada
        if comando != 'Julgar previamente': #Verifica se não é o comando de julgar, para assim ler o nome do participante
            nome_candidato_fantasia = input() #Recebe o nome e fantasia do participante
        comando_fantasia(comando, nome_candidato_fantasia, dic_candidatos_fantasias)  #Executa a funçao que executa o comando pedido
        comando = input() #Recebe o prox comando

    lista_rank = calc_pontuacao(dic_candidatos_fantasias) #Executa a funão que retorna o rank com as pontuações dos candidatos
    print('=== RESULTADOS DO DESFILE ===')  #Print inicio resultado do desfile
    if len(lista_rank) > 0: #Verifica se o rank tem candidatos
        for i in range(len(lista_rank)):  #Loop que passa pela qtd de pessoas no rank
            print(f'{i + 1}. {lista_rank[i][0]} --- {lista_rank[i][1]:.1f}')  #Printa o lugar, nome e fantasia
            print()
        print(f'PARABÉNS {lista_rank[0][0].upper()}!!! VOCÊ ACABA DE VENCER O PRIMEIRO DESFILE DO LIMOEIRO!!')  #Printa a msg do primeiro colocado
    
    else: #Caso não tenha ninguem no rank, printa a respectiva msg
        print('Parece que não sobrou ninguem na disputa, que pena…')

main()