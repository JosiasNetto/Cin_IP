def ajustando_palavra(palavra):
    palavra = f'0{palavra}'
    if len(palavra) < 32:
        palavra = ajustando_palavra(palavra)
    
    return palavra



def byte_na_palavra(byte,palavra,qtd_tentativas,contador):
    
    if byte in palavra:
        print(f'Muito bem! Estamos dentro! Vamos queimar essa cidade!!')

    else:
        print(f'Não é essa a senha, estamos ficando sem tempo.')
        contador += 1
        
        if contador < qtd_tentativas:
            byte = input()
            byte_na_palavra(byte,palavra,qtd_tentativas,contador)
        
        else:
            print('Corre Keanu! Eles nos descobriram!!')

            
palavra = input()
qtd_tentativas = int(input())
byte = input()
contador = 0

if len(palavra) < 32:
    palavra = ajustando_palavra(palavra)

if qtd_tentativas > 0:
    byte_na_palavra(byte,palavra,qtd_tentativas,contador)