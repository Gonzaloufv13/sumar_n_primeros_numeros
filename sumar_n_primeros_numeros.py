

'''
Algoritmo: Sumar los n primeros números
Entrada: n (número entero mayor o igual que 0)
Salida: salida (suma 1 + 2 + ... + n)

INICIO
    salida <- 0
    PARA i DESDE 1 HASTA n HACER
        salida <- salida + i
    FIN PARA
    DEVOLVER salida
FIN
'''

# Algoritmo Sumar los n primeros números en python
def sumar_n_primeros_numeros(n):
    """Devuelve la suma de los números del 1 al n."""
    salida = 0
    for i in range(1, n + 1):
        salida = salida + i
    return salida


# =====================================================================
# PRUEBAS de ejecución
# =====================================================================

if __name__ == "__main__":
    print("sumar_n_primeros_numeros(5) =", sumar_n_primeros_numeros(5))
    print("sumar_n_primeros_numeros(10) =", sumar_n_primeros_numeros(10))
    print("sumar_n_primeros_numeros(100) =", sumar_n_primeros_numeros(100))
    print("sumar_n_primeros_numeros(0) =", sumar_n_primeros_numeros(0))


'''
Ejecución (python sumar_n_primeros_numeros.py):

sumar_n_primeros_numeros(5) = 15
sumar_n_primeros_numeros(10) = 55
sumar_n_primeros_numeros(100) = 5050
sumar_n_primeros_numeros(0) = 0

Comprobación: 1 + 2 + 3 + 4 + 5 = 15, y con la fórmula n * (n + 1) / 2
se obtiene lo mismo: 10 * 11 / 2 = 55 y 100 * 101 / 2 = 5050.
'''
