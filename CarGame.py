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
