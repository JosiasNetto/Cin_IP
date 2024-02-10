#Funcao que cria a mochila 
def  criando_matriz(frase, matriz_mochila):
  if frase != 'finalizar' and frase != 'f':   #Verifica se a frase nao eh finalizar
    matriz_mochila.append(list(frase))  #Adciona a linha recebida como item da matriz mochila
    frase = input() #Recebe a prox linha
    criando_matriz(frase, matriz_mochila) #Chama a funcao novamente ate o finalizar 
  
  return 

#Funcao que recebe os itens para organizar, e tira o que nao sao obrigatorios
def recebendo_itens(equipamentos_obrigatorios, equipamento, equipamentos):
  if equipamento != 'finalizar programa' and equipamento != 'f':  #Verificacao para continuar adcionando
    equipamento = equipamento.split('-')  #Separando as partes do equipamento recebido em uma lista
    
    if equipamento[2] in equipamentos_obrigatorios: #Verifica se o eqp esta na lista dos obrigatorios
      equipamentos.append(equipamento)  #Adciona o equipamento na lista dos equipamentos certos
      equipamentos_obrigatorios.remove(equipamento[2])  #Remove o equipamento da lista dos obrigatorios
      #Funcao organizar mochila
    else:
      print(f'Não precisamos de {equipamento[0]}')  #Nao sendo obrigatorio, printa esta mensagem

    equipamento = input() #Recebe o prox equipamento
    recebendo_itens(equipamentos_obrigatorios, equipamento, equipamentos) #Chama a funcao novamente ate sua finalizacao
    
  return

#Funcao que verifica se o item cabe na mochila
def verificando_tamanho(tamanho, mochila, contador_i, contador_j, i, j):
  consegue = False
  
  if mochila[i][j] == '0':  #Verificando se o item verificado eh um espaco vazio
    
    if contador_j < int(tamanho[0]):  #Verifica se o num de colunas vazias contadas da linha esta menor que o necessario
      contador_j += 1 
      
      if contador_j == int(tamanho[0]):  #Verifica se o num de colunas vazias seguidas contadas, ja eh igual ao necessario
        if contador_i == int(tamanho[1]): #Verifica se o num de linhas vazias seguidas contadas, eh igual ao necessario 
          consegue = True
        
        elif contador_i < int(tamanho[1]):  #Verifica se o num de linhas vazias contadas eh menor que o desejado
          contador_i += 1
          
          if contador_i == int(tamanho[1]): #Verifica se o num de linhas vazias contadas, eh igual ao necessario apos o aumento
            consegue = True
          
          else: #Se ainda nao estiver igual ao desejado
            i += 1  #Aumenta o indice da linha
            if i < len(mochila):  #Verifica se o indice nao passa do tamanho da mochila
              consegue = verificando_tamanho(tamanho, mochila, contador_i, contador_j, i, j)  #Executa a funcao para contar com o prox indice i
            
            else: #Se passar, o item nao cabe
             consegue = False
      
      else: #Caso nao esteja igual 
        j += 1  #Aumenta o indice da coluna
        if j < len(mochila[0]): #Verifica se o indice nao passa do tamanho da mochila
          consegue = verificando_tamanho(tamanho, mochila, contador_i, contador_j, i, j)  #Executa a funcao para contar com o prox indice j
        
        else: #Se passar, ira para a prox linha 
          j = 0
          i += 1
          if i >= len(mochila): #Caso passe da ultima linha, o item nao cabe
            consegue = False
  
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
      
  return consegue
  #Retornar a posicao inical que o obj tem que estar para assim fazer a funcao que troca o espaco vazio pelo nome do objeto
  #Pode fazer subtraindo a posicao que descobriu que cabe com os tamanhos
  #Retornar valores absurdos caso nao funcione
  #Criar funcao que troque
  #Printar quando o item eh adcionado

def main():
  frase_inicial = input() #Recebe a primeira linha da mochila
  mochila = []  #Declara mochila inial vazia
  criando_matriz(frase_inicial, mochila)  #Executa a funcao que adcionara os intens na mochila
  print(mochila)
  
  equipamentos_obrigatorios = input().split(', ') #Recebendo equipamentos obrigatorios e criando sua lista
  equipamento = input() #Recebendo primeiro equipamento a ser adcionado
  equipamentos = [] #Lista dos equipamentos certos a organizar
  
  recebendo_itens(equipamentos_obrigatorios, equipamento, equipamentos) #Chamando funcao que organiza os itens
  print(equipamentos)
  
  tamanho = equipamentos[0][1].split('x') #Separa o tamanho de linhas e colunas em uma lista
  if verificando_tamanho(tamanho, mochila, 1, 0, 0, 0):
    print('Boa')
  else:
    print('ish')

main()