#Variaveis globais para o codigo
frase_decifrada = []
frase = input()
valor_ascii = 0
valor_total = 0
contador_vazios = 0
tem_algorismo = False

#loop que passa por cada cacter da frase para se decifrar
for char in frase:
    
    #Verificando se o char é um espaço vazio, se for, não passara pelo processo de transformação
    if char == ' ':
        frase_decifrada.append(char)
        contador_vazios += 1
    
    #Processo para transformar o caracter, em sua representação em ascii, soma com o tamanho da frase
    ##No final, transforma o valor adquirido para o carcter que o representa na tabela
    else:
        valor_ascii = ord(char)
        valor_total = valor_ascii + len(frase)
        frase_decifrada.append(chr(valor_total))

#Loop que passa por todos os inteiros de 0 a 9, e verifica se algum esta na frase decifrada
for int in range(10):
        if str(int) in frase_decifrada:
            tem_algorismo = True

#Se tiver o inteiro, imprimira isto
if tem_algorismo:
    print(f'Algo de errado não está certo. Será que estou ficando doido?')

#Verificando se a quantidade de vazios é igual ao tamanho da frase decifrada
elif contador_vazios == len(frase_decifrada):
    print(f'Ué não tem nada para me decifrar aqui')

#Impressão da frase decifrada normalmente
else:
    print(f'Descobri o que a mensagem significa: ',end='')
    for char in frase_decifrada:
        print(char,end='')