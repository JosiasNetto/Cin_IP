def num_pedidos(pedido, comidas):
    if 'qtd_pedidos' in comidas[pedido]:
        comidas[pedido].update({'qtd_pedidos' : comidas[pedido]['qtd_pedidos'] + 1})
                
    else:
        comidas[pedido].update({'qtd_pedidos' : 1})

    return

def calc_pedidos_inexistentes(pedido, comidas_inexistentes_pedido):
    if pedido in comidas_inexistentes_pedido:
        comidas_inexistentes_pedido[pedido] += 1

    else:
        comidas_inexistentes_pedido[pedido] = 1
    
    return 

def main():

    comidas = {'bobo de camarao' : {'ingedientes' : ('camarao', 'macaxeira', 'leite de coco', 'dende', 'tomate', 'cebola'), 'preco' : 58}, 
    'tapioca de carne de sol' : {'ingredientes' :('massa de tapioca', 'carne de sol', 'queijo coalho', 'tomate', 'cebola'), 'preco' : 60},
    'carne de sol com macaxeira' : {'ingredientes' : ('carne de sol', 'macaxeira', 'manteiga'), 'preco' : 38.50}, 
    'camarao na moranga' : {'ingredientes' : ('moranga', 'camarao', 'cebola', 'alho', 'tomate', 'pimentao', 'creme de leite', 'azeite', 'coentro'), 'preco' : 68.50}}

    qtd_preço_ingredientes = {'camarao' : {'qtd' : 5, 'preco' : 30}, 'macaxeira' : {'qtd' : 5, 'preco' : 3}, 'leite de coco' : {'qtd' : 5, 'preco' : 5}, 
    'dende' : {'qtd' : 5, 'preco' : 15}, 'tomate' : {'qtd' : 5, 'preco' : 3}, 'cebola' : {'qtd' : 5, 'preco' : 2}, 'massa de tapioca' : {'qtd' : 5, 'preco' : 10}, 
    'carne de sol' : {'qtd' : 5, 'preco' : 30},  'queijo coalho' : {'qtd' : 5, 'preco' : 15}, 'manteiga' : {'qtd' : 5, 'preco' : 5.50}, 
    'moranga' : {'qtd' : 5, 'preco' : 10}, 'alho' : {'qtd' : 5, 'preco' : 1.5}, 'pimentao' : {'qtd' : 5, 'preco' : 2}, 'creme de leite' : {'qtd' : 5, 'preco' : 4}, 
    'azeite' : {'qtd' : 5, 'preco' : 15}, 'coentro' : {'qtd' : 5, 'preco' : 1}}
    
    comidas_inexistentes_pedido = {}

    
    acabou = False
    while not acabou:
        try:
            pedido = input()
            if pedido in comidas:
                num_pedidos(pedido, comidas)
            
            else:
                calc_pedidos_inexistentes(pedido, comidas_inexistentes_pedido)
                if comidas_inexistentes_pedido[pedido] > 2:
                    #Programar funcao que recebe os ingredientes
                    #Add na lista de comdias     

        
        except EOFError:
            acabou = True