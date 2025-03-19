# Nombre del estudiante: Luis Navarro Masson
# Grupo: 81
# Número y Texto del problema: Problema 1 - Serie de Fibonacci
# Código Fuente: autoría propia

# Solicitar al usuario un número entero positivo mayor que 1
while True:
    try:
        n = int(input("Ingrese la cantidad de elementos de la serie de Fibonacci a mostrar (mayor que 1): "))
        if n > 1:
            break
        else:
            print("Por favor, ingrese un número mayor que 1.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero positivo.")

# Inicializar los primeros dos números de Fibonacci
a, b = 0, 1

# Mostrar la serie de Fibonacci
print(f"Los primeros {n} números de la serie de Fibonacci son:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

print()  # Salto de línea final
