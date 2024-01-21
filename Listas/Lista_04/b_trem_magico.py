#Função que recebe como parametro os pesos das malas, e os organiza
def organizar_mala(pesos_mala):
    
    #Organizando os pesos em ordem crescente
    pesos_mala.sort()

    #Variaveis de auxilio para salvar o primeiro e segundo peso da lista
    peso_aux0 = pesos_mala[0]
    peso_aux1 = pesos_mala[1]

    #Processo de trocar o primeiro e segundo peso pelo ultimo e penultimo respectivamente
    #Apos trocando o ultimo e o penultimo com o primeiro e o segundo que foram salvos anteriormente
    pesos_mala[0] = pesos_mala[-1]
    pesos_mala[1] = pesos_mala[-2]
    pesos_mala[-1] = peso_aux0
    pesos_mala[-2] = peso_aux1

    #Retornando a lista organizada
    return pesos_mala

#Função que retornar a velocidade, carga e total de pessoas do trem
def parametros(qtd_carvao, peso, num_passageiros):
    
    #Calculos a partir dos parametros recebidos
    velocidade = int((int(qtd_carvao) + 200) / 2)
    carga = int((int(peso) + 4000) / 1000)
    total_pessoas = (int(num_passageiros) + 40)

    #Retornando cada uma das variaveis 
    return velocidade, carga, total_pessoas

#Função que retorna a lista dos funcionarios que irão trabalhar
def turno(funcionarios, hora, num_roteiro):
    convocados = []
            
    #Verificando a hora do turno e o roteiro escolhido 
    #Adciona a lista de convocados a depender das variaveis       
    if int(hora[0]) > 7 and int(hora[0]) < 21:
        if num_roteiro == ('Roteiro 1'):
            convocados.append(funcionarios[0])
            convocados.append(funcionarios[1])
        
        elif num_roteiro == ('Roteiro 2'):
            convocados.append(funcionarios[0])
            convocados.append(funcionarios[-1])
    
    elif int(hora[0]) == 7 and int(hora[1]) > 0:
        if num_roteiro == ('Roteiro 1'):
            convocados.append(funcionarios[0])
            convocados.append(funcionarios[1])
        
        elif num_roteiro == ('Roteiro 2'):
            convocados.append(funcionarios[0])
            convocados.append(funcionarios[-1])
        
    
    else:
        if num_roteiro == ('Roteiro 1'):
            convocados.append(funcionarios[2])
        
    #Retornando a lista de convocados
    return convocados
            

#Definindo a função que organiza todo o processo do trem
def protocolo_de_inicio():

    #Recebendo os pesos das malas, e tranformando em uma lista
    pesos_mala = input().split(', ')
    #Recebendo a lista de malas organizadas a partir da função
    malas_organizadas = organizar_mala(pesos_mala)

    #Imprimindo a lista das malas organizadas
    print(f"A nova organização das malas é a seguinte: ",end='')
    for i in range(len(malas_organizadas)):
        if i < (len(malas_organizadas) - 1):
            print(f'{malas_organizadas[i]}, ',end='')
        else:
            print(f'{malas_organizadas[i]}')


    #Recebendo os parametros, e tranformando em uma lista
    lista_parametros = input().split(', ')
    #Recebendo os valores desejados a partir da função
    velocidade, carga, qtd_passageiros = parametros(lista_parametros[0], lista_parametros[1], lista_parametros[2])

    #Imprimindo os resultados da função
    print(f'A velocidade que o trem partirá é de: {velocidade}Km/H')
    print(f'A carga do Trem em Toneladas é: {carga} Ton.')
    print(f'A quantidade de passageiros é de {qtd_passageiros}')


    #Recebendo os nomes dos funcionarios, e tranformando em uma lista
    lista_funcionarios = input().split(', ')
    #Recebendo a hora, e transformando em uma lista de elementos 'horas' e 'minutos'
    hora = input().split(':')
    #Recebendo o numero do roteiro
    roteiro = input()
    #Recebendo a lista de convocados a partir da execução da função
    lista_convocados = turno(lista_funcionarios, hora, roteiro)

    #Verificando se existem funcionarios na lista, se sim, imprimi o nome de cada um
    if len(lista_convocados) == 0:
        print(f'Os funcionários convocados são: Nenhum! O turno da Madrugada vai ser tranquilo para todos')
    
    else:
        print(f'Os funcionários convocados são: ',end='')
        for i in range(len(lista_convocados)):
            if i < (len(lista_convocados) - 1):
                print(f'{lista_convocados[i]}, ',end='')
            else:
                print(f'{lista_convocados[i]}')


#Executando a função principal
protocolo_de_inicio()
