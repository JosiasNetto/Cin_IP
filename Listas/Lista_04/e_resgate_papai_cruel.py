
#Funcao relativa ao desafio para coordenada X
def desafio_tranca_x(frase_x):
    
    #Variaveis de auxilio
    lista_alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    num_letra_repetida = 0
    num_letra_mais_repetida = 0
    num_letra_menos_repetida = 1000000

    #Transformando a frase toda em minuscula
    frase_x = frase_x.lower()

    #Loop que passa por cada letra da frase
    for letra in frase_x:
        #Verifica se a letra esta na lista alfabeto, se sim, exclui a letra da lista
        if letra in lista_alfabeto:
            lista_alfabeto.remove(letra)
        
        #Verifica se a letra nao eh uma espaco, se nao for, calcula quantas vezes a letra aparece na frase
        if letra != ' ':
            num_letra_repetida = frase_x.count(letra)

        #Verifica se a qtd de vezes que a letra aparece, eh maior do que a qtd da letra que mais aparece
        if num_letra_repetida > num_letra_mais_repetida:
            #Se sim, a salva como a que mais se repete
            num_letra_mais_repetida = num_letra_repetida

        #Verifica se a qtd de vezes que a letra aparece, eh menor do que a qtd da letra que menos aparece
        if num_letra_repetida < num_letra_menos_repetida:
            #Se sim, a salva como a que menos se repete
            num_letra_menos_repetida = num_letra_repetida 
    
    #Verifca se a lista do alfabeto foi zerada, vendo assim se eh um pangrama
    if len(lista_alfabeto) == 0:
        #Se for pangrama, imprimi e retorna a qtd de vezes que a letra que mais se repete na frase aparece
        print(f'A 1ª coordenada do Papai Noel é: {num_letra_mais_repetida}')
        return  num_letra_mais_repetida
    
    else:
        #Se nao for pangrama, imprimi e retorna a qtdde vezes que a letra que menos aparece se repete na frase
        print(f'A 1ª coordenada do Papai Noel é: {num_letra_menos_repetida}')
        return num_letra_menos_repetida

#Funcao relativa ao desafio da coordenada Y
def desafio_choque_y(frase_y):
    
    #Variaveis de auxilio
    vogais = ['a', 'e ', 'i','o','u','A','E','I','O','U']
    tamanho_palavra = len(frase_y)
    tem_vogal = False
    
    #Executa a funcao que calcula o num de Fibonnaci relativo ao tamanho da palavra
    num_resposta = numero_fibonnaci(tamanho_palavra)
    
    #Loop que passa pela frase e verifica se ela possui vogais
    for letra in frase_y:
        if letra in vogais:
            tem_vogal = True
    
    #Verifica se a palavra tem vogal, dependendo, multiplica a resposta pelo respectivo num certo
    if tem_vogal:
        num_resposta = num_resposta * 4
    
    else:
        num_resposta = num_resposta * 2
    
    #Imprimi e retorna o num da resposta da coordenada Y
    print(f'A 2ª coordenada do Papai Noel é: {num_resposta}')
    return num_resposta

#Funcao que calcula o num de fibbonaci
def numero_fibonnaci(num_sequencia):
    
    #Se for o numero 0 ou 1, retorna eles proprios como resposta
    if num_sequencia <= 1:
        return num_sequencia
    
    #Se for maior que 1 retornara a soma entre as 2 funcoes dos numeros anteriores
    #Fazendo assim uma funcao recessiva ate chegar no num 1 e 0
    else:
        return (numero_fibonnaci(num_sequencia - 1)) + (numero_fibonnaci(num_sequencia - 2))

#Funcao relativa a coordenada Z
def desafio_rapa_z(palavra_z,frase_z):

    #Variaveis de Auxilio
    lista_alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    lista_alfabeto_maisculo = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    diferenca_palavra = 0
    diferenca_frase = 0
    contador_maisculas = 0
    contador_minusculas = 0

    #Loop que passa pela palavra, e conta o num de letras maisculas e minusculas
    for letra in palavra_z:
        if letra in lista_alfabeto:
            contador_minusculas += 1
        
        elif letra in lista_alfabeto_maisculo:
            contador_maisculas += 1
    
    #Calculo da diferenca entre minusculas e maiusculas da palavra
    diferenca_palavra = contador_minusculas - contador_maisculas

    #Resetando o contador de maisculas e minusculas para contar a frase
    contador_maisculas = 0
    contador_minusculas = 0
    
    #Loop que passa pela frase e conta o num de maiusculas e minusculas dela
    for letra in frase_z:
        if letra in lista_alfabeto:
            contador_minusculas += 1
        
        elif letra in lista_alfabeto_maisculo:
            contador_maisculas += 1
    
    #Calculo da diferenca de minusculas e maiusculas da frase
    diferenca_frase = contador_minusculas - contador_maisculas

    #Calculo do resultado da coordenada
    resultado_z = int(diferenca_frase ** diferenca_palavra)

    #Imprimi e retorna a coordenada Z
    print(f'A 3ª coordenada do Papai Noel é: {resultado_z}')
    return resultado_z

#Funcao que calcula a distancia final entre Jack e Papai Noel
def distancia_final(x_noel,y_noel,z_noel,x_jack,y_jack,z_jack):
    
    #Calculo da distancia
    distancia_papai_noel_jack = float((((x_noel - x_jack)**2) + ((y_noel - y_jack)**2) + ((z_noel - z_jack)**2))**(1/2))

    #Retorna a distancia entre os dois
    return distancia_papai_noel_jack

#Funcao que gerencia e inicia todo o processo
def protocolo_distancia():

    #Recebe o input da frase x e o coloca como parametro do desafio X
    frase_x = input()
    cordenada_x = desafio_tranca_x(frase_x)

    #Recebe o input da frase y e o coloca como parametro do desafio Y
    frase_y = input()
    cordenada_y = desafio_choque_y(frase_y)

    #Recebe os inputs da palavra e fraze z, e os coloca como parametros do desafio Z
    palavra_z = input()
    frase_z = input()
    cordenada_z = desafio_rapa_z(palavra_z,frase_z)

    #Recebe as coordenadas de Jack
    x_jack = int(input())
    y_jack = int(input())
    z_jack = int(input())

    #Executa a funcao que calcula a distancia final, recebendo como parametros as coordenadas do Papai Noel e do jack
    resultado_distancia = distancia_final(cordenada_x,cordenada_y,cordenada_z,x_jack,y_jack,z_jack)

    #Imprimi a distancia entre eles
    print(f'A distância entre Jack Esqueleto e Papai Noel é: {resultado_distancia:.2f}')

#Executa a funcao principal
protocolo_distancia()
