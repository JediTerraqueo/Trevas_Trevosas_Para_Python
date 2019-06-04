#                  ENTRADA
# 0<=N<=1000, indica o número de partidas;
# linha 1 - indica o nome do primeiro jogador;
# linha 2 - indica o nome do segundo jogador;
# os nomes dos jogadores só podem ter até 10 letras;
# os nomes não podem ter espaços em branco;
# as N linhas tem dois inteiros entre 0 e 5, A e B;
# em todas as partidas, o primeiro jogador sempre escolhe par;
# O final da entrada é indicada por N = 0;


#                     SAIDA

# Identificador do conjunto, como "Teste N";
# As N linhas seguintes devem conter o nome do ganhador;
#               *LINHA EM BRANCO*

#              *INICIO DO PROGRAMA*



teste = 0
c = 0
while c == 0:
    i = 0
    list_P = [0, 2, 4, 6, 8, 10]
    list_I = [1, 3, 5, 7, 9]
    N = int(input())
    if N >= 0 and N <=1000:
        if N == 0:
            break
        nome1 = str(input())
        if len(nome1) >= 0 and len(nome1) <= 10:
            nome2 = str(input())
            if len(nome2) >= 0 and len(nome2) <= 10:
                teste = teste + 1
                if teste >= 2:
                    print("\n")
                print('Teste', teste)
                while i != N:
                    D = 0
                    A, B = (input()).split(" ")
                    A = int(A)
                    B = int(B)
                    if A >= 0 and A<= 5:
                        if B >= 0 and B <= 5:
                            i = i + 1
                            D = A + B
                            if D in list_P:
                                print(nome1)

                            elif D in list_I:
                                print(nome2)
                        else:
                            break
                    else:
                        break
            else:
                break
        else:
            break

    else:
        break