#Princpais Variaveis utilizadas no Loop
lugar_show = ""
codigos_pessoas = ""
codigos_vip = 0
virus = False
ajudou = False

#Recebendo lugar do show, e iniciando um loop baseado em se o codigo de finalização for mandado, ou receber o do virus
lugar_show = input()
while codigos_pessoas != "0000" and not virus:
    #Recebendo codigo das pessoas, e apenas contando se forem vips
    codigos_pessoas = input()
    if codigos_pessoas == "1000":
        print("Mais um VIP! Não podemos esquecer de contabilizá-lo.")
        codigos_vip += 1
    
    elif codigos_pessoas == "1001":
        print("Ingresso Normal. Não iremos contabilizá-lo.")
    
    elif codigos_pessoas == "1002":
        print("Ele ficará na frente do show, porém não é VIP! Não será contabilizado também.")
    
    elif codigos_pessoas == "1003":
        print("Espera, quem é esse? Ele não pagou! Não devemos sequer analisar sua entrada.")
    
    #Codigo do virus, que inicia um loop ate ser mandado o texto de ajuda, que ira para-lo
    elif codigos_pessoas == "1004":
        print("Esse código não existe! O sistema quebrou...")
        print("Vamos aguardar até que o suporte nos ajude.")
        virus = True
        while not ajudou:
            texto_ajuda = input()
            if texto_ajuda == "Ajudou":
                ajudou = True
            else:
                print("Ainda não...")
#Imprimindo onde sera e os assentos Vips do show
print(f"O show da Taylor Swift será em {lugar_show} e contará com {codigos_vip} VIPs!")