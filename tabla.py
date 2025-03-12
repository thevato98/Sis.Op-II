import hashlib

# -------------------------------
# Clase NodoDHT
# -------------------------------
class NodoDHT:
    def __init__(self, id, rango_inicio, rango_fin):  # CORRECTO
        self.id = id
        self.rango_inicio = rango_inicio
        self.rango_fin = rango_fin
        self.tabla = {}  # Almacenamiento local de clave-valor
        self.vecinos = []  # Otros nodos en la red
        self.activo = True  # Simulación de nodo activo o caído
        self.log = []  # Registro de actividad
    
    def agregar_vecino(self, vecino):
        self.vecinos.append(vecino)

    def calcular_hash(self, clave):
        # Calcula un hash entre 0 y 99 usando SHA-1
        return int(hashlib.sha1(clave.encode()).hexdigest(), 16) % 100

    def pertenece_a_nodo(self, clave):
        hash_clave = self.calcular_hash(clave)
        return self.rango_inicio <= hash_clave <= self.rango_fin

    def almacenar(self, clave, valor):
        if not self.activo:
            self.log_evento(f"Nodo {self.id} está caído. No puede almacenar {clave}.")
            return
            
        hash_clave = self.calcular_hash(clave)
        if self.pertenece_a_nodo(clave):
            self.tabla[clave] = valor
            self.log_evento(f"Almacenado {clave} -> {valor}")
        else:
            reenviado = False
            for vecino in self.vecinos:
                if vecino.activo and vecino.pertenece_a_nodo(clave):
                    self.log_evento(f"Reenviando {clave} a Nodo {vecino.id}")
                    vecino.almacenar(clave, valor)
                    reenviado = True
                    break
            if not reenviado:
                self.log_evento(f"No se encontró un vecino activo para almacenar {clave}")

    def buscar(self, clave):
        if not self.activo:
            self.log_evento(f"Nodo {self.id} está caído. No puede buscar {clave}.")
            return None
        
        if clave in self.tabla:
            self.log_evento(f"Clave {clave} encontrada en Nodo {self.id}")
            return self.tabla[clave]
        else:
            for vecino in self.vecinos:
                if vecino.activo and vecino.pertenece_a_nodo(clave):
                    self.log_evento(f"Consultando a vecino Nodo {vecino.id} por clave {clave}")
                    return vecino.buscar(clave)
            self.log_evento(f"Clave {clave} no encontrada en Nodo {self.id} ni vecinos")
            return None

    def simular_caida(self):
        self.activo = False
        self.log_evento(f"Nodo {self.id} simulado como caído.")

    def reactivar(self):
        self.activo = True
        self.log_evento(f"Nodo {self.id} reactivado.")

    def log_evento(self, mensaje):
        self.log.append(mensaje)
        print(f"[Nodo {self.id}] {mensaje}")

    def imprimir_log(self):
        print(f"\nLog de Nodo {self.id}:")
        for evento in self.log:
            print(f"  {evento}")

# -------------------------------
# Configuración y simulación
# -------------------------------

# Crear 3 nodos iniciales
nodo1 = NodoDHT(1, 0, 33)
nodo2 = NodoDHT(2, 34, 66)
nodo3 = NodoDHT(3, 67, 99)

# Conectar vecinos
nodo1.agregar_vecino(nodo2)
nodo1.agregar_vecino(nodo3)
nodo2.agregar_vecino(nodo1)
nodo2.agregar_vecino(nodo3)
nodo3.agregar_vecino(nodo1)
nodo3.agregar_vecino(nodo2)

# Almacenar claves
nodo1.almacenar("servidor1", "192.168.1.10")
nodo1.almacenar("servidor2", "192.168.1.20")
nodo1.almacenar("servidor3", "192.168.1.30")

# Simular caída de Nodo 2
print("\nSimulando caída de Nodo 2...")
nodo2.simular_caida()

# Consultas después de la caída
print("\nConsultas tras la caída de Nodo 2:")
print(f"Buscar servidor1: {nodo1.buscar('servidor1')}")
print(f"Buscar servidor2: {nodo1.buscar('servidor2')}")
print(f"Buscar servidor3: {nodo1.buscar('servidor3')}")
print(f"Buscar servidor4 (inexistente): {nodo1.buscar('servidor4')}")

# Añadir un nuevo nodo dinámicamente (Nodo 4)
print("\nAñadiendo Nodo 4 con rango 34-49...")
nodo4 = NodoDHT(4, 34, 49)
nodo4.agregar_vecino(nodo1)
nodo4.agregar_vecino(nodo3)

nodo1.agregar_vecino(nodo4)
nodo3.agregar_vecino(nodo4)

# Almacenar clave en Nodo 4
nodo4.almacenar("servidor4", "192.168.1.40")

# Reactivar Nodo 2
print("\nReactivando Nodo 2...")
nodo2.reactivar()

# Consultas finales
print("\nConsultas finales:")
print(f"Buscar servidor4: {nodo1.buscar('servidor4')}")
print(f"Buscar servidor1: {nodo1.buscar('servidor1')}")

# Mostrar logs de todos los nodos
nodo1.imprimir_log()
nodo2.imprimir_log()
nodo3.imprimir_log()
nodo4.imprimir_log()