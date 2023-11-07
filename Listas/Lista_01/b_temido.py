#Recebendo a frase e a caracteristica do monstro
frase_monstro = input()
carac_monstro = input()
monstro_nome = ''
monstro_v_f = False


#Lobisomen
if ((frase_monstro == "Parou filhotada, assim vocês vão deixar todo mundo maluco.") and (carac_monstro == "Uivar" or carac_monstro == "Pelos" or carac_monstro == "Caninos")):
    monstro = "Lobisomem"
    monstro_v_f = True

#Frankstein
elif ((frase_monstro == "Veio de novo pelo correio, deixa de ser pão duro.") and (carac_monstro == "Desmontável" or carac_monstro == "Parafusos" or carac_monstro == "Morto-vivo")):
    monstro = "Frankenstein"
    monstro_v_f = True

#Homem Invisivel
elif ((frase_monstro == "Quem me beliscou?") and (carac_monstro == "Transparente")):
    monstro = "Homem Invisível"
    monstro_v_f = True

#Mumia
elif ((frase_monstro == "Tô na área galera!") and (carac_monstro == "Enfaixado" or carac_monstro == "Morto-vivo")):
    monstro = "Múmia"
    monstro_v_f = True

#Imprimir mensgem monstro ou Humano
if monstro_v_f == True:
    print("Bem-vindos ao Hotel Transilvânia!")
    
    #Checkar para qual dos monstros sera mandada a mensagem e imprimi-la
    if monstro == "Lobisomem":
        print("Wayne, seu cachorrão.")
    
    elif monstro == "Frankenstein":
        print("Frank, assim vai acabar perdendo a cabeça.")
    
    elif monstro == "Homem Invisível":
        print("Griffin, prazer em vê-lo.")
    
    elif monstro == "Múmia":
        print("Murray, sempre soltando areia.")

else:
    print("UM HUMANO! Quem é você, e como você achou esse lugar?")