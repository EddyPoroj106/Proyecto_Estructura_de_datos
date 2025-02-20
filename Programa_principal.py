from vehiculo import Vehiculo
from Mantenimiento import Mantenimiento
from flota_vehiculos import FlotaVehiculos

def mostrar_menu():
    print("-----> Menú de Gestión de Flota de Vehículos <-----")
    print("1. Registrar un vehículo")
    print("2. Agregar mantenimiento a un vehículo")
    print("3. Consultar historial de mantenimientos de un vehículo")
    print("4. Calcular costo total de mantenimientos de un vehículo")
    print("5. Listar todos los vehículos")
    print("6. Buscar un vehículo por placa")
    print("7. Eliminar un vehículo por placa")
    print("8. Salir")
    
def main():
    flota = FlotaVehiculos()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        print("==========================================")
        if opcion == "1":
            print("---> Registrar un vehículo <---")
            placa = input("Ingrese la placa del vehículo: ")
            marca = input("Ingrese la marca del vehículo: ")
            modelo = input("Ingrese el modelo del vehículo: ")
            año = int(input("Ingrese el año del vehículo: "))
            kilometraje = float(input("Ingrese el kilometraje del vehículo: "))
            try:
                vehiculo = Vehiculo(placa, marca, modelo, año, kilometraje)
                flota.registrar_vehiculo(vehiculo)
                print("Vehículo registrado exitosamente.")
                print("==========================================")
            except ValueError as e:
                print(f"Error: {e}")
                print("==========================================")
                

        elif opcion == "2":
            print("---> Agregar Mantenimiento <---")
            placa = input("Ingrese la placa del vehículo: ")
            vehiculo = flota.buscar_vehiculo(placa)
            if vehiculo:
                fecha = input("Ingrese la fecha del mantenimiento: ")
                descripcion = input("Ingrese la descripción del mantenimiento: ")
                costo = float(input("Ingrese el costo del mantenimiento: "))
                try:
                    nuevo_mantenimiento = Mantenimiento(fecha, descripcion, costo)
                    vehiculo.agregar_mantenimiento(nuevo_mantenimiento)
                    print("Mantenimiento agregado exitosamente.")
                    print("==========================================")
                except ValueError as e:
                    print(f"Error: {e}")
                    print("==========================================")
            else:
                print("Vehículo no encontrado.")
                print("==========================================")

        elif opcion == "3":
            print("---> Historial de Mantenimientos <---")
            placa = input("Ingrese la placa del vehículo: ")
            vehiculo = flota.buscar_vehiculo(placa)
            if vehiculo:
                print("Historial de mantenimientos:")
                for mantenimiento in vehiculo.consultar_historial():
                    print(mantenimiento)
                print("==========================================")
            else:
                print("Vehículo no encontrado.")
                print("==========================================")

        elif opcion == "4":
            print("---> Costo Total de Mantenimientos <---")
            placa = input("Ingrese la placa del vehículo: ")
            vehiculo = flota.buscar_vehiculo(placa)
            if vehiculo:
                costo_total = vehiculo.calcular_costo_total()
                print(f"Costo total de mantenimientos: {costo_total}")
                print("==========================================")
            else:
                print("Vehículo no encontrado.")
                print("==========================================")

        elif opcion == "5":
            print("---> Listar vehículos <---")
            vehiculos = flota.listar_vehiculos()
            if vehiculos:
                print("Vehículos Registrados:")
                for vehiculo in vehiculos:
                    print(vehiculo)
                    print("==========================================")
            else:
                print("No hay vehículos registrados.")
                print("==========================================")

        elif opcion == "6":
            print("---> Buscar vehículo <---")
            placa = input("Ingrese la placa del vehículo: ")
            vehiculo = flota.buscar_vehiculo(placa)
            if vehiculo:
                print(f"Vehículo encontrado: {vehiculo}")
                print("==========================================")
            else:
                print("Vehículo no encontrado.")
                print("==========================================")

        elif opcion == "7":
            print("---> Eliminar vehículo <---")
            placa = input("Ingrese la placa del vehículo: ")
            if flota.eliminar_vehiculo(placa):
                print("Vehículo eliminado correctamente.")
                print("==========================================")
            else:
                print("Vehículo no encontrado.")
                print("==========================================")

        elif opcion == "8":
            print("Ha salido del programa.")
            print("==========================================")
            break

        else:
            print("Opción no válida.")
            print("==========================================")

if __name__ == "__main__":
    main()