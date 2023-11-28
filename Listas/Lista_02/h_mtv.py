#Principais Variaveis do codigo
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
candidato_ganhador = ""

#Loop que repete dependendo do numero de celebridades, mas so guarda em varial, se alguns especificos aparecerem
for i in range(numero_celebridades):
    nome_celebridade = input()
    if nome_celebridade == "Kanye West":
        celebridade_ex_kanye = True

    elif nome_celebridade == "Gerard Piqué":
        celebridade_ex_pique = True

    elif nome_celebridade == "Chris Martin":
        celebridade_ex_crismartin = True
    
    print(f"Apresentador: Contamos com a ilustre presença de {nome_celebridade}, uma salva de palmas!")

#Loop que recebe o nome de cada uma das 5 candidatas, e guarda em uma variavel qual compareceu
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
    

print("Apresentador: Vamos deixar de enrolação e ir para a premiação!")

#Sequencia que confere quem eh a vencedora, baseada na hierarquia do premio. Imprimindo diretamente na checkagem quem ganhou, e vendo se seu ex compareceu para falar
if candidato_taylor:
    candidato_ganhador = "TAYLOR SWIFT"
    print("Apresentador: E a artista do ano do MTV Video Music Awards 2023 é...")
    print(f"{candidato_ganhador}")
    if celebridade_ex_kanye:
        print("Kanye West: Eu vou te deixar terminar. Estou feliz por você, mas Beyoncé fez um dos melhores vídeos de todos os tempos.")

elif candidato_katy:
    candidato_ganhador = "KATY PERRY"
    print("Apresentador: E a artista do ano do MTV Video Music Awards 2023 é...")
    print(f"{candidato_ganhador}")

elif candidato_ariana:
    candidato_ganhador = "ARIANA GRANDE"
    print("Apresentador: E a artista do ano do MTV Video Music Awards 2023 é...")
    print(f"{candidato_ganhador}")

elif candidato_beyonce:
    candidato_ganhador = "BEYONCÉ"
    print("Apresentador: E a artista do ano do MTV Video Music Awards 2023 é...")
    print(f"{candidato_ganhador}")
    if celebridade_ex_crismartin:
        print("Chris Martin: Minha heroína, minha irmã, meu tudo. Você merece!")

elif candidato_shakira:
    candidato_ganhador = "SHAKIRA"
    print("Apresentador: E a artista do ano do MTV Video Music Awards 2023 é...")
    print(f"{candidato_ganhador}")
    if celebridade_ex_pique:
        print("Gerard Piqué: Meu amor me perdoa, volta pra mim...")

