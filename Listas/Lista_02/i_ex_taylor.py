#Recebendo Nome fora do loop(Facilita caso a primeira frase ja seja "vou dormir")
nome_pretendente = input()

#Loop Para comparar as palavras do pretendente e da taylor, e verificar se são iguais
while nome_pretendente != "vou dormir":
    palavra_pretendente = input()
    palavra_taylor = input()
    #Loop para verificar se cada caracter do pretendente, é igual a um caracter da palavra da taylor
    for char in palavra_pretendente:
        if char in palavra_taylor:
            #Se o caracter for igual, retirar da palavra da taylor, esvitando que veja o mesmo caracter mais de uma vez
            palavra_taylor = palavra_taylor.replace(char,"",1)

    #Checkagem se a palavra do pretendente pode formar a da taylor
    ##Pois, se tiverer a quantidade suficiente de caracteres iguais, toda a palavra da taylor sera excluida    
    if palavra_taylor == "":
        print(f"você acertou, estreou na lista! {nome_pretendente}")
    
    else:
        print("perdeu covarde!")

    #Recebendo o nome do proximo pretendente    
    nome_pretendente = input()
