#Funcao que cria a mochila 
def  criando_matriz(frase, matriz_mochila):
  if frase != 'finalizar' and frase != 'f':   #Verifica se a frase nao eh finalizar
    matriz_mochila.append(list(frase))  #Adciona a linha recebida como item da matriz mochila
    frase = input() #Recebe a prox linha
    criando_matriz(frase, matriz_mochila) #Chama a funcao novamente ate o finalizar 
  
  return 

def verificando_equipamentos_obrigatorios(mochila,obrigatorios):
  for i in mochila:
    if 'P' in i and 'primaria' in obrigatorios:
      obrigatorios.remove('primaria')
    if 'M' in i and 'munição' in obrigatorios:
      obrigatorios.remove('munição')
    if 'G' in i and 'granada' in obrigatorios:
      obrigatorios.remove('granada')
    if 'B' in i and 'branca' in obrigatorios:
      obrigatorios.remove('branca')
    if 'S' in i and 'secundaria' in obrigatorios:
      obrigatorios.remove('secundaria')
    if 'A' in i and 'acessorios' in obrigatorios:
      obrigatorios.remove('acessorios')

  return obrigatorios

#Funcao que recebe os itens para organizar, e tira o que nao sao obrigatorios
def recebendo_itens(equipamentos_obrigatorios, equipamento, equipamentos, mochila):
  if equipamento != 'finalizar programa' and equipamento != 'f':  #Verificacao para continuar adcionando
    equipamento = equipamento.split('-')  #Separando as partes do equipamento recebido em uma lista
    
    if equipamento[2] in equipamentos_obrigatorios: #Verifica se o eqp esta na lista dos obrigatorios
      tamanho_atual = equipamento[1].split('x')
      posicao_j, posicao_i = verificando_tamanho(tamanho_atual, mochila, 1, 0, 0, 0, False )

      if posicao_j == -1:
        print(f'Não há espaço para {equipamento[0]}')
      
      else:
        tipo_equipamento = list(equipamento[2])
        substituindo_itens(posicao_i, posicao_j, tamanho_atual, tipo_equipamento, mochila, 0, 0)
        equipamentos.append(equipamento)  #Adciona o equipamento na lista dos equipamentos certos
        equipamentos_obrigatorios.remove(equipamento[2])  #Remove o equipamento da lista dos obrigatorios
        print(f'Item adicionado: {equipamento[0]}')
        #Funcao organizar mochila
    else:
      print(f'Não precisamos de {equipamento[0]}')  #Nao sendo obrigatorio, printa esta mensagem

    equipamento = input() #Recebe o prox equipamento
    recebendo_itens(equipamentos_obrigatorios, equipamento, equipamentos, mochila) #Chama a funcao novamente ate sua finalizacao
    
  return
  


