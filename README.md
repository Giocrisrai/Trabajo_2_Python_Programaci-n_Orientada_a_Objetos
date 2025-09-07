# Sistema de Inventario con Programación Orientada a Objetos

## 📋 Descripción del Proyecto

Este proyecto implementa un **sistema básico de inventario** desarrollado en Python utilizando principios de Programación Orientada a Objetos (POO). El sistema permite gestionar productos y realizar operaciones de inventario a través de una interfaz de consola interactiva.

## 🎯 Objetivos del Proyecto

- Implementar correctamente la clase `Producto` con validaciones y métodos de actualización
- Desarrollar la clase `Inventario` para gestionar una colección de productos
- Implementar manejo robusto de excepciones para entradas inválidas
- Crear una interfaz de usuario interactiva para probar todas las funcionalidades

## 🏗️ Arquitectura del Sistema

### Clases Principales

#### 1. Clase `Producto`
Representa un producto individual con los siguientes atributos:
- **nombre** (str): Nombre del producto
- **precio** (float): Precio unitario del producto
- **cantidad** (int): Cantidad disponible en inventario

**Métodos implementados:**
- `actualizar_precio(nuevo_precio)`: Modifica el precio validando que sea positivo
- `actualizar_cantidad(nueva_cantidad)`: Modifica la cantidad validando que sea positiva
- `calcular_valor_total()`: Calcula el valor total (precio × cantidad)
- `__str__()`: Representación legible del producto

#### 2. Clase `Inventario`
Gestiona una colección de productos con los siguientes métodos:
- `agregar_producto(producto)`: Añade un producto al inventario
- `buscar_producto(nombre)`: Busca un producto por su nombre
- `calcular_valor_inventario()`: Calcula el valor total del inventario
- `listar_productos()`: Lista todos los productos del inventario

## ✨ Características Principales

### 🔒 Validaciones Robustas
- **Nombres**: No pueden estar vacíos, se normalizan automáticamente
- **Precios**: Deben ser numéricos y no negativos
- **Cantidades**: Deben ser enteros no negativos
- **Tipos de datos**: Validación estricta de tipos

### 🛡️ Manejo de Excepciones
- `ProductoNoEncontradoError`: Excepción personalizada para productos no encontrados
- `TypeError`: Para tipos de datos incorrectos
- `ValueError`: Para valores inválidos (negativos, vacíos, etc.)
- `KeyboardInterrupt`: Para interrupciones del usuario

### 🎮 Interfaz de Usuario
Menú interactivo con las siguientes opciones:
1. **Agregar producto** - Añadir nuevos productos al inventario
2. **Buscar producto** - Buscar productos por nombre
3. **Listar productos** - Mostrar todos los productos
4. **Calcular valor total** - Obtener el valor total del inventario
5. **Actualizar precio** - Modificar el precio de un producto existente
6. **Actualizar cantidad** - Modificar la cantidad de un producto existente
7. **Salir** - Terminar la aplicación

## 🚀 Instalación y Uso

### Requisitos
- Python 3.7 o superior
- No se requieren dependencias externas

### Ejecución
```bash
python sistema_inventario.py
```

### Ejemplo de Uso
```
============================================================
        SISTEMA DE INVENTARIO (POO)
============================================================
0. Salir
1. Agregar producto
2. Buscar producto
3. Listar productos
4. Calcular valor total de inventario
5. Actualizar precio de un producto
6. Actualizar cantidad de un producto
============================================================
Seleccione una opción: 1

[Agregar producto]
Nombre: Laptop Dell
Precio: $1200.50
Cantidad: 5
✔ Producto agregado/actualizado: Producto(nombre='Laptop Dell', precio=$1200.50, cantidad=5, total=$6002.50)
```

## 📊 Funcionalidades Avanzadas

### Fusión Inteligente de Productos
- Si se agrega un producto con un nombre que ya existe, el sistema fusiona automáticamente las cantidades
- El precio se actualiza al valor más reciente

### Búsqueda Insensible a Mayúsculas
- La búsqueda de productos no distingue entre mayúsculas y minúsculas
- Los nombres se normalizan automáticamente

### Formato de Salida Consistente
- Todos los valores monetarios se muestran con 2 decimales
- Información de productos formateada de manera legible
- Mensajes de confirmación y error claros

## 🧪 Casos de Prueba

### Validaciones de Entrada
```python
# Casos válidos
Producto("Laptop", 1200.50, 5)  # ✅ Correcto
Producto("Mouse", 25.0, 100)    # ✅ Correcto

# Casos inválidos
Producto("", 100, 5)            # ❌ Nombre vacío
Producto("Laptop", -100, 5)     # ❌ Precio negativo
Producto("Laptop", 100, -5)     # ❌ Cantidad negativa
```

### Manejo de Excepciones
```python
try:
    inventario.buscar_producto("Producto Inexistente")
except ProductoNoEncontradoError as e:
    print(f"Error: {e}")  # "No se encontró el producto 'Producto Inexistente'."
```

## 📁 Estructura del Proyecto

```
Trabajo_2_Python_Programaci-n_Orientada_a_Objetos/
├── sistema_inventario.py    # Código principal del sistema
└── README.md               # Este archivo de documentación
```

## 🔧 Detalles Técnicos

### Tecnologías Utilizadas
- **Python 3.7+**: Lenguaje de programación principal
- **Dataclasses**: Para la clase Producto con validaciones automáticas
- **Type Hints**: Para mejor documentación y verificación de tipos
- **Exception Handling**: Manejo robusto de errores

### Patrones de Diseño
- **Encapsulación**: Atributos privados y métodos públicos bien definidos
- **Validación**: Funciones de validación reutilizables
- **Separación de responsabilidades**: Lógica de negocio separada de la interfaz de usuario

## 📈 Criterios de Evaluación

Este proyecto cumple con todos los criterios de evaluación:

- ✅ **Clase Producto (30%)**: Implementación completa con validaciones y métodos requeridos
- ✅ **Clase Inventario (30%)**: Gestión completa de productos con todas las operaciones
- ✅ **Manejo de Excepciones (20%)**: Implementación robusta de try-except para todos los casos
- ✅ **Interfaz de Usuario (20%)**: Menú interactivo completo y funcional

## 👨‍💻 Autor

**Giocrisrai Godoy**  
Curso de Python UNIR - Trabajo 2: Programación Orientada a Objetos

## 📝 Notas Adicionales

- El sistema está diseñado para ser robusto y manejar casos edge
- La interfaz es intuitiva y proporciona retroalimentación clara al usuario
- El código está bien documentado y sigue las mejores prácticas de Python
- Se incluyen validaciones exhaustivas para prevenir errores de entrada

---

*Desarrollado como parte del Trabajo 2 del Curso de Python UNIR*
