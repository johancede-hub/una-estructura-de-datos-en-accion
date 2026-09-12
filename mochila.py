
mochila = [None, None, None, None]

def mostrar_inventario():
    print("\n INVENTARIO ACTUAL")
    for i in range(len(mochila)):
        if mochila[i] is None:
            print(f"Slot [{i}]: [ VACÍO ]")
        else:
            print(f"Slot [{i}]: {mochila[i]}")
    print("-------------------------\n")

def agregar_objeto(objeto):

    for i in range(len(mochila)):
        if mochila[i] is None:
            mochila[i] = objeto
            print(f"¡Éxito! Guardaste '{objeto}' en el slot [{i}].")
            return True
   
    print(f"¡Inventario lleno! No puedes guardar '{objeto}'. La mochila ha llegado a su límite de 4 espacios.")
    return False

def quitar_objeto(objeto):
    
    for i in range(len(mochila)):
        if mochila[i] == objeto:
            mochila[i] = None
            print(f"¡Objeto retirado! Sacaste '{objeto}' del slot [{i}].")
            return True
    print(f"El objeto '{objeto}' no se encuentra en la mochila.")
    return False

# - DEMONSTRACIÓN Y PRUEBAS -

mostrar_inventario()

print("--- AGREGANDO OBJETOS ---")
agregar_objeto("Arma")
agregar_objeto("Linterna")
agregar_objeto("Curas")
agregar_objeto("Alimentos")

mostrar_inventario()

print("--- CASO LÍMITE (AGREGAR DE MÁS) ---")
agregar_objeto("Mapa")

print("--- RETIRANDO UN OBJETO ---")
quitar_objeto("Linterna")

mostrar_inventario()

print("--- AGREGANDO NUEVO OBJETO TRAS LIBERAR ESPACIO ---")
agregar_objeto("Mapa")

mostrar_inventario()