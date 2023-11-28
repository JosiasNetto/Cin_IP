#Principais Variaveis para o codigo
numero_versos = 0
plateia_nota = 0
contador_verso = 0
frase_maiuscula = ""

#Recebendo numero de versos a serem cantados, e fazendo loop dependendo do seu tamanho
numero_versos = int(input())
for i in range(numero_versos):
    #Olhando em que verso esta, imprimindo frase e lendo o que a plateia fala, dependendo do verso
    frase_maiuscula = ""
    if i == 0:
        print("Cause, baby, now we've got")
        plateia_frase = input()
        #Loop para gerar frase toda maiuscula a partir do upper de cada caracter
        for j in plateia_frase:
            frase_maiuscula += j.upper()
        if frase_maiuscula == "BAD BLOOD":
            print("BAD BLOOD")
            plateia_nota += 1
    
    elif i == 1:
        print("You know it used to be")
        plateia_frase = input().upper()
        for j in plateia_frase:
            frase_maiuscula += j.upper()
        if frase_maiuscula == "MAD LOVE":
            print("MAD LOVE")
            plateia_nota += 1

    elif i == 2:
        print("So take a look what")
        plateia_frase = input().upper()
        for j in plateia_frase:
            frase_maiuscula += j.upper()
        if frase_maiuscula == "YOU'VE DONE":
            print("YOU'VE DONE")
            plateia_nota += 1
    
    elif i == 3:
        print("Cause, baby, now we've got")
        plateia_frase = input().upper()
        for j in plateia_frase:
            frase_maiuscula += j.upper()
        if frase_maiuscula == "BAD BLOOD, HEY":
            print("BAD BLOOD, HEY")
            plateia_nota += 1
    

#Vendo se a plateia acertou tudo, pelo menos metade  ou menos que a metade.
if numero_versos == plateia_nota:
    print("A plateia deu um show! Acertou tudo!")

elif (numero_versos / 2) <= plateia_nota:
    print("A plateia acertou a maior parte da música")

else:
    print("Foi um dia atípico e a plateia se esqueceu de grande da música")