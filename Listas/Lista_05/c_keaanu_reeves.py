def ajustando_palavra(palavra): #Função que add os 0 na palavra
    
    palavra = f'0{palavra}' #Add o 0 na esquerda
    if len(palavra) < 32:   #Se a palavra ainda for menor que 32, executa a função novamente
        palavra = ajustando_palavra(palavra)
    
    return palavra



def byte_na_palavra(byte,palavra,qtd_tentativas,contador):  #Funcção que verifica se o byte esta na palavra, e ja imprimi a msg correta
    
    if byte in palavra: #Verifica se o byte eh um elemento da sequencia de strings
        print(f'Muito bem! Estamos dentro! Vamos queimar essa cidade!!')    #Imprimi a msg que deu certo

    else:   #Imprimi que deu errado  e aumenta 1 no contador
        print(f'Não é essa a senha, estamos ficando sem tempo.')
        contador += 1   
        
        if contador < qtd_tentativas:   #Verifica se o contador esta menor que a qtd de tentativas disponiveis
            byte = input()  #Recebe o novo byte
            byte_na_palavra(byte,palavra,qtd_tentativas,contador)   #Executa a função novamente com o novo byte
        
        else:   #Caso nenhum byte seja a senha correta
            print('Corre Keanu! Eles nos descobriram!!')

def main():          
    palavra = input()   #Palavra do Firewall
    qtd_tentativas = int(input())   #Quantas vezes tentara a senha
    byte = input()  #Recebendo o primeiro byte pra decifrar a senha
    contador = 0    #Variavel aux

    if len(palavra) < 32:   #Verifica se a palara tem menos de 32 caracteres
        palavra = ajustando_palavra(palavra)    #Executa a função que add os 0 na esquerda do caracter

    if qtd_tentativas > 0:  #Verifica tem tentativas
        byte_na_palavra(byte,palavra,qtd_tentativas,contador)   #Executa a função que recebe os bytes, e ja diz se eh a senha certa

main()