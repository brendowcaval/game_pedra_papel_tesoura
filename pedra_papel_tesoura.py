# Desenvolvido por Brendow Cavalcante
# Projeto : Jogo de pedra, papel e tesoura

import random
import os
import time





def verificando_decisoes(decisao_usuario, decisao_maquina):
    if decisao_usuario == decisao_maquina:
        return "empate"
    elif decisao_usuario == "pedra" and decisao_maquina == "tesoura":
        return "usuário ganha"
    elif decisao_usuario == "papel" and decisao_maquina == "pedra":
        return "usuário ganha"
    elif decisao_usuario == "tesoura" and decisao_maquina == "papel":
        return "usuário ganha"
    else:
        return "máquina ganha"


jogo = jogo_andamento = True
 



while jogo:
    os.system('cls')
    print("               GAME PEDRA, PAPEL E TESOURA ")
    print("[1] iniciar partida")
    print("[2] como jogar")
    print("[3] sair")

    resposta_inicial  = int(input())
    os.system('cls')

    if resposta_inicial == 1:
        pontos_usuario = pontos_maquina = 0
        aviso = escolha_usuario = escolha_maquina = ""
        opcoes_maquina = ["pedra", "papel", "tesoura"]

        while jogo_andamento:
            os.system('cls')
            print(f"usuário : {pontos_usuario}/10           maquina : {pontos_maquina}/10")
            print(aviso.upper())
            print(escolha_usuario)
            print(escolha_maquina)

            print("[]pedra    []papel    []tesoura")
            valor_usuario = input()
            valor_maquina = opcoes_maquina[random.randrange(0,3)]

            if verificando_decisoes(valor_usuario, valor_maquina) == "empate":
                aviso = "empate"
                escolha_usuario = "você escolheu " + valor_usuario
                escolha_maquina = "máquina escolheu " + valor_maquina


            elif verificando_decisoes(valor_usuario, valor_maquina) == "usuário ganha":
                aviso = "você venceu"
                pontos_usuario = pontos_usuario + 1
                escolha_usuario = "você escolheu " + valor_usuario
                escolha_maquina = "máquina escolheu " + valor_maquina
                
                # fim da partida e oportunidade de jogar novamente
                if pontos_usuario == 10:
                    os.system('cls')
                    print("VOCÊ GANHOU A PARTIDA!")
                    time.sleep(3)
                    print("quer jogar novamente? []sim []não")
                    resposta = input()
                    if resposta == "sim":
                        pontos_usuario = pontos_maquina = 0
                        aviso = escolha_usuario = escolha_maquina = ""
                    else:
                        jogo_andamento = False

                
                
            elif verificando_decisoes(valor_usuario, valor_maquina) == "máquina ganha":
                aviso = "máquina venceu"
                pontos_maquina = pontos_maquina + 1
                escolha_usuario = "você escolheu " + valor_usuario
                escolha_maquina = "máquina escolheu " + valor_maquina
                
                # fim da partida e oportunidade de jogar novamente
                if pontos_maquina == 10:
                    os.system('cls')
                    print("VOCÊ PERDEU A PARTIDA!")
                    time.sleep(3)
                    print("quer jogar novamente? []sim []não")
                    resposta = input()
                    if resposta == "sim":
                        pontos_usuario = pontos_maquina = 0
                        aviso = escolha_usuario = escolha_maquina = ""
                    else:
                        jogo_andamento = False

                
        

    elif resposta_inicial == 2:
        print("                   COMO JOGAR")
        print("para ser vitorioso, vc precisar ganhar 10 vezes na pedra, papel e tesoura")
        print("caso não aconteça, a máquina ganha\n")

        print("instruções para jogar:")
        print("- pedra ganha de tesoura")
        print("- papel ganha de pedra")
        print("- tesoura ganha de papel")
        input()
    elif resposta_inicial == 3:
        print("jogo fechado!")
        jogo = False
    else:
        print("esse comando nao existe!")
        time.sleep(3)


    