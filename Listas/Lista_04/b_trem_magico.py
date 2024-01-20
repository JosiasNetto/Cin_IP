def organizar_mala(pesos_mala):
    pesos_mala.sort()
    peso_aux0 = pesos_mala[0]
    peso_aux1 = pesos_mala[1]
    pesos_mala[0] = pesos_mala[-1]
    pesos_mala[1] = pesos_mala[-2]
    pesos_mala[-1] = peso_aux0
    pesos_mala[-2] = peso_aux1
    #Pode ser que nao organize na ordem por nao ser inteiros
    #E se tiver menos de 4 pesos? Pode ser o problema

    return pesos_mala

def parametros(qtd_carvao, peso, num_passageiros):
    
    velocidade = int((int(qtd_carvao) + 200) / 2)
    carga = int((int(peso) + 4000) / 1000)
    total_pessoas = (int(num_passageiros) + 40)

    return velocidade, carga, total_pessoas

def turno(funcionarios, hora, num_roteiro):
    convocados = []
            
    if hora[0] == '0':
        if hora[1] == '7' and (hora[3] != '0' or hora[4] != '0'):
            if num_roteiro == ('Roteiro 1'):
                convocados.append(funcionarios[0])
                convocados.append(funcionarios[1])
            
            elif num_roteiro == ('Roteiro 2'):
                convocados.append(funcionarios[0])
                convocados.append(funcionarios[-1])
        
        elif int(hora[1]) > 7:
            if num_roteiro == ('Roteiro 1'):
                convocados.append(funcionarios[0])
                convocados.append(funcionarios[1])
            
            elif num_roteiro == ('Roteiro 2'):
                convocados.append(funcionarios[0])
                convocados.append(funcionarios[-1])
        
        else:
            if num_roteiro == ('Roteiro 1'):
                convocados.append(funcionarios[2])
        
                    
    elif hora[0] == '1':
        if num_roteiro == ('Roteiro 1'):
            convocados.append(funcionarios[0])
            convocados.append(funcionarios[1])
        
        elif num_roteiro == ('Roteiro 2'):
                convocados.append(funcionarios[0])
                convocados.append(funcionarios[-1])
    
    elif hora[0] == '2' and hora[1] == '0':
        if num_roteiro == ('Roteiro 1'):
            convocados.append(funcionarios[0])
            convocados.append(funcionarios[1])
        
        elif num_roteiro == ('Roteiro 2'):
                convocados.append(funcionarios[0])
                convocados.append(funcionarios[-1])
    
    else:
        if num_roteiro == ('Roteiro 1'):
            convocados.append(funcionarios[2])
        
    
    return convocados
            

def protocolo_de_inicio():

    pesos_mala = input().split(', ')
    malas_organizadas = organizar_mala(pesos_mala)
    print(f"A nova organização das malas é a seguinte: ",end='')
    for i in range(len(malas_organizadas)):
        if i < (len(malas_organizadas) - 1):
            print(f'{malas_organizadas[i]}, ',end='')
        else:
            print(f'{malas_organizadas[i]}')


    lista_parametros = input().split(', ')
    velocidade, carga, qtd_passageiros = parametros(lista_parametros[0], lista_parametros[1], lista_parametros[2])
    print(f'A velocidade que o trem partirá é de: {velocidade}Km/H')
    print(f'A carga do Trem em Toneladas é: {carga} Ton.')
    print(f'A quantidade de passageiros é de {qtd_passageiros}')

    lista_funcionarios = input().split(', ')
    hora = input().split()
    roteiro = input()
    lista_convocados = turno(lista_funcionarios, hora, roteiro)
    if len(lista_convocados) == 0:
        print(f'Os funcionários convocados são: Nenhum! O turno da Madrugada vai ser tranquilo para todos')
    
    else:
        print(f'Os funcionários convocados são: {lista_convocados}"')

protocolo_de_inicio()

#Printar cada funcionario individulamte
#Nao eh o sorquito