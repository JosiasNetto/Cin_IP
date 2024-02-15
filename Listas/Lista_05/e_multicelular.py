def  criando_matriz(frase, matriz_mochila): #Funcao que cria a mochila 
  if frase != 'finalizar' and frase != 'f': #Verifica se a frase nao eh finalizar
    matriz_mochila.append(list(frase))  #Adciona a lista da linha recebida como item da matriz mochila
    frase = input() #Recebe a prox linha
    criando_matriz(frase, matriz_mochila) #Chama a funcao novamente ate o finalizar 
  
  return 

def verificando_equipamentos_obrigatorios(mochila,obrigatorios):  #Funcao que verifica se inicialmente a mochila ja veio com algum item
  
  for i in mochila: #Loop que passa por cada linha da mochila
    
    #Verificando se alguma das iniciais dos itens esta na linha, se sim, a remove da lista de itens obrigatorios
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

  return obrigatorios #Retorna os itens obrigatorios atualizados

#Funcao que recebe os itens para organizar, tira os que nao sao obrigatorios;
#Chama a funcao que verifica se o item cabe na mochila
#Se cabe, chama a funcao que add o item na mochila
def recebendo_itens(equipamentos_obrigatorios, equipamento, equipamentos, mochila):
  if equipamento != 'finalizar programa' and equipamento != 'f':  #Verificacao para continuar adcionando
    equipamento = equipamento.split('-')  #Separando as partes do equipamento recebido em uma lista
    
    if equipamento[2] in equipamentos_obrigatorios: #Verifica se o eqp esta na lista dos obrigatorios
      tamanho_atual = equipamento[1].split('x') #Separando o tamanho do item
      posicao_j, posicao_i = verificando_tamanho(tamanho_atual, mochila, 1, 0, 0, 0, False )  #Funcao que retorna a posicao que o item ocupa na mochila

      if posicao_j == -1: #Verificando se o item nao cabe na mochila e imprimindo sua respectiva msg
        print(f'Não há espaço para {equipamento[0]}') 
      
      else:
        tipo_equipamento = list(equipamento[2])
        substituindo_itens(posicao_i, posicao_j, tamanho_atual, tipo_equipamento, mochila, 0, 0)  #Executando a funcao que add os itens na mochila
        equipamentos.append(equipamento)  #Adciona o equipamento na lista dos equipamentos certos
        equipamentos_obrigatorios.remove(equipamento[2])  #Remove o equipamento da lista dos obrigatorios
        print(f'Item adicionado: {equipamento[0]}') #Imprimindo a msg que o item foi adcionado
      
    else:
      print(f'Não precisamos de {equipamento[0]}')  #Nao sendo obrigatorio, printa esta mensagem

    equipamento = input() #Recebe o prox equipamento
    recebendo_itens(equipamentos_obrigatorios, equipamento, equipamentos, mochila) #Chama a funcao novamente ate sua finalizacao
    
  return
  

def verificando_tamanho(tamanho, mochila, contador_i, contador_j, i, j, achou_j): #Funcao que verifica se o item cabe na mochila
  #Declarando variaveis da posicao do item na mochila
  posicao_final_i = 0
  posicao_final_j = 0
  
  if mochila[i][j] == 'O':  #Verificando se o item verificado eh um espaco vazio
    
    if contador_j < int(tamanho[0]):  #Verifica se o num de colunas vazias contadas da linha esta menor que o necessario
      contador_j += 1 
      
      if contador_j == int(tamanho[0]):  #Verifica se o num de colunas vazias seguidas contadas, ja eh igual ao necessario
        if contador_i == int(tamanho[1]): #Verifica se o num de linhas vazias seguidas contadas, eh igual ao necessario 
          #Se sim, retorna a posicao onde o item ficara na bolsa
          posicao_final_j = j - (int(tamanho[0]) - 1)
          posicao_final_i = i - (int(tamanho[1]) - 1)

        else:
          achou_j = True  #Variavel aux para declara que o num de colunas daquela linha cabe
          i += 1  #Vai para a prox linha
          j -= int(tamanho[0]) - 1  #Retorna para a coluna onde tem que ser verificado o espaco vazio
          if i < len(mochila):  #Verifica se a linha nao passa do tamanho da mochila
            posicao_final_j, posicao_final_i = verificando_tamanho(tamanho, mochila, contador_i, contador_j, i, j, achou_j) #Executa funcao novamente na prox posicao            
          
          else: #Se passar do num max de linhas, retorna -1 que declara que nao tem espaco na mochila para o item
            posicao_final_j = -1
            posicao_final_i = -1

      else: #Caso o num de colunas vazias ainda nao seja igual ao necessario 
        j += 1  #Aumenta o indice da coluna
        if j < len(mochila[0]): #Verifica se o indice nao passa do tamanho da mochila
          posicao_final_j, posicao_final_i = verificando_tamanho(tamanho, mochila, contador_i, contador_j, i, j, achou_j)  #Executa a funcao para contar com o prox indice j
        
        else: #Se passar do tamanho de colunas da mochila, vai para a prox linha
          contador_i = 1
          contador_j = 0 
          j = 0
          i += 1

          if i < len(mochila):  #Verifica se a linha nao passa do tamanho total da mochila, e executa a funcao novamente
            posicao_final_j, posicao_final_i = verificando_tamanho(tamanho, mochila, contador_i, contador_j, i, j, achou_j)

          else: #Declara que o item nao cabe na mochila
            posicao_final_i = -1
            posicao_final_j = -1

        if i >= len(mochila): #Caso passe da ultima linha, o item nao cabe
          posicao_final_j = -1
          posicao_final_i = -1
    
    elif contador_i < int(tamanho[1]):  #Verifica se o num de linhas vazias contadas eh menor que o desejado
      contador_i += 1 #Aumenta um no contador de linhas
      contador_j = 1  #Reseta o contador de colunas, ja que verificara outra linha
      j += 1  #Passa para a prox coluna

      posicao_final_j, posicao_final_i = verificando_tamanho(tamanho, mochila, contador_i, contador_j, i, j, achou_j) #Chama a funcao para a prox coluna
      

    else: #Caso esteja chegue no tamanho necessario, retorna a posicao a se add na mochila
      posicao_final_j = j - (tamanho[0] - 1)
      posicao_final_i = i - (tamanho[1] - 1)

  else: #Caso o espaco nao seja vazio, reseta os contadores e passa para a prox coluna
    contador_i = 1
    contador_j = 0
    j += 1 
    
    if j >= len(mochila[0]):  #Verifica se esta maior que o tamanho max de colunas
      j = 0 #Volta pra coluna 0
      i += 1  #Vai para a prox linha
      
      if i >= len(mochila): #Se passar do num max de linhas, o item nao cabe
        posicao_final_j = -1
        posicao_final_i = -1

      else: #Se nao passar, chama a funcao para o item da prox linha
        posicao_final_j, posicao_final_i = verificando_tamanho(tamanho, mochila, contador_i, contador_j, i, j, achou_j)

    else: #Caso j nao passe do tamanho da mochila
      if achou_j: #Verifica se j ja foi achado naquele momento, se sim, muda para falso, e volta uma linha
        achou_j = False
        i -= 1

      #Resetando os contadores e chamando a funcao para o prox item
      contador_i = 1
      contador_j = 0
      posicao_final_j, posicao_final_i = verificando_tamanho(tamanho, mochila, contador_i, contador_j, i, j, achou_j)
  
  return posicao_final_j, posicao_final_i #Retorna a posicao que o item deve comecar a ser inserido na mochila 

