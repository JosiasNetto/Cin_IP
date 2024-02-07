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

def decodificando_decimais(lista_decimais_completa,lista_decodificada):

    if len(lista_decimais_completa) > 0:
        lista_decodificada.append(chr(lista_decimais_completa[0]))
        lista_decimais_completa.pop(0)
        decodificando_decimais(lista_decimais_completa,lista_decodificada)
    
    else:
        lista_decodificada = []
    
    return lista_decodificada


def main():
    sequencia_binario = input().split(' ')
    lista_aux = []
    lista_decimais = loop_binarios(sequencia_binario,lista_aux)

    lista_aux = []
    lista_decodificados = decodificando_decimais(lista_decimais,lista_aux)

    print(f'Os códigos da Matrix indicam que {"".join(lista_decodificados)} está perto.')

main()