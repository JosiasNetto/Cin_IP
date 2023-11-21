#Variaveis principai para o codigo
quant_musica = 0
pontos = 0
frase = ""

#Recebendo Musica ou frase, e calculando os pontos da plateia dependendo do caso
while (pontos >= 0 and frase != "long live"):
    frase = input()
    if frase == "os fãs estão formando uma ciranda":
        pontos -= 3 

    elif frase == "os fãs estão ligando os flashes e atrapalhando a visão" or frase == "os fãs estão dançando na frente da tela" or frase == "os fãs estão gritando o nome da Taylor e atrapalhando a música":
        pontos -= 2
    
    elif frase == "os fãs estão cantando as músicas em coro" or frase == "houve um pedido de casamento na sessão":
        pontos += 2
    
    else:
        pontos += 1
        quant_musica += 1
#Imprimindo se o filme foi terminado e a quantidade de musicas tocadas
else:
    if pontos < 0:
       print(f"A Taylor só conseguiu cantar {quant_musica} músicas e a sessão foi interrompida.")
    
    elif frase == "long live":
        print(f"A Taylor conseguiu concluir o show sem muitas interrupções e cantou {quant_musica} músicas.")
