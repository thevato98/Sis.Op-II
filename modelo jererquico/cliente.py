import socket

def consultar_nombre(nombre):
    servidor_raiz = ('localhost', 5000)  # Contacta al servidor raíz en localhost:5000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(servidor_raiz)
        s.sendall(nombre.encode())
        respuesta = s.recv(1024).decode()
        print(f"Respuesta recibida: {respuesta}")

if __name__ == '__main__':
    nombre = input("Introduce el nombre a resolver (ej. nodo1.empresa.com): ")
    consultar_nombre(nombre)