def substituindo_itens(posicao_i, posicao_j, tamanho, tipo_equipamento, mochila, contador_i, contador_j): #Funcao que add os itens na mochila
  inicial_tipo = tipo_equipamento[0]  #Declarando a inicial que aparecera na mochila

  if contador_j < int(tamanho[0]):  #Verifica se o contador de colunas esta menor que o tamanho do item
    mochila[posicao_i][posicao_j] = inicial_tipo  #Declara o espaco daquela posicao como o item
    contador_j += 1 #Aumenta um no contador de colunas
    posicao_j += 1  #vai para a prox coluna
    
    substituindo_itens(posicao_i, posicao_j, tamanho, tipo_equipamento, mochila, contador_i, contador_j)  #Chama a funcao para a prox posicao
  
  elif contador_i < (int(tamanho[1]) - 1):  #Verifica se o contador de linhas esta menor que o tamanho do item
    posicao_i += 1  #Passa para a prox linha
    posicao_j -= contador_j #Volta para a coluna inicial correta daquela linha
    contador_j = 0  #Reseta o contador de colunas
    contador_i += 1 #Soma no contador de linhas
    
    substituindo_itens(posicao_i, posicao_j, tamanho, tipo_equipamento, mochila, contador_i, contador_j)  #Chama a funcao novamente para a prox posicao

  return mochila  #Retorna a mochila

def printado_mochila(mochila, i, j, acabou):  #Funcao que imprimi a mochila
  if not acabou:  #Verifica se nao acabou

    if  j < len(mochila[0]) - 1:  #Verifica se nao esta na ultima coluna para printar sem quebra de linha
      print(f'{mochila[i][j].upper()}',end='')
    
    else: #Caso seja o ultimo. printa com quebra de linha
      print(f'{mochila[i][j].upper()}')
    
    if j < len(mochila[0]) - 1: #Caso nao passe do tamanho da mochila, vai para a prox coluna
      j += 1
    
    elif i < len(mochila) - 1:  #Caso passe, verifica se esta na linha max da mochila, se nao, vai para a proxima linha e reseta a coluna
      i += 1
      j = 0

    else: #Quando chega na ultima, muda a variavel para que acabou
      acabou = True
    
    printado_mochila(mochila, i, j, acabou) #Chama a funcao ate que acabe

  return mochila


def main():
  frase_inicial = input() #Recebe a primeira linha da mochila
  mochila = []  #Declara mochila inial vazia
  criando_matriz(frase_inicial, mochila)  #Executa a funcao que adcionara os intens na mochila

  
  equipamentos_obrigatorios = input().split(', ') #Recebendo equipamentos obrigatorios e criando sua lista
  verificando_equipamentos_obrigatorios(mochila, equipamentos_obrigatorios) #Verificando se ja tem algum obrigatorio na mochila

  equipamento = input() #Recebendo primeiro equipamento a ser adcionado
  equipamentos = [] #Lista dos equipamentos certos a organizar
  
  recebendo_itens(equipamentos_obrigatorios, equipamento, equipamentos, mochila) #Chamando funcao que organiza os itens na mochila

  printado_mochila(mochila, 0, 0, False)  #Funcao que printa a mochila
  
  #Imprimindo os itens que faltaram
  if len(equipamentos_obrigatorios) > 0:
    print(f'Faltou: ',end='')
    for num in range(len(equipamentos_obrigatorios)):
      if num < len(equipamentos_obrigatorios) - 1:
        print(f'{equipamentos_obrigatorios[num]}',end=', ')

      else:
        print(f'{equipamentos_obrigatorios[num]}')

main() 