import numpy as np
import matplotlib.pyplot as plt

g = 9.8  # gravedad

def posicion_3d(x0, y0, z0, vx0, vy0, vz0, t):
    x = x0 + vx0 * t
    y = y0 + vy0 * t
    z = z0 + vz0 * t - 0.5 * g * t**2
    return x, y, z

def trayectoria_3d(x0, y0, z0, vx0, vy0, vz0, t_final):
    ts = np.linspace(0, t_final, 200)
    xs, ys, zs = [], [], []

    for t in ts:
        x, y, z = posicion_3d(x0, y0, z0, vx0, vy0, vz0, t)
        xs.append(x)
        ys.append(y)
        zs.append(z)

    return ts, xs, ys, zs

def graficar(xs, ys, zs, x0, y0, z0, vx0, vy0, vz0, xf, yf, zf):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Graficar la trayectoria
    ax.plot(xs, ys, zs, 'b-', linewidth=2, label='Trayectoria')
    
    # Marcar el punto inicial
    ax.scatter([x0], [y0], [z0], color='green', s=100, label='Punto inicial', zorder=5)
    
    # Marcar el punto final
    ax.scatter([xf], [yf], [zf], color='purple', s=100, label='Punto final', zorder=5)
    
    # Vector de velocidad inicial (escalado para visualización)
    escala_velocidad = 0.1  # Factor de escala para visualizar mejor el vector
    ax.quiver(x0, y0, z0, vx0 * escala_velocidad, vy0 * escala_velocidad, vz0 * escala_velocidad,
              color='red', arrow_length_ratio=0.3, linewidth=2, label='Velocidad inicial')
    
    # Vector de gravedad (mostrado en el punto inicial, apuntando hacia abajo)
    escala_gravedad = 0.5  # Factor de escala para visualizar la gravedad
    ax.quiver(x0, y0, z0, 0, 0, -g * escala_gravedad,
              color='orange', arrow_length_ratio=0.3, linewidth=2, label='Gravedad')
    
    # Etiquetas y título
    ax.set_xlabel('X (m)', fontsize=11)
    ax.set_ylabel('Y (m)', fontsize=11)
    ax.set_zlabel('Z (m)', fontsize=11)
    ax.set_title('Trayectoria del tiro parabólico con vectores', fontsize=13, fontweight='bold')
    ax.legend(loc='upper left')
    
    # Ajustar los límites para que se vean bien los vectores
    ax.set_box_aspect([1, 1, 1])
    
    plt.show()

def mostrar_ayuda():
    print("\n" + "="*60)
    print("AYUDA - Simulador de Tiro Parabólico 3D")
    print("="*60)
    print("\nCOMANDOS DISPONIBLES:")
    print("  calcular  - Calcular y graficar una trayectoria")
    print("  help      - Mostrar esta ayuda")
    print("  salir     - Salir del programa (también: exit, quit)")
    print("\nPARÁMETROS DEL TIRO PARABÓLICO:")
    print("  x0, y0, z0  - Posición inicial (m)")
    print("  vx0, vy0, vz0 - Velocidad inicial en cada eje (m/s)")
    print("  t_final     - Tiempo final de la simulación (s)")
    print("\nEJEMPLO:")
    print("  Posición inicial: x0=0, y0=0, z0=0")
    print("  Velocidad inicial: vx0=5, vy0=3, vz0=10")
    print("  Tiempo final: t_final=2.5")
    print("\nNOTAS:")
    print("  - La gravedad está fijada en 9.8 m/s²")
    print("  - El programa calculará la trayectoria y mostrará un gráfico 3D")
    print("="*60 + "\n")

def obtener_valor(mensaje, valor_por_defecto=None):
    """Solicita un valor numérico al usuario con opción de valor por defecto"""
    if valor_por_defecto is not None:
        entrada = input(f"{mensaje} (Enter para usar {valor_por_defecto}): ").strip()
        if entrada == "":
            return valor_por_defecto
        try:
            return float(entrada)
        except ValueError:
            print(f"Valor inválido. Usando {valor_por_defecto}")
            return valor_por_defecto
    else:
        while True:
            try:
                return float(input(f"{mensaje}: "))
            except ValueError:
                print("Por favor, ingrese un número válido.")

def calcular_trayectoria():
    print("\n--- Cálculo de Trayectoria ---")
    print("Ingrese los parámetros (puede presionar Enter para usar valores por defecto)")
    
    x0 = obtener_valor("Posición inicial X (m)", 0)
    y0 = obtener_valor("Posición inicial Y (m)", 0)
    z0 = obtener_valor("Posición inicial Z (m)", 0)
    vx0 = obtener_valor("Velocidad inicial en X (m/s)", 5)
    vy0 = obtener_valor("Velocidad inicial en Y (m/s)", 3)
    vz0 = obtener_valor("Velocidad inicial en Z (m/s)", 10)
    t_final = obtener_valor("Tiempo final (s)", 2.5)
    
    print(f"\nCalculando trayectoria con:")
    print(f"  Posición inicial: ({x0}, {y0}, {z0}) m")
    print(f"  Velocidad inicial: ({vx0}, {vy0}, {vz0}) m/s")
    print(f"  Tiempo final: {t_final} s")
    
    ts, xs, ys, zs = trayectoria_3d(x0, y0, z0, vx0, vy0, vz0, t_final)
    pos_final = posicion_3d(x0, y0, z0, vx0, vy0, vz0, t_final)
    xf, yf, zf = pos_final
    
    print(f"\nPosición final en t={t_final}s: ({xf:.2f}, {yf:.2f}, {zf:.2f}) m")
    print("Mostrando gráfico...\n")
    
    graficar(xs, ys, zs, x0, y0, z0, vx0, vy0, vz0, xf, yf, zf)

def main():
    print("\n" + "="*60)
    print("Simulador de Tiro Parabólico 3D")
    print("="*60)
    print("Escriba 'help' para ver la ayuda o 'salir' para terminar")
    print("="*60 + "\n")
    
    while True:
        comando = input("> ").strip().lower()
        
        if comando == "help" or comando == "h" or comando == "ayuda":
            mostrar_ayuda()
        elif comando == "calcular" or comando == "calc" or comando == "c":
            calcular_trayectoria()
        elif comando == "salir" or comando == "exit" or comando == "quit" or comando == "q":
            print("\n¡Hasta luego!")
            break
        elif comando == "":
            continue
        else:
            print(f"Comando '{comando}' no reconocido. Escriba 'help' para ver los comandos disponibles.")

if __name__ == "__main__":
    main()
