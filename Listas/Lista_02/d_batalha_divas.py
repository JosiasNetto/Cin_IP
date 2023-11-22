#Declarando Variaveis antes do loop
numero_apresentacoes = int(input())
rodadas_ganhas_taylor = 0
rodadas_ganhas_beyonce = 0
placar_vencedor = 0
placar_perdedor = 0
apresentacao_acontecendo = True

#Loop que representa toda a apresentacao, dependendo do numero de apresentacoes declarada
print("Vai começar! Vamos ver quem é a verdadeira diva!")
for i in range(numero_apresentacoes):
    if apresentacao_acontecendo:
        print(f"Vai começar a {i + 1}º rodada!")
        #Recebendo variaveis das notas da apresentacao
        nota_coreo_taylor = int(input())
        nota_figurino_taylor = int(input())
        nota_coreo_beyonce = int(input())
        nota_figurino_beyonce = int(input())

        #Calculando nota final de cada estrela
        nota_final_taylor = ((nota_coreo_taylor * 4) + (nota_figurino_taylor * 3))
        nota_final_beyonce = ((nota_figurino_beyonce * 3) + (nota_coreo_beyonce * 4))

        #Verificando quais das notas eh maior e declarando a vencedora da rodada
        if nota_final_taylor > nota_final_beyonce:
            rodadas_ganhas_taylor += 1
            vencedora_rodada = "Tay"
            placar_vencedor = nota_final_taylor
            placar_perdedor = nota_final_beyonce
        
        else:
            rodadas_ganhas_beyonce += 1
            vencedora_rodada = "Bey"
            placar_vencedor = nota_final_beyonce
            placar_perdedor = nota_final_taylor
        
        #imprimindo vencedora da rodada
        print(f"Fim da apresentação! O placar da rodada {i + 1} foi {placar_vencedor}x{placar_perdedor} para os representantes da {vencedora_rodada}.")

        #Calculando a diferenca de pontos entre os placares, e imrpimindo dependendo do seu tamanho
        diferenca_placar = abs(nota_final_beyonce - nota_final_taylor)
        if diferenca_placar > 20:
            print(f"A diferença na pontuação foi de {diferenca_placar} pontos.")
        
        else:
            print(f"A diferença de pontos foi de apenas {diferenca_placar}.")
        
        if rodadas_ganhas_taylor == 3 or rodadas_ganhas_beyonce == 3:
            apresentacao_acontecendo = False

#Verificando quem ganou mais rodadas, e imprimindo a vencedora
if rodadas_ganhas_beyonce > rodadas_ganhas_taylor:
    print(f"Minha nossa! A equipe da Beyoncé chocou o mundo e venceu a equipe da Taylor Swift por um placar de {rodadas_ganhas_beyonce} a {rodadas_ganhas_taylor}. A Bey é a verdadeira rainha do pop!")

else:
    print(f"Uuuh! Por um placar de {rodadas_ganhas_taylor} a {rodadas_ganhas_beyonce}, a equipe da Taylor Swift venceu a competição e mostrou que ela é a verdadeira diva do pop!")