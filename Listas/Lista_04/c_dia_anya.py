def listando_itens(lista):
    for i in range(len(lista)):
            if i < len(lista) - 1:
                print(f'{lista[i]}, ',end='')
            
            else:
                print(f'{lista[i]}.')

def soma_valores(lista_valores):
    somatorio = 0
    for num in range(len(lista_valores)):
        somatorio += int(lista_valores[num])
    
    return somatorio

def decodificando_presentes(Lista_valores):
    nome_presente = []
    for num in range(len(Lista_valores)):
        nome_presente.append(chr(int(Lista_valores[num])))
    
    return nome_presente

def presentes_anya():
    lista_presentes_excluidos = []
    lista_presentes = []
    num_presentes = int(input())

    for num in range(num_presentes):
        presente_codificado = input().split(' ')
        total_valor = soma_valores(presente_codificado)

        presente_decodificado = decodificando_presentes(presente_codificado)
        presente_decodificado = ''.join(presente_decodificado)

        if presente_decodificado not in lista_presentes:
            lista_presentes.append(presente_decodificado)
            print(f'{presente_decodificado} ',end='')
            print(f'foi adicionado a lista ultrassecreta de presentes da Anya!!')
            

            if (total_valor % 2) != 0:
                lista_presentes_excluidos.append(presente_decodificado)
                
                
        else:
            print(f'{presente_decodificado} já está na lista de presentes da Anya!!')


    if len(lista_presentes_excluidos) > 0:
        print(f'Infelizmente o Twilight é mão de vaca e os seguintes itens precisaram ser excluídos da lista de presentes ultrassecretos da Anya: ',end='')
        listando_itens(lista_presentes_excluidos)

        for i in range(len(lista_presentes_excluidos)):
            if lista_presentes_excluidos[i] in lista_presentes:
                lista_presentes.remove(lista_presentes_excluidos[i])
        
        if len(lista_presentes) > 0:
            print(f'Lista final dos melhores presentes da Anya: ',end='')
            listando_itens(lista_presentes)
        
        else:
            print(f'O quê? Nenhum presente? Isso é um absurdo! Vamos corrigir essa injustiça e garantir que Anya tenha um Dia das Crianças inesquecível!')

            
    elif len(lista_presentes) > 0:
        print(f'Parece que o Dia das Crianças desse ano será especial!!!! Anya ganhará todos os presentes planejados, mesmo que ela não seja tão exemplar como deveria…')
        print(f'Lista final dos melhores presentes da Anya: ',end='')
        listando_itens(lista_presentes)

    
    else:
        print(f'O quê? Nenhum presente? Isso é um absurdo! Vamos corrigir essa injustiça e garantir que Anya tenha um Dia das Crianças inesquecível!')


presentes_anya()