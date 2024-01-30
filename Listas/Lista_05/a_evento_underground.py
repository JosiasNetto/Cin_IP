#Função que multiplica os numeros impares
def multiplicador_impares(n):
    
    #Declarando variavel para resposta
    resposta = 0
    
    #Caso Base
    if n == 1:
        resposta = 1
    
    #Caso o numero seja Impar
    elif n % 2 == 1:
        resposta = n * multiplicador_impares(n-2)

    #Caso o numero seja impar
    else:
        resposta = multiplicador_impares(n-1)

    #Retorna o calculo final
    return resposta

#Função principal
def main():
    #Codigo recebido na entrada do evento
    seu_codigo = int(input())

    #Executando a função que gera a senha
    senha_acesso = multiplicador_impares(seu_codigo)

    #Imprimindo a senha
    print(senha_acesso)

#Executando a principal
main()