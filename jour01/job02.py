class Operation:
    def __init__(self, nombre1=12, nombre2=3):
        self.nombre1 = nombre1
        self.nombre2 = nombre2


operation_instance = Operation()

print(f"Nombre 1: {operation_instance.nombre1}")
print(f"Nombre 2: {operation_instance.nombre2}")