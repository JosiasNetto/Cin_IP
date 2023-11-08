numero = int(input())
string_1, string_2, string_3 = input(), input(), input()

#Calculando Local com mais sinais, dependendo do numero recebido
lugar_sinal = str()
achou_lugar = True
    #Numero 1 muda o local para a string com o maior número de letras
if numero == 1:
    if len(string_1) > len(string_2) and len(string_1) > len(string_3):
        lugar_sinal = string_1
    
    elif len(string_2) > len(string_1) and len(string_2) > len(string_3):
        lugar_sinal = string_2
    
    elif len(string_3) > len(string_2) and len(string_3) > len(string_1):
        lugar_sinal = string_3
    
    elif len(string_1) == len(string_2) and len(string_1) == len(string_3):
        print("Droga! Ainda não consegui descobrir o local que possui mais sinais desconhecidos! Vou ter que ficar mais um tempo nessa Mansão Mal-Assombrada...")
        achou_lugar = False

    #Número 2 muda o local para a string com o menor número de letras
elif numero == 2:
    if len(string_1) < len(string_2) and len(string_1) < len(string_3):
        lugar_sinal = string_1
    
    elif len(string_2) < len(string_1) and len(string_2) < len(string_3):
        lugar_sinal = string_2
    
    elif len(string_3) < len(string_2) and len(string_3) < len(string_1):
        lugar_sinal = string_3
    
    elif len(string_1) == len(string_2) and len(string_1) == len(string_3):
        print("Droga! Ainda não consegui descobrir o local que possui mais sinais desconhecidos! Vou ter que ficar mais um tempo nessa Mansão Mal-Assombrada...")
        achou_lugar = False

if achou_lugar:
    print(lugar_sinal)

#Descobrindo sinal se o tamanho das palavras for igual
if not achou_lugar:
    sorted({string_1,string_2,string_3})
    if string_1 > string_2 and string_1 > string_3:
        lugar_sinal = string_1
        achou_lugar == True
        print(lugar_sinal)

    elif string_2 > string_1 and string_2 > string_3:
        lugar_sinal = string_2
        achou_lugar == True
        print(lugar_sinal)

    elif string_3 > string_2 and string_3 > string_1:
        lugar_sinal = string_3
        achou_lugar == True
        print(lugar_sinal)

    elif string_1 == string_2 and string_1 == string_3:
        print("AAAAAA! Um fantasma me assustou!")
        print("(Uma mensagem apareceu no monitor que você estava usando. ""Agente, um erro inesperado aconteceu. A EPF contactará você novamente quando tudo estiver funcionando da forma correta. Nosso sistema foi invadido por alguém que se identifica como Hubert P.Enguin"")")
#Achado o local com mais sinais, imprimi a mensagem
if achou_lugar:
    print("(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando.\"Muito bem agente. A EPF agradece os seus esforços\"")

#Impressão Final independente de qualquer resultado
print("(Depois de ler a mensagem, você dormiu. Ao acordar, você não estava mais no CIn de outubro de 2012, mas no CIn de 2023, sem acreditar na situação que vivenciou)")