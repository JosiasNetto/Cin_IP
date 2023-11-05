D = int(input())
P = str
if (D <= 10):
    P = "Arthur"

else:
    if(D <= 30):
        P = "Luiz"
    else:
        if(D <= 100):
            P = "Pedro"
        else:
            P = "Nenhum"

print(P)