class MochilaVideojuego:
    def __init__(self, capacidad=4):
        self.capacidad = capacidad
        # El vector se inicializa con casillas vacías (None) representando los slots
        self.vector_slots = [None] * capacidad

    def mostrar_inventario(self):
        print("\n--- INVENTARIO DE LA MOCHILA ---")
        for indice, objeto in enumerate(self.vector_slots):
            estado = objeto if objeto is not None else "[ VACÍO ]"
            print(f"Slot [{indice}]: {estado}")
        print("---------------------------------")

    def agregar_objeto(self, objeto):
        # Buscamos la primera posición libre (None) en el vector
        for i in range(self.capacidad):
            if self.vector_slots[i] is None:
                self.vector_slots[i] = objeto
                print(f"¡Éxito! Has guardado '{objeto}' en el slot [{i}].")
                return True
        
        # Caso límite: La mochila está llena
        print(f"¡Inventario lleno! No puedes guardar '{objeto}'. La mochila está a su máxima capacidad ({self.capacidad}/{self.capacidad}).")
        return False

    def usar_o_remover_objeto(self, indice):
        if 0 <= indice < self.capacidad:
            if self.vector_slots[indice] is not None:
                objeto_retirado = self.vector_slots[indice]
                self.vector_slots[indice] = None
                print(f"Has usado o descartado '{objeto_retirado}' del slot [{indice}]. Ahora está vacío.")
            else:
                print(f"El slot [{indice}] ya se encuentra vacío.")
        else:
            print("Error: Posición de slot inválida.")


# ==========================================
# SIMULACIÓN Y PRUEBAS CON LOS OBJETOS DEFINIDOS
# ==========================================

# Creamos una mochila con capacidad fija de 4 espacios
mi_mochila = MochilaVideojuego(4)

print("--- CASO DE FUNCIONAMIENTO NORMAL ---")
mi_mochila.agregar_objeto("Arma")
mi_mochila.agregar_objeto("Linterna")
mi_mochila.agregar_objeto("Curas")
mi_mochila.agregar_objeto("Alimentos")

mi_mochila.mostrar_inventario()

print("\n--- CASO LÍMITE (MOCHILA LLENA) ---")
# Intentamos agregar un 5to objeto cuando ya no hay espacio disponible
mi_mochila.agregar_objeto("Mapa")

print("\n--- LIBERANDO ESPACIO Y REINTENTANDO ---")
# Usamos el objeto del slot 1 (Linterna) para liberar espacio
mi_mochila.usar_o_remover_objeto(1)
mi_mochila.mostrar_inventario()

# Ahora sí podemos guardar el nuevo objeto en el espacio liberado
mi_mochila.agregar_objeto("Mapa")
mi_mochila.mostrar_inventario()