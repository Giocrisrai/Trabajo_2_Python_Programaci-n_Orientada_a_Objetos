#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sistema_inventario.py
Sistema básico de Inventario con Programación Orientada a Objetos en Python.

Características:
- Clase Producto con validaciones y métodos de actualización.
- Clase Inventario para gestionar la colección de productos.
- Manejo de excepciones (valores negativos, tipos incorrectos, producto no encontrado).
- Menú interactivo por consola para probar funcionalidades.

Ejecutar:
    python sistema_inventario.py
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional


class ProductoNoEncontradoError(LookupError):
    """Se lanza cuando no se encuentra un producto por su nombre."""
    pass


def _validar_nombre(nombre: str) -> str:
    if not isinstance(nombre, str):
        raise TypeError("El nombre debe ser de tipo str.")
    nombre_limpio = nombre.strip()
    if not nombre_limpio:
        raise ValueError("El nombre no puede estar vacío.")
    return nombre_limpio


def _validar_precio(precio: float) -> float:
    if not isinstance(precio, (int, float)):
        raise TypeError("El precio debe ser numérico (int o float).")
    precio = float(precio)
    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")
    return round(precio, 2)


def _validar_cantidad(cantidad: int) -> int:
    if not isinstance(cantidad, int):
        raise TypeError("La cantidad debe ser un entero (int).")
    if cantidad < 0:
        raise ValueError("La cantidad no puede ser negativa.")
    return cantidad


@dataclass
class Producto:
    nombre: str
    precio: float
    cantidad: int

    def __post_init__(self):
        self.nombre = _validar_nombre(self.nombre)
        self.precio = _validar_precio(self.precio)
        self.cantidad = _validar_cantidad(self.cantidad)

    # Métodos del enunciado
    def actualizar_precio(self, nuevo_precio: float) -> None:
        self.precio = _validar_precio(nuevo_precio)

    def actualizar_cantidad(self, nueva_cantidad: int) -> None:
        self.cantidad = _validar_cantidad(nueva_cantidad)

    def calcular_valor_total(self) -> float:
        return round(self.precio * self.cantidad, 2)

    def __str__(self) -> str:
        return (f"Producto(nombre='{self.nombre}', "
                f"precio=${self.precio:.2f}, "
                f"cantidad={self.cantidad}, "
                f"total=${self.calcular_valor_total():.2f})")


class Inventario:
    def __init__(self) -> None:
        self._productos: List[Producto] = []

    # Utilidad interna para normalizar nombres
    @staticmethod
    def _clave(nombre: str) -> str:
        return _validar_nombre(nombre).lower()

    def agregar_producto(self, producto: Producto) -> None:
        """Agrega un producto. Si ya existe por nombre (insensible a mayúsculas),
        combina cantidades y actualiza el precio al más reciente.
        """
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden agregar instancias de Producto.")
        clave = self._clave(producto.nombre)
        existente = self._buscar_por_clave(clave)
        if existente:
            # Política: fusionar cantidades y actualizar precio al nuevo.
            nueva_cantidad = existente.cantidad + producto.cantidad
            existente.actualizar_precio(producto.precio)
            existente.actualizar_cantidad(nueva_cantidad)
        else:
            self._productos.append(producto)

    def _buscar_por_clave(self, clave: str) -> Optional[Producto]:
        for p in self._productos:
            if self._clave(p.nombre) == clave:
                return p
        return None

    def buscar_producto(self, nombre: str) -> Producto:
        prod = self._buscar_por_clave(self._clave(nombre))
        if not prod:
            raise ProductoNoEncontradoError(f"No se encontró el producto '{nombre}'.")
        return prod

    def calcular_valor_inventario(self) -> float:
        return round(sum(p.calcular_valor_total() for p in self._productos), 2)

    def listar_productos(self) -> List[Producto]:
        return list(self._productos)


# ------------------------- Interfaz de Usuario (CLI) -------------------------

def _input_float(msg: str) -> float:
    valor = input(msg).strip()
    try:
        return _validar_precio(float(valor))
    except Exception as e:
        raise ValueError(f"Entrada inválida para precio: {e}")


def _input_int_no_negativo(msg: str) -> int:
    valor = input(msg).strip()
    if not valor.isdigit():
        # Permite "0" y números positivos
        raise ValueError("Debe ingresar un entero mayor o igual a 0.")
    return _validar_cantidad(int(valor))


def _input_nombre(msg: str) -> str:
    return _validar_nombre(input(msg))


def menu_principal() -> None:
    inventario = Inventario()

    opciones = {
        "1": "Agregar producto",
        "2": "Buscar producto",
        "3": "Listar productos",
        "4": "Calcular valor total de inventario",
        "5": "Actualizar precio de un producto",
        "6": "Actualizar cantidad de un producto",
        "0": "Salir",
    }

    def mostrar_menu():
        print("\n" + "=" * 60)
        print("        SISTEMA DE INVENTARIO (POO)")
        print("=" * 60)
        for k in sorted(opciones.keys()):
            print(f"{k}. {opciones[k]}")
        print("=" * 60)

    while True:
        try:
            mostrar_menu()
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "0":
                print("Saliendo del sistema. ¡Hasta luego!")
                break

            elif opcion == "1":
                print("\n[Agregar producto]")
                nombre = _input_nombre("Nombre: ")
                precio = _input_float("Precio: $")
                cantidad = _input_int_no_negativo("Cantidad: ")
                producto = Producto(nombre=nombre, precio=precio, cantidad=cantidad)
                inventario.agregar_producto(producto)
                print(f"✔ Producto agregado/actualizado: {producto}")

            elif opcion == "2":
                print("\n[Buscar producto]")
                nombre = _input_nombre("Nombre a buscar: ")
                prod = inventario.buscar_producto(nombre)
                print(f"✔ Encontrado: {prod}")

            elif opcion == "3":
                print("\n[Listar productos]")
                productos = inventario.listar_productos()
                if not productos:
                    print("Inventario vacío.")
                else:
                    print("-" * 60)
                    for p in productos:
                        print(p)
                    print("-" * 60)

            elif opcion == "4":
                total = inventario.calcular_valor_inventario()
                print(f"\n✔ Valor total del inventario: ${total:.2f}")

            elif opcion == "5":
                print("\n[Actualizar precio]")
                nombre = _input_nombre("Nombre del producto: ")
                nuevo_precio = _input_float("Nuevo precio: $")
                prod = inventario.buscar_producto(nombre)
                prod.actualizar_precio(nuevo_precio)
                print(f"✔ Precio actualizado: {prod}")

            elif opcion == "6":
                print("\n[Actualizar cantidad]")
                nombre = _input_nombre("Nombre del producto: ")
                nueva_cantidad = _input_int_no_negativo("Nueva cantidad: ")
                prod = inventario.buscar_producto(nombre)
                prod.actualizar_cantidad(nueva_cantidad)
                print(f"✔ Cantidad actualizada: {prod}")

            else:
                print("Opción no válida. Intente nuevamente.")

        except ProductoNoEncontradoError as e:
            print(f"✖ Error: {e}")
        except (TypeError, ValueError) as e:
            print(f"✖ Entrada inválida: {e}")
        except KeyboardInterrupt:
            print("\nInterrumpido por el usuario. Saliendo...")
            break
        except Exception as e:
            print(f"✖ Error inesperado: {e}")


if __name__ == "__main__":
    menu_principal()
