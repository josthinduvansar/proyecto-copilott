"""
IMPLEMENTACIONES DE TABLAS HASH EN PYTHON
==========================================

Este archivo contiene implementaciones prácticas de tablas hash
con Chaining y Open Addressing, para complementar el blog educativo.
"""

# ============================================================
# 1. TABLA HASH CON CHAINING (Encadenamiento)
# ============================================================

class NodoLista:
    """Nodo para la lista enlazada en Chaining"""
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.siguiente = None


class TablaHashChaining:
    """
    Implementación de Tabla Hash usando Encadenamiento (Chaining)
    
    Características:
    - Cada posición contiene una lista enlazada
    - Maneja colisiones fácilmente
    - Puede crecer dinámicamente
    """
    
    def __init__(self, tamaño=10):
        """Inicializar la tabla hash con un tamaño dado"""
        self.tamaño = tamaño
        self.tabla = [None] * tamaño
        self.cantidad = 0
    
    def _hash(self, clave):
        """
        Función hash simple: usa ord() para convertir caracteres a números
        y aplica módulo para obtener índice
        """
        suma = sum(ord(c) for c in str(clave))
        return suma % self.tamaño
    
    def poner(self, clave, valor):
        """
        Insertar un par clave-valor en la tabla hash
        
        Pasos:
        1. Calcular hash(clave)
        2. Obtener índice
        3. Insertar en la lista enlazada
        """
        índice = self._hash(clave)
        
        # Si no hay lista en este índice, crearla
        if self.tabla[índice] is None:
            self.tabla[índice] = NodoLista(clave, valor)
            self.cantidad += 1
        else:
            # Verificar si la clave ya existe
            nodo_actual = self.tabla[índice]
            while nodo_actual:
                if nodo_actual.clave == clave:
                    # Actualizar valor existente
                    nodo_actual.valor = valor
                    return
                if nodo_actual.siguiente is None:
                    break
                nodo_actual = nodo_actual.siguiente
            
            # Agregar al final de la lista
            nodo_actual.siguiente = NodoLista(clave, valor)
            self.cantidad += 1
    
    def obtener(self, clave):
        """
        Buscar y recuperar el valor asociado a una clave
        
        Pasos:
        1. Calcular hash(clave)
        2. Buscar en la lista enlazada
        3. Retornar valor o None
        """
        índice = self._hash(clave)
        
        nodo = self.tabla[índice]
        while nodo:
            if nodo.clave == clave:
                return nodo.valor
            nodo = nodo.siguiente
        
        return None
    
    def eliminar(self, clave):
        """
        Eliminar un par clave-valor de la tabla hash
        
        Pasos:
        1. Calcular hash(clave)
        2. Buscar el nodo en la lista
        3. Eliminar ajustando punteros
        """
        índice = self._hash(clave)
        nodo = self.tabla[índice]
        nodo_anterior = None
        
        while nodo:
            if nodo.clave == clave:
                if nodo_anterior is None:
                    # Es el primer nodo
                    self.tabla[índice] = nodo.siguiente
                else:
                    # Está en medio o final
                    nodo_anterior.siguiente = nodo.siguiente
                self.cantidad -= 1
                return True
            nodo_anterior = nodo
            nodo = nodo.siguiente
        
        return False
    
    def factor_carga(self):
        """Calcular el factor de carga (elementos / tamaño)"""
        return self.cantidad / self.tamaño
    
    def mostrar(self):
        """Mostrar el contenido de la tabla hash"""
        print(f"\n{'='*50}")
        print("TABLA HASH CON CHAINING")
        print(f"{'='*50}")
        print(f"Tamaño: {self.tamaño}")
        print(f"Cantidad de elementos: {self.cantidad}")
        print(f"Factor de carga: {self.factor_carga():.2f}")
        print(f"{'-'*50}")
        
        for i, nodo in enumerate(self.tabla):
            elementos = []
            nodo_actual = nodo
            while nodo_actual:
                elementos.append(f"{nodo_actual.clave}:{nodo_actual.valor}")
                nodo_actual = nodo_actual.siguiente
            
            if elementos:
                print(f"[{i}] -> {' -> '.join(elementos)}")
            else:
                print(f"[{i}] -> vacío")


