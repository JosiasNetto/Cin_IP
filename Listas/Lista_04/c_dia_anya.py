#Funcao que lista cada elemento de uma lista, um de cada vez
def listando_itens(lista):
    for i in range(len(lista)):
            if i < len(lista) - 1:
                print(f'{lista[i]}, ',end='')
            
            else:
                print(f'{lista[i]}.')


#Funcao que soma os valores dos numeros ASCII 
def soma_valores(lista_valores):
    somatorio = 0
    for num in range(len(lista_valores)):
        somatorio += int(lista_valores[num])
    
    return somatorio


#Funcao que decodifica o nome dos presentes da Anya
def decodificando_presentes(Lista_valores):
    nome_presente = []
    #Loop que converte o numero ASCII em letra, e a adciona na lista do nome do presente
    for num in range(len(Lista_valores)):
        nome_presente.append(chr(int(Lista_valores[num])))
    
    #Retorna uma lista onde cada elemento eh uma letra do presente
    return nome_presente


#Funcao principal que organiza tudo em um unico codigo
def presentes_anya():
    #Variaveis de auxilio para o codigo
    lista_presentes_excluidos = []
    lista_presentes = []
    #Recebendo o numero de presentes a decodificar
    num_presentes = int(input())

    #Loop que passa pelo numero de presentes
    for num in range(num_presentes):
        #Recebe o nome do presente codificado e o separa em uma lista
        presente_codificado = input().split(' ')

        #Executa e recebe o somatorio dos valores do presente codificado
        total_valor = soma_valores(presente_codificado)

        #Executa e recebe o nome do presente decodificado em uma lista
        presente_decodificado = decodificando_presentes(presente_codificado)
        #Transforma a lista do nome do presente em uma string
        presente_decodificado = ''.join(presente_decodificado)

        #Verifica se o presente ja esta lista
        if presente_decodificado not in lista_presentes:
            #Se nao estiver, adciona o presente a lista e imprimi a mensagem
            lista_presentes.append(presente_decodificado)
            print(f'{presente_decodificado} ',end='')
            print(f'foi adicionado a lista ultrassecreta de presentes da Anya!!')
            
            #Verifica se o somatorio dos valores do presente eh impar e se for, o adciona a lista dos que serao excluidos
            if (total_valor % 2) != 0:
                lista_presentes_excluidos.append(presente_decodificado)
                
        #Se ja estiver, avisa que eh um presente repitido       
        else:
            print(f'{presente_decodificado} já está na lista de presentes da Anya!!')


    #Verifica se existem presentes a ser excluidos
    if len(lista_presentes_excluidos) > 0:
        #Se sim, imprimi quais serao e os exclui da lista
        print(f'Infelizmente o Twilight é mão de vaca e os seguintes itens precisaram ser excluídos da lista de presentes ultrassecretos da Anya: ',end='')
        listando_itens(lista_presentes_excluidos)

        #Loop que passa pela lista dos excluidos, e verifica se o presente esta na lista normal, e o exclui
        for i in range(len(lista_presentes_excluidos)):
            if lista_presentes_excluidos[i] in lista_presentes:
                lista_presentes.remove(lista_presentes_excluidos[i])
        
        #Verifica se ainda ha presentes na lista, se tiver, os lista
        if len(lista_presentes) > 0:
            print(f'Lista final dos melhores presentes da Anya: ',end='')
            listando_itens(lista_presentes)
        
        #Se nao tiver, imprimi a mensagem para comprar
        else:
            print(f'O quê? Nenhum presente? Isso é um absurdo! Vamos corrigir essa injustiça e garantir que Anya tenha um Dia das Crianças inesquecível!')

    
    #Verifica se ha presentes na lista, se tiver, os lista um a um
    elif len(lista_presentes) > 0:
        print(f'Parece que o Dia das Crianças desse ano será especial!!!! Anya ganhará todos os presentes planejados, mesmo que ela não seja tão exemplar como deveria…')
        print(f'Lista final dos melhores presentes da Anya: ',end='')
        listando_itens(lista_presentes)

    
    #Caso nao tenha, imprimi a mensagem para comprar
    else:
        print(f'O quê? Nenhum presente? Isso é um absurdo! Vamos corrigir essa injustiça e garantir que Anya tenha um Dia das Crianças inesquecível!')


#Executa a funcao principal
presentes_anya()