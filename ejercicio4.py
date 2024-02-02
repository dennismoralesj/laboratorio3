def suma_es_par(n1, n2):
    suma = n1 + n2
    return suma % 2 == 0

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))

resultado = suma_es_par(n1, n2)
print(f"La suma de {n1} y {n2} es par: {resultado}")