import socket

# Diccionario con los servidores autoritativos conocidos
servidores_autoritativos = {
    'empresa.com': ('localhost', 5002)  # empresa.com lo maneja el servidor autoritativo en puerto 5002
}

def servidor_tld():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 5001))
        s.listen()
        print("Servidor TLD .com escuchando en localhost:5001")

        while True:
            conn, addr = s.accept()
            with conn:
                nombre = conn.recv(1024).decode()
                print(f"Consulta recibida en TLD: {nombre}")

                dominio = '.'.join(nombre.split('.')[-2:])

                if dominio in servidores_autoritativos:
                    auth_host, auth_port = servidores_autoritativos[dominio]
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as auth_sock:
                        auth_sock.connect((auth_host, auth_port))
                        auth_sock.sendall(nombre.encode())
                        respuesta = auth_sock.recv(1024).decode()
                else:
                    respuesta = "Dominio autoritativo no encontrado"

                conn.sendall(respuesta.encode())

if __name__ == '__main__':
    servidor_tld()
