def actividad_1():
    print("\nEjercicio 1")

    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))

    mayor = numero1 if numero1 > numero2 else numero2

    print(f"El mayor es: {mayor}")


def buscar_palabra(palabra, *lista):
    return "La palabra fue encontrada." if palabra in lista else "La palabra no fue encontrada."


def actividad_2():
    print("\nEjercicio 2")

    palabra = input("Ingrese la palabra a buscar: ")
    cantidad = int(input("¿Cuántas palabras quiere ingresar?: "))

    lista = []

    for i in range(cantidad):
        palabra_lista = input(f"Ingrese la palabra {i + 1}: ")
        lista.append(palabra_lista)

    print(buscar_palabra(palabra, *lista))


def actividad_3():
    print("\nEjercicio 3")

    numero = int(input("Ingrese un número: "))

    resultado = "El número es par." if numero % 2 == 0 else "El número es impar."

    print(resultado)


def calcular_promedio(*numeros):
    return sum(numeros) / len(numeros) if len(numeros) > 0 else 0


def actividad_4():
    print("\nEjercicio 4")

    cantidad = int(input("¿Cuántos números quiere ingresar?: "))

    numeros = []

    for i in range(cantidad):
        numero = float(input(f"Ingrese el número {i + 1}: "))
        numeros.append(numero)

    promedio = calcular_promedio(*numeros)

    print(f"El promedio es: {promedio}")


def verificar_argumentos(*args):
    if len(args) < 2:
        print("Error: no se pasaron suficientes argumentos.")
    else:
        print("Se pasaron suficientes argumentos.")


def actividad_5():
    print("\nEjercicio 5")

    argumentos = input("Ingrese argumentos separados por espacios: ").split()

    verificar_argumentos(*argumentos)


def mostrar_menu():
    print("\n===== PRÁCTICA =====")
    print("1 - Calcular el mayor de dos números")
    print("2 - Buscar una palabra en una lista")
    print("3 - Determinar si un número es par o impar")
    print("4 - Calcular el promedio de una lista")
    print("5 - Verificar cantidad de argumentos")
    print("0 - Salir")


def main():
    actividades = {
        "1": actividad_1,
        "2": actividad_2,
        "3": actividad_3,
        "4": actividad_4,
        "5": actividad_5
    }

    while True:
        mostrar_menu()

        opcion = input("Seleccione una actividad: ")

        if opcion == "0":
            print("Programa finalizado.")
            break

        elif opcion in actividades:
            actividades[opcion]()

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()