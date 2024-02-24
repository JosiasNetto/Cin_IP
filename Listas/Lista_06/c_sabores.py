def num_pedidos(pedido, comidas, qtd_preco_ingredientes, custo):
#Funcao que faz a soma de quantas vezes aquele pedido foi pedido
#Subtrai os ingredientes utilizados da qtd disponivel
#Compra os novos ingredientes e retorna o custo

    if 'qtd_pedidos' in comidas[pedido]:  #Verifica se o pedido ja foi solicitado anterior mente
        comidas[pedido].update({'qtd_pedidos' : comidas[pedido]['qtd_pedidos'] + 1})  #Adciona 1 a qtd do pedido
                
    else:
        comidas[pedido].update({'qtd_pedidos' : 1}) #Declara a primeira vez que o pedido foi solicitado

    for i in comidas[pedido]['ingredientes']: #Loop que passa pelos ingredientes do pedido
      if qtd_preco_ingredientes[i]['qtd'] == 0: #Verifica se o estoque do ingrediente esta em 0
        qtd_preco_ingredientes[i].update({'qtd' : 3}) #Adciona mais 3 ao estoque
        custo += (qtd_preco_ingredientes[i]['preco'] * 4) #Faz o calculo do custo da compra do ingrediente
      
      else:
        qtd_preco_ingredientes[i].update({'qtd' : qtd_preco_ingredientes[i]['qtd'] - 1})  #Subtrai 1 da qtd do ingrediente disponivel
        
    return custo  #Retorna o custo da compra de ingredientes

def calc_pedidos_inexistentes(pedido, comidas_inexistentes_pedido): #Funcao que calcula quantas vezes um pedido que nao existe, foi solicitado
    if pedido in comidas_inexistentes_pedido: #Se ja tiver sido peido antes, soma 1 ao atual
        comidas_inexistentes_pedido[pedido] += 1

    else: #Se nao tiver, declara que foi pedido uma vez
        comidas_inexistentes_pedido[pedido] = 1
    
    return 

def gerando_comida_nova(pedido, comidas, qtd_preco_ingredientes): #Funcao que add uma comida ao cardapio
  #Variaveis Aux
  dic_aux = {}
  preco_total = 0

  for i in range(9):  #Loop que recebe os 9 ingredientes da comida nova
      ingrediente = input() #Rebendo o ingrediente
      dic_aux[f'{i}'] = ingrediente #Adcionando no dic de aux
      preco_total += qtd_preco_ingredientes[ingrediente]['preco'] #Pegando o valor do ingrediente e add no preco total
  
  preco_total += 5  #Somando 5 ao preco total

  dic_pedido = {'ingredientes' : tuple(dic_aux.values()), 'preco' : preco_total}  #Criando dic com as infos do pedido

  comidas.update({pedido : dic_pedido}) #Adcionando ao dic das comidas disponiveis, onde o pedido eh a chave, e o dic com as infos o valor

  return

def calc_lucro(pedido, comidas):  #Funcao que calcula Lucro do pedido
   lucro = comidas[pedido]['preco'] #Lucro igual a o preco do produto

   return lucro #Retorna Lucro

def calc_mais_pedido(pedido, comidas, mais_pedido, num_mais_pedido):  #Funcao que retorna o pedido que foi mais solicitado ate o momento
  for i in comidas: #Loop que passa pelo dic das comidas disponiveis
     if comidas[i].get('qtd_pedidos', 0) > num_mais_pedido: #Verifica se a qtd do pedido i, eh maior que o do maior atual
        num_mais_pedido = comidas[i].get('qtd_pedidos', 0)  #Recebe a qtd de vezes que o pedido i foi solicitado
        mais_pedido = pedido  #Recebe o nome do pedido mais solicitado

  return mais_pedido, num_mais_pedido #Retorna o nome e a qtd do pedido mais solicitado
  


