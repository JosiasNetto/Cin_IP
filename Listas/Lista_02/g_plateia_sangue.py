#Principais Variaveis para o codigo
numero_versos = 0
plateia_nota = 0
contador_verso = 0

#Recebendo numero de versos a serem cantados, e fazendo loop dependendo do seu tamanho
numero_versos = int(input())
for i in range(numero_versos):
    #Olhando em que verso esta, imprimindo frase e lendo o que a plateia fala, dependendo do verso
    if i == 0:
        print("Cause, baby, now we've got")
        plateia_frase = input().upper()
        if plateia_frase == "BAD BLOOD":
            print("BAD BLOOD")
            plateia_nota += 1
    
    elif i == 1:
        print("You know it used to be")
        plateia_frase = input().upper()
        if plateia_frase == "MAD LOVE":
            print("MAD LOVE")
            plateia_nota += 1

    elif i == 2:
        print("So take a look what")
        plateia_frase = input().upper()
        if plateia_frase == "YOU'VE DONE":
            print("YOU'VE DONE")
            plateia_nota += 1
    
    elif i == 3:
        print("Cause, baby, now we've got")
        plateia_frase = input().upper()
        if plateia_frase == "BAD BLOOD, HEY":
            print("BAD BLOOD, HEY")
            plateia_nota += 1
    

#Vendo se a plateia acertou tudo, pelo menos metade  ou menos que a metade.
if numero_versos == plateia_nota:
    print("A plateia deu um show! Acertou tudo!")

elif (numero_versos / 2) <= plateia_nota:
    print("A plateia acertou a maior parte da música")

else:
    print("Foi um dia atípico e a plateia se esqueceu de grande da música")