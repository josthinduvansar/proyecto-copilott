# Proyecto Copilot - Estructura de Datos: COLA (Queue)

Proyecto educativo sobre la estructura de datos **COLA (Queue)** - estructura FIFO (First In, First Out).

## 📋 Contenido del Proyecto

### 1. **queue.py** - Implementación de Colas
Contiene dos implementaciones:

#### Clase `Queue`
- Cola básica usando listas de Python
- Operaciones: `enqueue()`, `dequeue()`, `peek()`, `is_empty()`, `size()`, `display()`, `clear()`
- Ideal para aprender los conceptos básicos

#### Clase `CircularQueue`
- Cola circular con tamaño fijo
- Reutiliza espacio de memoria eficientemente
- Operaciones: `enqueue()`, `dequeue()`, `peek()`, `is_empty()`, `is_full()`, `size()`, `display()`

### 2. **ejemplos_cola.py** - Ejemplos de Uso
5 ejemplos prácticos:
1. **Ejemplo Básico**: Operaciones fundamentales de la cola
2. **Simulación de Banco**: Fila de atención a clientes
3. **Cola de Impresión**: Procesamiento de tareas en orden
4. **Cola Circular**: Uso de estructura circular
5. **Manejo de Errores**: Casos de error y excepciones

### 3. **test_cola.py** - Pruebas Unitarias
Suite completa de pruebas con `unittest`:
- 10 pruebas para `Queue`
- 9 pruebas para `CircularQueue`
- 1 prueba comparativa entre ambas

## 🚀 Cómo Ejecutar

### Ejecutar Ejemplos
```bash
python ejemplos_cola.py
```

### Ejecutar Pruebas
```bash
python test_cola.py
```

O con más verbosidad:
```bash
python test_cola.py -v
```

## 📚 Conceptos Clave

### ¿Qué es una Cola?
- Estructura de datos **FIFO** (First In, First Out)
- El primer elemento en entrar es el primero en salir
- Analogía: fila en un banco o caja de supermercado

### Operaciones Principales
| Operación | Complejidad | Descripción |
|-----------|------------|------------|
| `enqueue()` | O(1) | Añade elemento al final |
| `dequeue()` | O(1) | Elimina primer elemento |
| `peek()` | O(1) | Ve primer elemento sin eliminarlo |
| `is_empty()` | O(1) | Verifica si está vacía |
| `size()` | O(1) | Obtiene cantidad de elementos |

### Diferencias: Queue vs CircularQueue

| Aspecto | Queue | CircularQueue |
|--------|-------|---------------|
| Capacidad | Dinámica | Fija |
| Memoria | Flexible | Constante |
| Operación dequeue | O(n) con listas | O(1) |
| Caso de uso | Flexible | Tiempo real |

## 💡 Aplicaciones Reales

1. **Impresoras**: Cola de trabajos de impresión
2. **Sistemas Operativos**: Scheduling de procesos
3. **Redes**: Buffer de paquetes
4. **Servidores**: Solicitudes HTTP
5. **Videojuegos**: Sistema de eventos
6. **Bancos**: Gestión de filas de clientes
7. **Call Centers**: Sistema de atención al cliente

## 📖 Estructura del Código

```
proyecto-copilot/
├── queue.py              # Implementación de colas
├── ejemplos_cola.py      # 5 ejemplos prácticos
├── test_cola.py          # Pruebas unitarias (20 casos)
└── README.md             # Este archivo
```

## ✅ Checklist de Aprendizaje

- [ ] Entender qué es una cola (FIFO)
- [ ] Conocer las operaciones básicas (enqueue, dequeue, peek)
- [ ] Diferenciar entre Queue normal y CircularQueue
- [ ] Comprender las complejidades de tiempo
- [ ] Ejecutar los ejemplos
- [ ] Entender las pruebas unitarias
- [ ] Intentar crear tu propia aplicación usando colas

## 🔍 Casos de Prueba

Las pruebas cubren:
- ✅ Cola vacía
- ✅ Encolado simple y múltiple
- ✅ Desencolado en orden FIFO
- ✅ Operación peek sin modificar
- ✅ Errores en cola vacía
- ✅ Limpiar cola
- ✅ Operaciones alternadas
- ✅ Capacidad de cola circular
- ✅ Reutilización de espacio circular

## 📌 Notas Importantes

- Una cola **vacía** puede generar `IndexError` al intentar `dequeue()` o `peek()`
- Una `CircularQueue` puede generar `OverflowError` si está llena
- El orden de atención es **siempre** FIFO
- Una cola circular es más eficiente en memoria que una lista dinámica para casos con capacidad conocida

## 🎓 Autor
Proyecto educativo para Estructura de Datos

---

**¡Happy Learning!** 🎉
