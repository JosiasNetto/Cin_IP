#Recebendo as variáveis
nome_vitima = input()
nome_antagonista = input()
tipo_armadilha = input()
#Divide por 60 pois transforma de segundos para minutos
tempo = float(input()) / 60

#Checkagem se armadilha combina com o autor, se sobrevive ou não e impressão da mensagem se sobreviver
if nome_antagonista == "John Kramer" and tipo_armadilha == "Armadilha de urso reversa":
    
    if tempo >= 5:
        print(f"Com tempo de sobra, {nome_vitima} consegue retirar a armadilha de sua cabeça, sobrevivendo com sucesso ao jogo de Jigsaw.")
    
    elif tempo >= 2.5 and tempo < 5:
        print(f"À beira de perder a cabeça, e desafiando as expectativas de seu algoz, {nome_vitima} remove a armadilha de urso e por pouco escapa de um destino cruel.")
    
    elif tempo < 2.5:
        print("Game Over...")

elif nome_antagonista == "John Kramer" and tipo_armadilha == "Tanque de agua":
    
    if tempo >= 4:
        print(f"{nome_vitima} usa suas práticas de respiração na natação a seu favor, vencendo o jogo de Jigsaw sem perder muito fôlego.")
    
    elif tempo >= 2 and tempo < 4:
        print(f"{nome_vitima} passa por maus bocados, mas vira o jogo e consegue evitar, no limite, seu afogamento dentro da armadilha.")
    
    elif tempo < 2:
        print("Game Over...")

elif nome_antagonista == "Amanda Young" and tipo_armadilha == "Caixa de laminas":
    
    if tempo >= 10:
        print(f"Apenas com ferimentos leves, {nome_vitima} se liberta rapidamente das perigosas lâminas da armadilha montada pela discípula de Jigsaw.")
    
    elif tempo >= 6 and tempo < 10:
        print(f"Por um triz, {nome_vitima} sobrevive ao jogo de Amanda, mas com lesões profundas em suas mãos e braços.")
    
    elif tempo < 6:
        print("Game Over...")

elif nome_antagonista == "Amanda Young" and tipo_armadilha == "Asas de anjo":
    
    if tempo >= 3:
        print(f"Com surpreendente facilidade, {nome_vitima} alcança a chave da armadilha e vence o desafio da aprendiz de Jigsaw.")
    
    elif tempo >= 1.5 and tempo < 3:
        print(f"{nome_vitima} desafia as possibilidades e o cruel anseio de sua algoz, escapando da armadilha com poucas queimaduras e arranhões.")
    
    elif tempo < 1.5:
        print("Game Over...")

else:
    exit()
    