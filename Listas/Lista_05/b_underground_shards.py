#Função que verifica se o numero recebido é igual ao numero desejado
#Se não for, separa em 2 numeros e testa eles
def separador_chips(n,n_desejado):
    #Caso base onde não é igual
    resposta = 'NAO'    
    
    #Caso o numero seja igual
    if n == n_desejado:
        resposta = 'SIM'
    
    #Caso o numero desejado seja maior do que o numero verificado
    elif n < n_desejado:
        resposta = 'NAO'
    
    #Caso não seja o num certo, verifica se é possivel dividir o num por 3
    elif n % 3 == 0:
        #Dividi em 2 numeros, onde um é metade do outro 
        n_separado_1 = n / 3
        n_separado_2 = n_separado_1 * 2

        #Executa a função para o num dividido
        resposta = separador_chips(n_separado_1,n_desejado)
        
        #Se ainda não tiver achado o num igual, verifica com o outro dividido
        if resposta == 'NAO':
            resposta = separador_chips(n_separado_2,n_desejado)   

    #Retorna resposta
    return resposta

#Função principal
def main():
    #Recebe o num de pedidos
    num_pedidos = int(input())

    #Loop que passa pela qtd de pedidos
    for i in range(num_pedidos):
        #Recebe a qtd desejada e a qtd inicial e as dividi em uma lista
        qtd_inicial_qtd_desejada = input().split(' ')
        
        #Executa a função deseparar e verificar, enviando o valor inicial e o desejadao
        resposta = separador_chips(int(qtd_inicial_qtd_desejada[0]),int(qtd_inicial_qtd_desejada[1]))
        print(resposta)

#Executa a principal
main()