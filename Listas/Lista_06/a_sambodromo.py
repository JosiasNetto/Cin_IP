def recebendo_escolas(nome_e_nota, escolas_obrigatorias, dic_escolas):  #Funcao que add o nome e a nota da escola ao dicionario, caso ela esteja na lista das escolas
  nome_e_nota = nome_e_nota.split(': ') #Separa o nome da nota
  if nome_e_nota[0] in escolas_obrigatorias:  #Verifica se o nome esta na lista das obrigatorias
    if nome_e_nota[0] in dic_escolas: #Verifica se a escola ja foi adcionada anteriormente
      print(f'{nome_e_nota[0]} teve sua nota atualizada!')  #Imprimi a msg de atualizacao
    
    else: #Caso ainda nao tenha sido add
      print(f'{nome_e_nota[0]} teve sua nota apurada!') #Imprimi a msg que foi add

    dic_escolas.update({nome_e_nota[0] : nome_e_nota[1]}) #Adciona o nome e a nota ao dicionario
  
  else: #Caso nao esteja na lista das obrigatorias
    print(f'Epa, o que essa escola está fazendo aqui?!')  #Imprimi a msg correspondente

def organizando_notas(dic_escolas): #Funcao que organiza as escolas por sua nota de forma decrescente
  dic_escolas_organizadas = sorted(dic_escolas.items(), key = lambda item : item[1], reverse= True) #Funcao que organiza, chamando pelos valores do dicionario

  return dic_escolas_organizadas  #Retorna a lista das escolas organizadas

def printando_resultado(dic_escolas): #Funcao que imprimi todas as msgs de resultado
  print() 
  print(f'CLASSIFICAÇÃO DO CARNAVAL 2024:') #Mensagem inicial
  for i in range(len(dic_escolas)): #Loop que printa ate a ultima escola
    print(f'{i + 1}. {dic_escolas[i][0]}: {dic_escolas[i][1]}')
  
  print()
  print(f'É CAMPEÃ! A ESCOLA {dic_escolas[0][0]} É A GRANDE VENCEDORA DO CARNAVAL DE 2024, FAZENDO {dic_escolas[0][1]} PONTOS!!') #Mensagem da escola vencedora
  print(f'Infelizmente, a escola {dic_escolas[-1][0]} não alcançou as expectativas, fazendo apenas {dic_escolas[-1][1]} pontos, e foi rebaixada.')  #Mensagem da escola perdedora



def main():
  #Declarando Variaveis aux 
  escolas_obrigatorias = ("Porto da Pedra", "Beija-flor", "Salgueiro", "Grande Rio", "Unidos da Tijuca", "Imperatriz", "Mocidade", "Portela", "Vila Isabel", "Mangueira", "Paraíso do Tuiuti", "Viradouro")
  dic_escolas = {}

  escola_e_nota = input() #Recebendo o nome e a nota da primeira escola
  while 'Fim' not in escola_e_nota: #Loop ate que o nome da escola seja igual a fim
    recebendo_escolas(escola_e_nota, escolas_obrigatorias, dic_escolas) #Executando Funcao que add o nome e a nota ao dicionario
    escola_e_nota = input() #Recebendo a prox escola
  
  classificacao_escolas = organizando_notas(dic_escolas)  #Executando Funao que organiza a classificacao das escolas por suas notas
  printando_resultado(classificacao_escolas)  #Pritando o resultado Final


main()
  
