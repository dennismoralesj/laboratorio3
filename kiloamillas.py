def convertir_millas(kilometros):
    millas_en_kilo = 0.621371
    return kilometros * millas_en_kilo

try:
    print("Bienvenido a la conversion de Km a Millas")
    kilometro = input("Ingrese la cantidad de Kilometros a convertir a Millas: ")
    kilometro = float(kilometro)
    millas = convertir_millas(kilometro)
    resultado ="{:.3f}".format(millas)
    print("Los kilómetros dados son aproximadamente:", resultado)
except ValueError:
    print("Error de Conversión: Ingresa una cantidad válida de kilómetros en número. Intenta nuevamente.")