#Funcao que verifica se o item cabe na mochila
def verificando_tamanho(tamanho, mochila, contador_i, contador_j, i, j, achou_j):
  posicao_final_i = 0
  posicao_final_j = 0
  
  if mochila[i][j] == 'O':  #Verificando se o item verificado eh um espaco vazio
    
    if contador_j < int(tamanho[0]):  #Verifica se o num de colunas vazias contadas da linha esta menor que o necessario
      contador_j += 1 
      
      if contador_j == int(tamanho[0]):  #Verifica se o num de colunas vazias seguidas contadas, ja eh igual ao necessario
        if contador_i == int(tamanho[1]): #Verifica se o num de linhas vazias seguidas contadas, eh igual ao necessario 
          consegue = True
          posicao_final_j = j - (int(tamanho[0]) - 1)
          posicao_final_i = i - (int(tamanho[1]) - 1)

        else:
          achou_j = True
          i += 1
          j -= int(tamanho[0]) - 1
          if i < len(mochila):
            posicao_final_j, posicao_final_i = verificando_tamanho(tamanho, mochila, contador_i, contador_j, i, j, achou_j)            
          else:
            posicao_final_j = -1
            posicao_final_i = -1

      else: #Caso nao esteja igual 
        j += 1  #Aumenta o indice da coluna
        if j < len(mochila[0]): #Verifica se o indice nao passa do tamanho da mochila
          posicao_final_j, posicao_final_i = verificando_tamanho(tamanho, mochila, contador_i, contador_j, i, j, achou_j)  #Executa a funcao para contar com o prox indice j
        
        else: #Se passar, ira para a prox linha
          contador_i = 1
          contador_j = 0 
          j = 0
          i += 1

          if i < len(mochila):
            posicao_final_j, posicao_final_i = verificando_tamanho(tamanho, mochila, contador_i, contador_j, i, j, achou_j)

          else:
            posicao_final_i = -1
            posicao_final_j = -1

        if i >= len(mochila): #Caso passe da ultima linha, o item nao cabe
          consegue = False
          posicao_final_j = -1
          posicao_final_i = -1
    
    elif contador_i < int(tamanho[1]):  #Verifica se o num de linhas vazias contadas eh menor que o desejado
      contador_i += 1
      contador_j = 1
      j += 1

      posicao_final_j, posicao_final_i = verificando_tamanho(tamanho, mochila, contador_i, contador_j, i, j, achou_j)
      

    else:
      posicao_final_j = j - (tamanho[0] - 1)
      posicao_final_i = i - (tamanho[1] - 1)

  else: #Caso o espaco nao seja vazio
    #Reseta os contadores
    contador_i = 1
    contador_j = 0
    
    j += 1  #Passa para a prox coluna
    if j >= len(mochila[0]):  #Verifica se nao passa do num max de colunas
      #Reseta a coluna, e vai para a prox linha
      j = 0
      i += 1 
      
      if i >= len(mochila): #Se passar do num max de linhas, o item nao cabe
        
        consegue = False
        posicao_final_j = -1
        posicao_final_i = -1

      else:
        posicao_final_j, posicao_final_i = verificando_tamanho(tamanho, mochila, contador_i, contador_j, i, j, achou_j)

    else:
      if achou_j:
        achou_j = False
        i -= 1

      contador_i = 1
      contador_j = 0
      posicao_final_j, posicao_final_i = verificando_tamanho(tamanho, mochila, contador_i, contador_j, i, j, achou_j)
  
  return posicao_final_j, posicao_final_i
  #Retornar a posicao inical que o obj tem que estar para assim fazer a funcao que troca o espaco vazio pelo nome do objeto
  #Pode fazer subtraindo a posicao que descobriu que cabe com os tamanhos
  #Retornar valores absurdos caso nao funcione
  #Criar funcao que troque
  #Printar quando o item eh adcionado

def substituindo_itens(posicao_i, posicao_j, tamanho, tipo_equipamento, mochila, contador_i, contador_j):
  #tipo_equipamento = list(tipo_equipamento) FAZ ISSO QUANDO CHAMAR
  inicial_tipo = tipo_equipamento[0]

  if contador_j < int(tamanho[0]):
    mochila[posicao_i][posicao_j] = inicial_tipo
    contador_j += 1
    posicao_j += 1
    
    substituindo_itens(posicao_i, posicao_j, tamanho, tipo_equipamento, mochila, contador_i, contador_j)
  
  elif contador_i < (int(tamanho[1]) - 1):
    posicao_i += 1
    posicao_j -= contador_j
    contador_j = 0 
    contador_i += 1
    
    substituindo_itens(posicao_i, posicao_j, tamanho, tipo_equipamento, mochila, contador_i, contador_j)

  return mochila

def printado_mochila(mochila, i, j, acabou):
  if not acabou:

    if  j < len(mochila[0]) - 1:
      print(f'{mochila[i][j].upper()}',end='')
    
    else:
      print(f'{mochila[i][j].upper()}')
    
    if j < len(mochila[0]) - 1:
      j += 1
    
    elif i < len(mochila) - 1:
      i += 1
      j = 0

    else:
      acabou = True
    
    printado_mochila(mochila, i, j, acabou)

  return mochila


def main():
  frase_inicial = input() #Recebe a primeira linha da mochila
  mochila = []  #Declara mochila inial vazia
  criando_matriz(frase_inicial, mochila)  #Executa a funcao que adcionara os intens na mochila

  
  equipamentos_obrigatorios = input().split(', ') #Recebendo equipamentos obrigatorios e criando sua lista
  verificando_equipamentos_obrigatorios(mochila, equipamentos_obrigatorios)

  equipamento = input() #Recebendo primeiro equipamento a ser adcionado
  equipamentos = [] #Lista dos equipamentos certos a organizar
  
  recebendo_itens(equipamentos_obrigatorios, equipamento, equipamentos, mochila) #Chamando funcao que organiza os itens

  printado_mochila(mochila, 0, 0, False)
  
  if len(equipamentos_obrigatorios) > 0:
    print(f'Faltou: ',end='')
    for num in range(len(equipamentos_obrigatorios)):
      if num < len(equipamentos_obrigatorios) - 1:
        print(f'{equipamentos_obrigatorios[num]}',end=', ')

      else:
        print(f'{equipamentos_obrigatorios[num]}')

main() 