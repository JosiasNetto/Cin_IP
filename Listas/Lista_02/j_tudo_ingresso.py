numero_amigos = 0
nome_amigo = ""
local_show = ""
valor_ingresso = 0
valor_carteira = 0
tempo_grad = 0

computadores_disponiveis = int(input)
valor_carteira = int(input())
tempo_grad = int(input())

nome_amigo = input()
while nome_amigo != "end":
    if nome_amigo != "laura" and nome_amigo != "carlos" and nome_amigo != "roberto":
        numero_amigos += 1
    nome_amigo = input()

if numero_amigos > 0:
    amigos_trabalhando = computadores_disponiveis 