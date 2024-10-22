def ley_coulomb():
    print("Ley de Coulomb: F = k * (q1 * q2) / r^2")
    k = 8.99e9  # Constante de Coulomb (N·m²/C²)
    q1 = float(input("Ingresa la carga q1 (en C): "))
    q2 = float(input("Ingresa la carga q2 (en C): "))
    r = float(input("Ingresa la distancia entre las cargas (en m): "))
    
    F = k * (q1 * q2) / (r**2)
    print(f"La fuerza de Coulomb es: {F} N")

def ley_gauss():
    print("Ley de Gauss: Φ = Q_interna / ε_0")
    epsilon_0 = 8.85e-12  # Constante de permitividad eléctrica en el vacío (C²/N·m²)
    Q_interna = float(input("Ingresa la carga interna (en C): "))
    
    flujo = Q_interna / epsilon_0
    print(f"El flujo eléctrico es: {flujo} N·m²/C")

def energia_potencial():
    print("Energía potencial eléctrica: U = k * (q1 * q2) / r")
    k = 8.99e9  # Constante de Coulomb (N·m²/C²)
    q1 = float(input("Ingresa la carga q1 (en C): "))
    q2 = float(input("Ingresa la carga q2 (en C): "))
    r = float(input("Ingresa la distancia entre las cargas (en m): "))
    
    U = k * (q1 * q2) / r
    print(f"La energía potencial eléctrica es: {U} J")

def seleccionar_operacion():
    print("\n--- Menú ---")
    print("1. Calcular la fuerza de Coulomb")
    print("2. Calcular el flujo eléctrico (Ley de Gauss)")
    print("3. Calcular la energía potencial eléctrica")
    print("4. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        ley_coulomb()
    elif opcion == "2":
        ley_gauss()
    elif opcion == "3":
        energia_potencial()
    elif opcion == "4":
        return False  # Salir del programa
    else:
        print("Opción inválida, intenta nuevamente.")
    
    return True  # Continuar en el programa

def menu():
    continuar = True
    while continuar:
        continuar = seleccionar_operacion()
        
        if continuar:
            # Preguntar si desea hacer otra operación
            repetir = input("¿Deseas realizar otra operación? (sí/no): ").strip().lower()
            if repetir == "no":
                print("Saliendo del programa...")
                continuar = False

menu()