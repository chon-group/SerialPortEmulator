import javino 
import time 
import random 
import string

porta = "/dev/ttyExogenous0" 
comm = javino.start(porta)

if comm:
    try:
        while True:
            if javino.availableMsg(comm):
                mensagem = javino.getMsg()
                if mensagem != None:
                    print(f"received: {mensagem}")
                    javino.sendMsg(comm,mensagem)
                else:
                    print(f".", end=" ", flush=True)
    except KeyboardInterrupt:
        javino.disconnect(comm)
else:
    print("Não foi possível conectar à porta serial.")
