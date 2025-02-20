from flota_vehiculos import Vehiculo, Mantenimiento, FlotaVehiculos

def mostrar_menu():
    print("\n--- Menú de Gestión de Flota de Vehículos ---")
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

        if opcion == "1":
            placa = input("Ingrese la placa del vehículo: ")
            marca = input("Ingrese la marca del vehículo: ")
            modelo = input("Ingrese el modelo del vehículo: ")
            año = int(input("Ingrese el año del vehículo: "))
            kilometraje = float(input("Ingrese el kilometraje del vehículo: "))
            try:
                vehiculo = Vehiculo(placa, marca, modelo, año, kilometraje)
                flota.registrar_vehiculo(vehiculo)
                print("Vehículo registrado exitosamente.")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            placa = input("Ingrese la placa del vehículo: ")
            vehiculo = flota.buscar_vehiculo(placa)
            if vehiculo:
                fecha = input("Ingrese la fecha del mantenimiento: ")
                descripcion = input("Ingrese la descripción del mantenimiento: ")
                costo = float(input("Ingrese el costo del mantenimiento: "))
                try:
                    mantenimiento = Mantenimiento(fecha, descripcion, costo)
                    vehiculo.agregar_mantenimiento(mantenimiento)
                    print("Mantenimiento agregado exitosamente.")
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print("Vehículo no encontrado.")

        elif opcion == "3":
            placa = input("Ingrese la placa del vehículo: ")
            vehiculo = flota.buscar_vehiculo(placa)
            if vehiculo:
                print("Historial de mantenimientos:")
                for mantenimiento in vehiculo.consultar_historial():
                    print(mantenimiento)
            else:
                print("Vehículo no encontrado.")

        elif opcion == "4":
            placa = input("Ingrese la placa del vehículo: ")
            vehiculo = flota.buscar_vehiculo(placa)
            if vehiculo:
                costo_total = vehiculo.calcular_costo_total()
                print(f"Costo total de mantenimientos: {costo_total}")
            else:
                print("Vehículo no encontrado.")

        elif opcion == "5":
            vehiculos = flota.listar_vehiculos()
            if vehiculos:
                print("Vehículos en la flota:")
                for vehiculo in vehiculos:
                    print(vehiculo)
            else:
                print("No hay vehículos registrados.")

        elif opcion == "6":
            placa = input("Ingrese la placa del vehículo: ")
            vehiculo = flota.buscar_vehiculo(placa)
            if vehiculo:
                print(f"Vehículo encontrado: {vehiculo}")
            else:
                print("Vehículo no encontrado.")

        elif opcion == "7":
            placa = input("Ingrese la placa del vehículo: ")
            if flota.eliminar_vehiculo(placa):
                print("Vehículo eliminado correctamente.")
            else:
                print("Vehículo no encontrado.")

        elif opcion == "8":
            print("Ha salido del programa.")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()