# ============================================================
# 2. TABLA HASH CON OPEN ADDRESSING (Linear Probing)
# ============================================================

class TablaHashOpenAddressing:
    """
    Implementación de Tabla Hash usando Direccionamiento Abierto
    con Linear Probing
    
    Características:
    - Todo se almacena en un arreglo
    - Si hay colisión, busca la siguiente posición
    - Más eficiente en memoria que Chaining
    """
    
    def __init__(self, tamaño=10):
        """Inicializar la tabla hash"""
        self.tamaño = tamaño
        self.tabla = [None] * tamaño  # None = vacío, "DELETED" = eliminado
        self.cantidad = 0
    
    def _hash(self, clave):
        """Función hash"""
        suma = sum(ord(c) for c in str(clave))
        return suma % self.tamaño
    
    def _buscar_posicion(self, clave, insertar=False):
        """
        Buscar posición para una clave usando Linear Probing
        
        Pasos:
        1. Calcular hash inicial
        2. Si está ocupado, probar siguiente posición
        3. Continuar hasta encontrar vacío o clave
        """
        índice = self._hash(clave)
        intentos = 0
        posición_delete = None
        
        while intentos < self.tamaño:
            # Verificar si la posición es None (vacía)
            if self.tabla[índice] is None:
                # Si buscamos para insertar y encontramos DELETED, guardar posición
                if insertar and posición_delete is not None:
                    return posición_delete
                return índice if insertar else None
            
            # Verificar si la posición contiene "DELETED"
            if isinstance(self.tabla[índice], str) and self.tabla[índice] == "DELETED":
                if posición_delete is None:
                    posición_delete = índice
                índice = (índice + 1) % self.tamaño
                intentos += 1
                continue
            
            # Verificar si la clave coincide
            if self.tabla[índice][0] == clave:
                return índice
            
            # Linear Probing: avanzar a la siguiente posición
            índice = (índice + 1) % self.tamaño
            intentos += 1
        
        # Si llegamos aquí y hay posición DELETED guardada, retornarla
        if insertar and posición_delete is not None:
            return posición_delete
        
        return None
    
    def poner(self, clave, valor):
        """Insertar un par clave-valor"""
        posición = self._buscar_posicion(clave, insertar=True)
        
        if posición is None:
            print(f"⚠️ Tabla llena, no se puede insertar {clave}")
            return False
        
        if self.tabla[posición] is None or (isinstance(self.tabla[posición], str)):
            self.cantidad += 1
        
        self.tabla[posición] = (clave, valor)
        return True
    
    def obtener(self, clave):
        """Obtener valor asociado a una clave"""
        posición = self._buscar_posicion(clave)
        
        if posición is not None and self.tabla[posición] is not None:
            return self.tabla[posición][1]
        
        return None
    
    def eliminar(self, clave):
        """Eliminar un par clave-valor (marcar como DELETED)"""
        posición = self._buscar_posicion(clave)
        
        if posición is not None and self.tabla[posición] is not None:
            self.tabla[posición] = "DELETED"
            self.cantidad -= 1
            return True
        
        return False
    
    def factor_carga(self):
        """Calcular factor de carga"""
        return self.cantidad / self.tamaño
    
    def mostrar(self):
        """Mostrar contenido de la tabla"""
        print(f"\n{'='*50}")
        print("TABLA HASH CON OPEN ADDRESSING (Linear Probing)")
        print(f"{'='*50}")
        print(f"Tamaño: {self.tamaño}")
        print(f"Cantidad de elementos: {self.cantidad}")
        print(f"Factor de carga: {self.factor_carga():.2f}")
        print(f"{'-'*50}")
        
        for i, elemento in enumerate(self.tabla):
            if elemento is None:
                print(f"[{i}] -> vacío")
            elif elemento == "DELETED":
                print(f"[{i}] -> DELETED (fue eliminado)")
            else:
                print(f"[{i}] -> {elemento[0]}: {elemento[1]}")


# ============================================================
# 3. EJEMPLOS DE USO
# ============================================================

