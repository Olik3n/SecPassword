import random
import string

def generar_contraseña(longitud):
    if longitud < 8:
        print("Para una contraseña segura, elige al menos 8 caracteres.")
        return None

    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

# Ejemplo de uso:
try:
    longitud = int(input("Ingresa la longitud de la contraseña que deseas (mínimo 8): "))
    contraseña_segura = generar_contraseña(longitud)
    if contraseña_segura:
        print("Tu contraseña generada es:", contraseña_segura)
except ValueError:
    print("Por favor, ingresa un número válido.")

