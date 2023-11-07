#Recebendo as variáveis
nome_vitima = input()
nome_antagonista = input()
tipo_armadilha = ()
tempo = float(input())
armadilha_certa = False
tipo_sobrev = ""

#calculo se a armadilha corresponde a seu autor e se sobrevive a armadilha
if nome_antagonista == "John Kramer" and tipo_armadilha == "Armadilha de urso reversa":
    armadilha_certa = True
    
    if tempo >= 5:
        tipo_sobrev = "Facil"
    
    elif tempo >= 2.5 and tempo < 5:
        tipo_sobrev = "Dificuldade"
    
    elif tempo < 2.5:
        tipo_sobrev = "morre"

elif nome_antagonista == "John Kramer" and tipo_armadilha == "Tanque de agua":
     armadilha_certa = True
    
    if tempo >= 4:
        tipo_sobrev = "Facil"
    
    elif tempo >= 2 and tempo < 4:
        tipo_sobrev = "Dificuldade"
    
    elif tempo < 2:
        tipo_sobrev = "morre"