#Funcao que decifra a palavra criptografada
def cifra_cesar(palavra_criptografada,num_posicoes,direcao):
    #Lista de aux do alfabeto
    alfabeto_maisculo = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    #Transforma a palavra criptografa em lista, ao inves de string
    palavra_criptografada = list(palavra_criptografada)
    
    #Para casos onde o input seja um numero de posicoes negativo
    #Inverte a direcao original para a inversa
    if int(num_posicoes) < 0:
        if direcao == 'R':
            direcao = 'L'
        else:
            direcao = 'R'

    #Loop que passa pela palavra criptografada
    for i in range(len(palavra_criptografada)):
        
        #Rebcebe o index da letra da palavra crip na lista do alfabeto
        i2 = alfabeto_maisculo.index(palavra_criptografada[i])
        
        #Se a direcao for R, avancara para a direita
        if direcao == 'R':
            #O indice sera igual ao resto do num de posicoes desejadas com 26
            i2 += (abs(int(num_posicoes)) % 26)
        
        #Para esquesda se for L
        elif direcao == 'L':
            i2 -= (abs(int(num_posicoes)) % 26)

        #Se o indice passar de 25, subtrai por 26 para retornar ao inicio da lista
        if i2 > 25:
            i2 -= 26

        #Troca a letra criptografada, pela letra certa
        palavra_criptografada[i] = alfabeto_maisculo[i2]

    #Retorna a palavra descriptografada
    return palavra_criptografada

#Funcao que calcula a distancia euclidiana
def distancia_euclides(x_atual,y_atual,x_destino,y_destino):
    x_atual = float(x_atual)
    y_atual = float(y_atual)
    x_destino = float(x_destino)
    y_destino = float(y_destino)

    #Formula calculo
    distancia = ((((x_atual - x_destino)** 2) + ((y_atual - y_destino)** 2))** (1/2))

    return distancia

#Funcao que recebe a distancia de duas cidades, e verifica a menor
def menor_valor(menor_distancia,distancia,cidade_mais_prox,cidade_verificada,indice_menor,indice_atual):
    
    #Verifica se a menor distancia atual, eh menor ou igual a distancia verificada
    if menor_distancia <= distancia:
        return menor_distancia,cidade_mais_prox,indice_menor
    
    #Se nao for, retorna a distancia verificada , a cidade analisada e o indice delas
    else:
        return distancia,cidade_verificada,indice_atual



#Funcao Principal
def main():

    #Recebe a qtd de cidades que o papai noel visitara
    num_cidades = int(input())
    info_cidades = []

    #Loop que recebe os inputs das cidades, e os salva em uma matriz
    for i in range(num_cidades):
        
        info_cidades.append(input().split(', '))
        

    #Declarando x e y iniciais
    x_atual = 0
    y_atual = 0

    #Loop que passa pela quantidade de cidade que salvaremos
    for i in range(len(info_cidades)):
        
        #Variaveis pra aux no inicio do loop
        menor_distancia = distancia_euclides(x_atual,y_atual,info_cidades[0][1],info_cidades[0][2])
        cidade_mais_prox = info_cidades[0][0]
        indice_menor = 0
        
        #Loop que passa novamente pela quantidade de cidades, para verificar qual esta mais perto da atual
        for j in range(len(info_cidades)):
            cidade_verificada = info_cidades[j][0]  
            
            #Calcula a distancia da cidade verificada
            distancia_verificada = distancia_euclides(x_atual,y_atual,info_cidades[j][1],info_cidades[j][2])
            
            #Retorna a menor distancia entre as duas, a cidade relativa a menor distancia, e o indice na lista relativo a tal
            menor_distancia,cidade_mais_prox,indice_menor = menor_valor(menor_distancia,distancia_verificada,cidade_mais_prox,cidade_verificada,indice_menor,j)
                

        #Executa a funcao para descriptografar a frase, utilizando da variavel que salva o menor indice para pegar as informacoes corretas     
        palavra_descriptografada = cifra_cesar(info_cidades[indice_menor][3],info_cidades[indice_menor][4],info_cidades[indice_menor][5])

        #Salva o novo x e y atual
        x_atual = float(info_cidades[indice_menor][1])
        y_atual = float(info_cidades[indice_menor][2])
        
        #Remove as info da cidade salva da lista 
        info_cidades.remove(info_cidades[indice_menor])

        #Imprimi a senha da cidade e a palavra descriptografada         
        print(f'A senha da cidade {cidade_mais_prox} é: ',end='')
        for k in range(len(palavra_descriptografada)):
            if k < len(palavra_descriptografada) - 1: 
                print(f'{palavra_descriptografada[k]}',end='')

            else:
                print(f'{palavra_descriptografada[k]}')

#Executa o codigo
main()
