import flota_vehiculos
import vehiculo
import Mantenimiento

def mostrar_menu():
    print("\n == Menú ==")
    print("1. Registrar un vehiculo")
    print("2. Agregar mantenimiento a un vehiculo")
    print("3. Consultar historial de mantenimientos de un vehiculo")
    print("4. Calcular costo total de mantenimientos de un vehiculo")
    print("5. Listar todos los vehículos")
    print("6. Buscar un vehiculo por placa")
    print("7. Eliminar un vehiculo por placa")
    print("8. Salir")
    return input("Ingrese una opcion: ")


def main():
    flota = flota_vehiculos.FlotaVehiculos()

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            placa = input("Ingrese la placa del vehiculo: ")
            marca = input("Ingrese la marca del vehiculo: ")
            modelo = input("Ingrese el modelo del vehiculo: ")
            año = int(input("Ingrese el año del vehiculo: "))
            kilometraje = float(input("Ingrese el kilometraje del vehiculo: "))
            vehiculo_nuevo = vehiculo.Vehiculo(placa, marca, modelo, año, kilometraje)
            flota.registrar_vehiculo(vehiculo_nuevo)
            print("Vehículo registrado exitosamente.")

        elif opcion == "2":
            placa = input("Ingrese la placa del vehiculo: ")
            vehiculo_buscado = flota.buscar_vehiculo(placa)
            if vehiculo_buscado:
                fecha = input("Ingrese la fecha del mantenimiento: ")
                descripcion = input("Ingrese la descripción del mantenimiento: ")
                costo = float(input("Ingrese el costo del mantenimiento: "))
                mantenimiento_nuevo = Mantenimiento.Mantenimiento(fecha, descripcion, costo)
                vehiculo_buscado.agregar_mantenimiento(mantenimiento_nuevo)
                print("Mantenimiento agregado exitosamente")
            else:
                print("Vehiculo no encontrado")

        elif opcion == "3":
            placa = input("Ingrese la placa del vehiculo: ")
            vehiculo_buscado = flota.buscar_vehiculo(placa)
            if vehiculo_buscado:
                print("Historial de mantenimientos:")
                for mantenimiento_str in vehiculo_buscado.consultar_historial():
                    print(mantenimiento_str)
            else:
                print("Vehiculo no encontrado")

        elif opcion == "4":
            placa = input("Ingrese la placa del vehiculo: ")
            vehiculo_buscado = flota.buscar_vehiculo(placa)
            if vehiculo_buscado:
                costo_total = vehiculo_buscado.calcular_costo_total()
                print(f"Costo total de mantenimientos: {costo_total}")
            else:
                print("Vehiculo no encontrado")

        elif opcion == "5":
            vehiculos_lista = flota.listar_vehiculos()
            if vehiculos_lista:
                print("Vehiculos en la flota:")
                for vehiculo_str in vehiculos_lista:
                    print(vehiculo_str)
            else:
                print("No hay vehiculos registrados")

        elif opcion == "6":
            placa = input("Ingrese la placa del vehiculo: ")
            vehiculo_buscado = flota.buscar_vehiculo(placa)
            if vehiculo_buscado:
                print(f"Vehiculo encontrado: {vehiculo_buscado}")
            else:
                print("Vehiculo no encontrado")

        elif opcion == "7":
            placa = input("Ingrese la placa del vehiculo: ")
            if flota.eliminar_vehiculo(placa):
                print("Vehiculo eliminado")
            else:
                print("Vehiculo no encontrado")

        elif opcion == "8":
            print("Ha salido del programa")
            break

        else:
            print("Opcion no valida")

if __name__ == "__main__":
    main()