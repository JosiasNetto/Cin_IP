#Recebendo respostas certas
resposta_correta_1 = input()
resposta_correta_2 = input()
resposta_correta_3 = input()

#Sequencia de perguntas, onde se estiver correta, imprimi a resposta e vai para a proxima
#pergunta 1
pergunta = input()
resposta = input()
acertou = False

if resposta == resposta_correta_1:
    print("Muito bem! Olha como a primeira foi fácil, seu amigo talvez sobreviva. Falta só mais duas para acabar com isso!")
    acertou = True

else:
    print("A resposta está e…e…rrada hahahahaha. Essa é a parte que eu mais gosto, venha aqui no quintal, você pode dar um adeus!")

#pergunta 2
if acertou:
    pergunta = input()
    resposta = input()

    if resposta == resposta_correta_2:
        print("A resposta está e…exata! Você é mais inteligente do que eu pensei, já posso caprichar nesta última, vamos ver se você realmente conhece filmes de terror!")

    else:
        print("A resposta está e…e…rrada hahahahaha. Essa é a parte que eu mais gosto, venha aqui no quintal, você pode dar um adeus!")
        acertou = False

    #pergunta 3
    if acertou:
        pergunta = input()
        resposta = input()

        if resposta == resposta_correta_3:
            print("Droga, não vai ser hoje que vou ver sangue, que pena! Mas não se esqueça de mim, quem sabe um dia algum dos seus amigos não queiram brincar para lhe salvar!")

        else:
            print("A resposta está e…e…rrada hahahahaha. Essa é a parte que eu mais gosto, venha aqui no quintal, você pode dar um adeus!")