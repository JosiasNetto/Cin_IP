nome_pretendente = input()
palavra_pretendente = input()
palavra_taylor = input()
palavra_igual = ""


while palavra_pretendente != "vou dormir":
    for char in palavra_pretendente:
        if char in palavra_taylor:
            palavra_taylor = palavra_taylor.replace(char,"",1)
        
        if palavra_taylor == "":
            print(f"você acertou, estreou na lista! {nome_pretendente}")
        
        else:
            print("perdeu covarde!")
        
    nome_pretendente = input()
    if nome_pretendente != "vou dormir":
        palavra_pretendente = input()
        palavra_taylor = input()

        
