class Operation:
    def __init__(self, nombre1=12, nombre2=3):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        result = self.nombre1 + self.nombre2
        print(f"Le résultat de l'addition : {result}")

operation_instance = Operation()
print(f"Nombre 1 : {operation_instance.nombre1}")
print(f"Nombre 2 : {operation_instance.nombre2}")

# Appeler la méthode addition
operation_instance.addition()