#Recebendo dados luta
sua_vida = int(input)
poder_sua_arma = int(input)
sua_habilidade_luta = int(input)
seu_poder_surpresa = int(input)
poder_arma_mascarado = int(input)
habilidade_luta_mascarado = int(input)
poder_surpresa_mascarado = int(input)
defesa_mascarado = int(input)
vivo = True
venceu_luta = False

#Calculo ataque sucedido ou não
if poder_sua_arma > poder_arma_mascarado and sua_habilidade_luta > habilidade_luta_mascarado and seu_poder_surpresa > poder_surpresa_mascarado:
    venceu_luta = True
    exit()

else:
    sua_vida -= defesa_mascarado
    if not sua_vida > 0:
        vivo = False

#Calculo habilidades pós perder luta
if not venceu_luta:
    poder_sua_arma = poder_sua_arma * 0.95
    sua_habilidade_luta = sua_habilidade_luta * 0.95
    seu_poder_surpresa = seu_poder_surpresa * 1.05

#Calculo segundo ataque


