import random

tam = 15  #tamanho do tabuleiro
numb = 5  #numero de buracos
tamd = 3  #numero de faces do dado

v = [0] * (tam + 1)  # 0-trilha 1-buraco
t = ['x'] * (tam + 1)

#gera tabuleiro (inteiro)

#buraco
i = 0
while i < numb:
    p = random.randint(1, tam)
    if v[p] == 0:
        v[p] = 1
        i = i + 1

#gera tabuleiro (string)
for i in range(1, tam + 1):
    if v[i] == 0:
        t[i] = "x"
    else:
        t[i] = "o"
t[0] = 'J12'
print("Inicio")
print(t)

vitoria = False
rodada = 0
j1 = 0
j2 = 0

while not vitoria:
    dado = random.randint(1, tamd)

    #jogador 1
    if rodada % 2 == 0:
        # vitoria
        if j1 + dado >= tam:
            print("Jogador 1 tirou ", dado)
            print("VITORIA DO JOGADOR 1")
            vitoria = True
        else:
            print("Jogador 1 tirou ", dado)

            #buraco
            if v[j1 + dado] == 1:
                print("Buraco")
            else:
                #origem
                if t[j1] == 'J12':
                    t[j1] = "J2"
                else:
                    if v[j1] == 0:
                        t[j1] = "x"
                    else:
                        t[j1] = "o"

                #destino
                if t[j1 + dado] == 'J2':
                    t[j1 + dado] = 'J12'
                else:
                    t[j1 + dado] = "J1"

                j1 = j1 + dado

    #jogador 2
    else:
        # vitoria
        if j2 + dado >= tam:
            print("VITORIA DO JOGADOR 2")
            vitoria = True
        else:
            print("Jogador 2 tirou ", dado)

            # buraco
            if v[j2 + dado] == 1:
                print("Buraco")
            else:
                # origem
                if t[j2] == 'J12':
                    t[j2] = "J1"
                else:
                    if v[j2] == 0:
                        t[j2] = "x"
                    else:
                        t[j2] = "o"

                # destino
                if t[j2 + dado] == 'J1':
                    t[j2 + dado] = 'J12'
                else:
                    t[j2 + dado] = "J2"

                j2 = j2 + dado

    #impressao do tabuleiro
    print(t, "\n")
    rodada = rodada + 1
