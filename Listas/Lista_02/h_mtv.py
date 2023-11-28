numero_celebridades = int(input())
celebridade_ex_kanye = False
celebridade_ex_pique = False
celebridade_ex_crismartin = False
candidato_taylor = False
candidato_katy = False
candidato_ariana = False
candidato_beyonce = False
candidato_shakira = False
nome_candidato = "" 

for i in range(numero_celebridades):
    nome_celebridade = input()
    if nome_celebridade == "Kanye West":
        celebridade_ex_kanye = True

    elif nome_celebridade == "Gerard Piqué":
        celebridade_ex_pique = True

    elif nome_celebridade == "Chris Martin":
        celebridade_ex_crismartin = True
    
    print(f"Apresentador: Contamos com a ilustre presença de {nome_celebridade}, uma salva de palmas!")

while nome_candidato != "Início da Premiação":
    nome_candidato = input()
    if nome_candidato == "Taylor Swift":
        candidato_taylor = True
    elif nome_candidato == "Katy Perry":
        candidato_katy = True
    elif nome_candidato == "Ariana Grande":
        candidato_ariana = True
    elif nome_candidato == "Beyoncé":
        candidato_beyonce = True
    elif nome_candidato == "Shakira":
        candidato_shakira = True
    
    