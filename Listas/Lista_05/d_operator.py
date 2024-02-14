def loop_binarios(num_binarios,lista_decimais): #Funcao que gera um loop com base na qtd de binarios
    tamanho_lista = len(num_binarios)   #Variavel aux que recebe quantas sequencias de binarios tem
    
    if tamanho_lista > 0:   #Verifica se existem binarios
        lista_decimais.append(decodificando_binario(num_binarios[0],0)) #Envia a primeira sequencia de binarios da lista, e retorna seu respectivo decimal
        num_binarios.pop(0) #Exclui o primeiro binario verificado
        lista_decimais = loop_binarios(num_binarios,lista_decimais) #Adciona cada decimal recurssivamente ate que a lista dos binarios se torne vazia

    return lista_decimais   #Retorna a lista dos decimais

def decodificando_binario(binario,decimal): #Funcao que decodifica de binario para decimal
    binario = list(binario) #Separa cada caracter do binario em uma lista
    posicao_max = len(binario) - 1  #Variavel aux para limitar recurssao e calcular binario 
    
    if posicao_max >= 0:    #Verifica se pocicao max nao eh menor que 0
        decimal += int(binario[0]) * (2**posicao_max)   #Calculo da soma do binario para decimal
        binario.pop(0)  #Excluindo o binario calculado
        decimal = decodificando_binario(binario,decimal)    #Realizando o calculo com o prox binario

    return decimal  #Retorna o decimal 

def decodificando_decimais(lista_decimais_completa,lista_decodificada): #Funcao que decodifica o decimal para sua letra na tabela ASCII 

    if len(lista_decimais_completa) > 0:    #Verifica se a lista dos decimais nao eh vazia
        lista_decodificada.append(chr(lista_decimais_completa[0]))  #Adciona o num decodificado numa lista
        lista_decimais_completa.pop(0)  #Exclui o num decodificado da lista utilizada
        decodificando_decimais(lista_decimais_completa,lista_decodificada)  #Chama a funcao para decodificar o prox
    
    else:   #Caso base
        lista_decodificada = []
    
    return lista_decodificada   #Retorna a lista com a palavra


def main():
    sequencia_binario = input().split(' ')  #Recebendo as sequencia dos binarios, e transformando em lista
    lista_aux = []  #Lista vazia de aux  
    lista_decimais = loop_binarios(sequencia_binario,lista_aux) #Executando os binarios, e transformando-os em decimais 

    lista_aux = []  
    lista_decodificados = decodificando_decimais(lista_decimais,lista_aux)  #Recebendo a lista da palavra atraves da funcao

    print(f'Os códigos da Matrix indicam que {"".join(lista_decodificados)} está perto.') #Imprimi a msg com a palavra

main()