def ejemplo_chaining():
    """Ejemplo de uso con Chaining"""
    print("\n" + "="*60)
    print("EJEMPLO 1: TABLA HASH CON CHAINING")
    print("="*60)
    
    tabla = TablaHashChaining(tamaño=5)
    
    # Insertar datos
    print("\n📍 Insertando datos...")
    datos = [
        ("Juan", 123),
        ("María", 456),
        ("Carlos", 789),
        ("Ana", 101112),
        ("Pedro", 131415),
        ("Eva", 161718),  # Esto causará colisión
    ]
    
    for clave, valor in datos:
        tabla.poner(clave, valor)
        print(f"✅ Insertado: {clave} -> {valor}")
    
    tabla.mostrar()
    
    # Buscar datos
    print("\n🔍 Buscando datos...")
    for clave in ["Juan", "Eva", "NoExiste"]:
        valor = tabla.obtener(clave)
        print(f"obtener('{clave}') = {valor}")
    
    # Eliminar datos
    print("\n🗑️ Eliminando datos...")
    tabla.eliminar("Maria")
    tabla.mostrar()


def ejemplo_open_addressing():
    """Ejemplo de uso con Open Addressing"""
    print("\n" + "="*60)
    print("EJEMPLO 2: TABLA HASH CON OPEN ADDRESSING")
    print("="*60)
    
    tabla = TablaHashOpenAddressing(tamaño=7)
    
    # Insertar datos
    print("\n📍 Insertando datos...")
    datos = [
        ("Juan", 100),
        ("María", 200),
        ("Carlos", 300),
        ("Ana", 400),
        ("Pedro", 500),
    ]
    
    for clave, valor in datos:
        tabla.poner(clave, valor)
        print(f"✅ Insertado: {clave} -> {valor}")
    
    tabla.mostrar()
    
    # Buscar datos
    print("\n🔍 Buscando datos...")
    for clave in ["Juan", "Ana", "NoExiste"]:
        valor = tabla.obtener(clave)
        print(f"obtener('{clave}') = {valor}")
    
    # Eliminar datos
    print("\n🗑️ Eliminando datos...")
    tabla.eliminar("María")
    tabla.mostrar()


def comparacion():
    """Comparar ambas implementaciones"""
    print("\n" + "="*60)
    print("COMPARACIÓN: CHAINING vs OPEN ADDRESSING")
    print("="*60)
    
    datos = [("A", 1), ("B", 2), ("C", 3), ("D", 4), ("E", 5)]
    
    # Chaining
    print("\n1. CON CHAINING:")
    tabla1 = TablaHashChaining(tamaño=3)
    for clave, valor in datos:
        tabla1.poner(clave, valor)
    tabla1.mostrar()
    print(f"\nFactor de carga: {tabla1.factor_carga():.2f}")
    
    # Open Addressing
    print("\n2. CON OPEN ADDRESSING:")
    tabla2 = TablaHashOpenAddressing(tamaño=7)
    for clave, valor in datos:
        tabla2.poner(clave, valor)
    tabla2.mostrar()
    print(f"\nFactor de carga: {tabla2.factor_carga():.2f}")


# ============================================================
# 4. EJECUCIÓN
# ============================================================

if __name__ == "__main__":
    print("""
╔════════════════════════════════════════════════════════════╗
║   IMPLEMENTACIONES DE TABLAS HASH EN PYTHON                ║
║   Blog Educativo: Estructuras de Datos                     ║
╚════════════════════════════════════════════════════════════╝
    """)
    
    # Ejecutar ejemplos
    ejemplo_chaining()
    ejemplo_open_addressing()
    comparacion()
    
    print("\n" + "="*60)
    print("✅ EJEMPLOS COMPLETADOS")
    print("="*60)
    print("\n💡 Conceptos demostrados:")
    print("   ✔ Inserción (PUT) en ambas estrategias")
    print("   ✔ Búsqueda (GET) en ambas estrategias")
    print("   ✔ Eliminación (DELETE) en ambas estrategias")
    print("   ✔ Manejo de colisiones")
    print("   ✔ Factor de carga")
    print("   ✔ Complejidad O(1) en promedio")
    print("\n" + "="*60 + "\n")