def main():

  #Declarando Variaveis de uso/aux no codigo
  comidas = {'bobo de camarao' : {'ingredientes' : ('camarao', 'macaxeira', 'leite de coco', 'dende', 'tomate', 'cebola'), 'preco' : 58}, 
    'tapioca de carne de sol' : {'ingredientes' :('massa de tapioca', 'carne de sol', 'queijo coalho', 'tomate', 'cebola'), 'preco' : 60},
    'carne de sol com macaxeira' : {'ingredientes' : ('carne de sol', 'macaxeira', 'manteiga'), 'preco' : 38.50}, 
    'camarao na moranga' : {'ingredientes' : ('moranga', 'camarao', 'cebola', 'alho', 'tomate', 'pimentao', 'creme de leite', 'azeite', 'coentro'), 'preco' : 68.50}}

  qtd_preco_ingredientes = {'camarao' : {'qtd' : 5, 'preco' : 30}, 'macaxeira' : {'qtd' : 5, 'preco' : 3}, 'leite de coco' : {'qtd' : 5, 'preco' : 5}, 
    'dende' : {'qtd' : 5, 'preco' : 15}, 'tomate' : {'qtd' : 5, 'preco' : 3}, 'cebola' : {'qtd' : 5, 'preco' : 2}, 'massa de tapioca' : {'qtd' : 5, 'preco' : 10}, 
    'carne de sol' : {'qtd' : 5, 'preco' : 30},  'queijo coalho' : {'qtd' : 5, 'preco' : 15}, 'manteiga' : {'qtd' : 5, 'preco' : 5.50}, 
    'moranga' : {'qtd' : 5, 'preco' : 10}, 'alho' : {'qtd' : 5, 'preco' : 1.5}, 'pimentao' : {'qtd' : 5, 'preco' : 2}, 'creme de leite' : {'qtd' : 5, 'preco' : 4}, 
    'azeite' : {'qtd' : 5, 'preco' : 15}, 'coentro' : {'qtd' : 5, 'preco' : 1}}
    
  comidas_inexistentes_pedido = {}
  lucro = 0
  custo = 0
  mais_pedido = ''
  num_mais_pedido = 0

    
  acabou = False
  while not acabou: #Loop que so acabara quando acontecer o EOF error
      try:  #Executando codigo ate que apareca o EOF
        pedido = input()  #Recebendo o pedido
        if pedido in comidas: #Verificando se o pedido esta na lista das comidas 
          custo = num_pedidos(pedido, comidas, qtd_preco_ingredientes, custo) #Executando funao que altera o banco de dados
          print(f'{pedido} saindo...')  #Printa que o pedido esta saindo
          lucro += calc_lucro(pedido, comidas)  #Executando funcao que calcula o lucro gerado pelo pedido
          mais_pedido, num_mais_pedido = calc_mais_pedido(pedido, comidas, mais_pedido, num_mais_pedido)  #Executando funcao que retorna o pedido mais solicitado
            
        else: #Caso o pedido nao esteja na lista das comidas disponiveis
          calc_pedidos_inexistentes(pedido, comidas_inexistentes_pedido)  #Executa funcao que verifica quantas vezes esse pedido foi solicitado
          if comidas_inexistentes_pedido[pedido] > 2: #Verificando se foi pedido mais de 2 vezes
            gerando_comida_nova(pedido, comidas, qtd_preco_ingredientes)  #Executando funcao que adciona o pedido ao cardapio
            print(f'Atendendo demandas, {pedido} é a mais nova adição ao cardápio do Sabores de Recife.')
                
          else: #Caso o pedido ainda nao estaja disponivel
            print(f'{pedido} ainda não é uma opção disponível.')

        
      except EOFError:  #Caso aconteca o EOF error, acaba o loop
        acabou = True

  lucro -= custo  #Subtrai os custo do lucro

  print('##### Fim do expediente #####')
  print(f'O lucro obtido no dia de hoje foi de R${lucro:.2f}.') #Imprimindo o lucro do dia

  if mais_pedido == 'bobo de camarao':  #Caso o mais pedido seja o bobo de camarao, printa a respectiva msg
     print(f'O bom e tradicional Bobó de Camarão, líder em vendas, nunca será superado!')

  else: #Caso seja outra comida, printa a mais pedida
     print(f'{mais_pedido.capitalize()} está fazendo sucesso entre os clientes, ultrapassando até mesmo o lendário Bobó de Camarão.')


main()