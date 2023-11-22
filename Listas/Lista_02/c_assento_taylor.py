#Variaveis pincipais para o codigo
numero_musicas = 0
nome_musica = ""
pontos_musica = 0
pontos_total = 0

#Recebendo quantidade de musicas analisadas
numero_musicas = int(input())

#Recebendo nome das musicas conforme quantas musicas forem analisadas
for i in range(numero_musicas):
    nome_musica = input().lower()
    
    #Declarando pontos = 0, para não conflitar com os pontos de uma musica analisada anteriormente
    pontos_musica = 0
    
    #Calculando pontos que a musica recebera, dependendo do seu tamanho, e se cada letra é uma vogal ou conssoante
    for j in nome_musica:
        if j == "a" or j =="e" or j == "i" or j == "o" or j == "u":
            pontos_musica += 1
        
        else:
            pontos_musica += 2
    
    #Declarando pontos totais no primeiro loop
    if i == 0:
        pontos_total = pontos_musica
    
    #Declarando nas proximas repetições do loop
    else:
        pontos_total *= pontos_musica

#Declarando o numero do assento e imprimindo para a fã
numero_assento = pontos_total
print(f"Parabéns por adquirir o ingresso! Seu assento é o {numero_assento}, estamos ansiosos para vê-lo, vai ser incrível!")