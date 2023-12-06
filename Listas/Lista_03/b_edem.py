#Lista com as respostas certas
##Cada elemento é um conjunto de resposta certa
respostas_certas = [["Zeus", "trovão", "deus"], ["Afrodite", "amor", "deusa"], ["Poseidon", "oceanos", "deus"], ["Hércules", "força", "semideus"], ["Aquiles", "resistência", "semideus"], ["Orfeu", "música", "semideus"]]
#Variaveis de auxilio para o codigo
percy_acertou = False
acertos_individuais = 0
acertos_questoes = 0

#Recebendo o numero de questões a serem respondidas
num_questoes = int(input())
if num_questoes > 0:
    #Loop relacionado ao numero de questoes que percy respondera
    for x in range(1,num_questoes + 1):
        percy_acertou = False
        #Recebendo a resposta do percy, e a transformando em uma lista
        resposta_percy = input().split(", ")

        #Loop que passa pela lista das respostas corretas
        for y in range(len(respostas_certas)):
            acertos_individuais = 0
            
            #Loop relacionado as respostas do percy
            ##Verifica se todos os 3 elementos da resposta do percy, estao ao mesmo tempo, em alguma das listas da resposta certa
            for z in range(len(resposta_percy)):
                if resposta_percy[z] in respostas_certas[y]:
                    acertos_individuais += 1
                
                #Para cada elemento da resposta, que existir dentro da lista, eh contabilizado um ponto
                ##Se obtiver 3 pontos, quer dizer que a resposta esta igual a aquela da lista
                if acertos_individuais == 3:
                    print(f"A resposta da {x}ª questão está... CORRETA!")
                    acertos_questoes += 1
                    percy_acertou = True

        if not percy_acertou:
            print(f"A resposta da {x}ª questão está... ERRADA!")

    #Calculando porcentagem de acertos do percy, e a imprimindo            
    porcentagem_acerto = int((acertos_questoes / num_questoes) * 100)
    print(f"Percy Jackson, sua taxa de acerto no EDEM é de aproximadamente... {porcentagem_acerto}%")

    #Imprimindo resultado do percy dependendo de seus acertos
    if porcentagem_acerto == 100:
        print("UAU, você gabaritou! Você é praticamente um deus do Olimpo!")

    elif porcentagem_acerto >= 60:
        print("Muito bem, você quase pode começar a desfilar entre os semideuses!")

    elif porcentagem_acerto >= 20:
        print("Você pode melhorar um pouco mais!")

    else:
        print("Bem... te vejo ano que vem")

else:
    print("Infelizmente, Percy Jackson, chegou atrasado para a exame...")