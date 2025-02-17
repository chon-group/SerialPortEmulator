import javino 
import time 
import random 
import string

sizeOfMsg = 8
porta = "/dev/ttyEmulatedPort0"  
comm = javino.start(porta)


def random_message(sm):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=sm))

if comm:
    try:
        while True:
            message = random_message(sizeOfMsg)
            javino.clearChannel(comm)
            javino.sendMsg(comm,message) 
            print(f"sent: {message}", flush=True)
            attemp = 500
            while attemp > 0:
                #print(".", end =" ", flush=True)
                attemp = attemp -1
                if javino.availableMsg(comm):
                    received = javino.getMsg()
                    if received == message:
                        attemp = 0
                        print(f"received: {received}", flush=True)
                    elif received != None:
                        print(f"late: {received}", end =" ", flush=True)
                        javino.clearChannel(comm)
            print("")  
            time.sleep(1)          
    except KeyboardInterrupt:
        javino.disconnect(comm)
else:
    print("Não foi possível conectar à porta serial.")
