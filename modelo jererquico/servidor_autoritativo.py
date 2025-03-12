import socket 

# Base de datos de nombres y direcciones IP
nombres_db = {
    'nodo1.empresa.com': '192.168.1.200',
    'nodo2.empresa.com': '192.168.1.201'
}

def servidor_autoritativo():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 5002))
        s.listen()
        print("Servidor autoritativo empresa.com escuchando en localhost:5002")

        while True:
            conn, addr = s.accept()
            with conn:
                nombre = conn.recv(1024).decode()
                print(f"Consulta recibida en servidor autoritativo: {nombre}")

                respuesta = nombres_db.get(nombre, "Nombre no encontrado")
                conn.sendall(respuesta.encode())

if __name__ == '__main__':
    servidor_autoritativo()
