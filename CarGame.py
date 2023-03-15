# CRIANDO A BASE (1)
# MODO DE ESCREVER UM TIPO DE COMANDO
command = ""
while command.lower() != "quit":
    command = input("> ") #input introduz um comando
    if command.lower() == "start":
        print("Car started...")
    elif command.lower() == "stop":
        print("Car stopped.")
# ESSA PARTE PODE SER REESCRITA COMO:
command = ""
while command != "quit":
    command = input("> ").lower()
    if command == "start":
        print("Car started...")
    elif command == "stop":
        print("Car stopped.")
 --
# 'CAR GAME' (2)
command = ""
while command != "quit": # POSSO SIMPLIFICAR/'TIRAR' ESSE COMANDO, POIS REPETI,POSOS POR 'while True:'
    command = input("> ").lower()
    if command == "start":
        print("Car started...")
    elif command == "stop":
        print("Car stopped.")
    elif command == "help":
        print("""  
start - to start the car 
stop - to stop the car
quit - to quit
        """)
    elif command == "quit": # COMANDO REPETIDO/ COM ESSE COMANDO PODEMOS PULAR FORA DO LOOP E TERMINAR O PROGRAMA
        break
    else:
        print("Sorry, I don't understand that")
--
# SIMPLIFICAÇÃO (3)
# SEM A REPETIÇÃO e simmplificando FICARIA:
command = ""
while True: # Esse comando simplificado diz o mesmo do que o anterior: o comando ficará seguindo em loop até ser explicitamente quebrado 'break'
    command = input("> ").lower()
    if command == "start":
        print("Car started...")
    elif command == "stop":
        print("Car stopped.")
    elif command == "help":
        print("""  
start - to start the car 
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that")
 --
# AJUSTES FINAIS (4)
# O incremento dessa boolean detalhará melhor se o carro já deu start ou se já deu stop, sem mensagens repetidas "poder startar ou dar stop mais de uma vez"
# Nosso FULL 'car game' fica assim:
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started: # Tradução: "se o carro está parado.."
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""  
start - to start the car 
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that")
 # FIM
