#Mensagem inicial
nome = str(input("Ola, Bom dia! Digite seu nome:"))
print("Bom dia " + nome + "!")
#Calculo do gasto de calorias no ano
tx_meta_basal = int(input("Agora por favor, me diga quantas calorias voce gasta em um dia sem fazer esforco:"))
cal_atv_fisica = int(input("Massa! Agora diga quantas calorias em media voce gasta quando faz um exercicio:"))
atv_semana = int(input("Uhh, e quantas vezes voce se exercita na semana?"))
mes_descanso = int(input("E quantos meses voce descansa?"))
cal_basal = (tx_meta_basal * 7 * 4 * 12)
cal_total_atv_fisica = (cal_atv_fisica * atv_semana * 4 * (12-mes_descanso))
calorias_gastas_ano = (cal_basal + cal_total_atv_fisica)
#Mensgaem de quantas calorias gasta
print(nome + "! voce gasta um total de:" + str(calorias_gastas_ano) + "calorias no ano!")
print("Agora vamos fazer o calculo de quantas voce consome!" )
#Calculo calorais consumidas
cal_cons_ref = int(input("Digite quantas calorias voce consome por refeição:"))
ref_dia = int(input("Legal! E quantas vezes voce come no dia?"))
cal_cons_ano = int((cal_cons_ref * ref_dia) * 7 * 4 * 12)
#Mensagem calorias consumidas
print("Ja calculamos as suas calorias consumidas " + nome + "!")
print("Voce consome um total de:" + str(cal_cons_ano) + "calorias por ano")
if(cal_cons_ano > calorias_gastas_ano):
    print("Infelizmente voce não conseguira emagrecer")
else:
    print("Voce conseguira emagrecer!")