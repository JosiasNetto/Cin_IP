#Recebendo os num binarios
#num_binarios = input().split(' ')

def decodificando_binario(binario,decimal):
    binario = list(binario)
    posicao_max = len(binario) - 1
    
    if posicao_max >= 0:
        decimal += int(binario[0]) * (2**posicao_max)
        binario.pop(0)
        decimal = decodificando_binario(binario,decimal)

    return decimal

def loop_binarios(num_binarios,lista_decimais):
    tamanho_lista = len(num_binarios)
    
    if tamanho_lista > 0:
        lista_decimais.append(decodificando_binario(num_binarios[0],0))
        num_binarios.pop(0)
        lista_decimais = loop_binarios(num_binarios,lista_decimais)

    return lista_decimais

def decodificando_decimais(lista_decimais_completa):
