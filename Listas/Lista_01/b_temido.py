#Recebendo a frase e a caracteristica do monstro
frase_monstro = input()
carac_monstro = input()
monstro_nome = ''
monstro_v_f = False


#Lobisomen
if (frase_monstro == "Parou filhotada, assim vocês vão deixar todo mundo maluco.") and (carac_monstro == "Uivar" or carac_monstro == "Pelos" or carac_monstro == "Caninos"):
    monstro = "Lobisomem"

#Frankstein
elif (frase_monstro == "Veio de novo pelo correio, deixa de ser pão duro.") and (carac_monstro == "Desmontável" or carac_monstro == "Parafusos" or carac_monstro == "Morto-vivo"):
    monstro = "Frankenstein"

#Homem Invisivel
elif (frase_monstro == "Quem me beliscou?") and (carac_monstro == "Transparente"):
    monstro = "Homem Invisível"

#Mumia
elif (frase_monstro == "Tô na área galera!") and (carac_monstro == "Enfaixado" or carac_monstro == "Morto-vivo"):
    monstro = "Múmia"

#Imprimir mensgem monstro ou Humano
if monstro_v_f == 

