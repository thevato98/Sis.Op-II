import socket

# Diccionario con los servidores TLD conocidos (solo "com" en este caso)
servidores_tld = {
    'com': ('192.168.236.129', 5001)  # El TLD .com está en localhost puerto 5001
}

def servidor_raiz():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('192.168.236.182', 5000))
        s.listen()
        print("Servidor raíz escuchando en 192.168.236.182:5000")

        while True:
            conn, addr = s.accept()
            with conn:
                nombre = conn.recv(1024).decode()
                print(f"Consulta recibida: {nombre}")

                tld = nombre.split('.')[-1]

                if tld in servidores_tld:
                    tld_host, tld_port = servidores_tld[tld]
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tld_sock:
                        tld_sock.connect((tld_host, tld_port))
                        tld_sock.sendall(nombre.encode())
                        respuesta = tld_sock.recv(1024).decode()
                else:
                    respuesta = "Dominio TLD no encontrado"

                conn.sendall(respuesta.encode())

if __name__ == '__main__':
    servidor_raiz()
