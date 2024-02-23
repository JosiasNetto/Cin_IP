def num_pedidos(pedido, comidas, qtd_preco_ingredientes):
    if 'qtd_pedidos' in comidas[pedido]:
        comidas[pedido].update({'qtd_pedidos' : comidas[pedido]['qtd_pedidos'] + 1})
                
    else:
        comidas[pedido].update({'qtd_pedidos' : 1})

    #for i in comidas[pedido]['ingredientes']:
       #qtd_preco_ingredientes.update({pedido : {})
        #Updatar qtd ingrediente do dic de ingredientes
    return

def calc_pedidos_inexistentes(pedido, comidas_inexistentes_pedido):
    if pedido in comidas_inexistentes_pedido:
        comidas_inexistentes_pedido[pedido] += 1

    else:
        comidas_inexistentes_pedido[pedido] = 1
    
    return 

def gerando_comida_nova(pedido, comidas, qtd_preco_ingredientes):
  dic_aux = {}
  preco_total = 0

  for i in range(9):
      ingrediente = input()
      dic_aux[f'{i}'] = ingrediente
      preco_total += qtd_preco_ingredientes[ingrediente]['preco']
  
  preco_total += 5

  dic_pedido = {'ingredientes' : tuple(dic_aux.values()), 'preco' : preco_total}

  comidas.update({pedido : dic_pedido})

  return

def calc_lucro(pedido, comidas):
   custo = comidas[pedido]['preco']

   return custo

def calc_mais_pedido(pedido, comidas, mais_pedido, num_mais_pedido):
  for i in comidas:
     if comidas[i].get('qtd_pedidos', 0) > num_mais_pedido:
        num_mais_pedido = comidas[i].get('qtd_pedidos', 0)
        mais_pedido = pedido

  return mais_pedido, num_mais_pedido
  


def main():

  comidas = {'bobo de camarao' : {'ingedientes' : ('camarao', 'macaxeira', 'leite de coco', 'dende', 'tomate', 'cebola'), 'preco' : 58}, 
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
  mais_pedido = ''
  num_mais_pedido = 0

    
  acabou = False
  while not acabou:
      try:
        pedido = input()
        if pedido in comidas:
          num_pedidos(pedido, comidas)
          print(f'{pedido} saindo...')
          lucro += calc_lucro(pedido, comidas)
          mais_pedido, num_mais_pedido = calc_mais_pedido(pedido, comidas, mais_pedido, num_mais_pedido)
            
        else:
          calc_pedidos_inexistentes(pedido, comidas_inexistentes_pedido)
          if comidas_inexistentes_pedido[pedido] > 2:
            gerando_comida_nova(pedido, comidas, qtd_preco_ingredientes)
            print(f'Atendendo demandas, {pedido} é a mais nova adição ao cardápio do Sabores de Recife.')
                
          else:
            print(f'{pedido} ainda não é uma opção disponível.')

        
      except EOFError:
        acabou = True

  print('##### Fim do expediente #####')
  print(f'O lucro obtido no dia de hoje foi de R${lucro:.2f}.')

  if mais_pedido == 'bobo de camarao':
     print(f'O bom e tradicional Bobó de Camarão, líder em vendas, nunca será superado!')

  else:
     print(f'{mais_pedido.capitalize()} está fazendo sucesso entre os clientes, ultrapassando até mesmo o lendário Bobó de Camarão.')


main()