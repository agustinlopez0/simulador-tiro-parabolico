# Simulador de Tiro Parabólico 3D

## Descripción

Este programa es un simulador interactivo de tiro parabólico en tres dimensiones que permite calcular y visualizar la trayectoria de un proyectil bajo la influencia de la gravedad. El programa proporciona una interfaz de línea de comandos intuitiva y genera visualizaciones 3D con vectores que representan las fuerzas y velocidades que influyen en el movimiento.

## Características

- **Cálculo de trayectorias 3D**: Simula el movimiento de un proyectil en el espacio tridimensional
- **Visualización interactiva**: Genera gráficos 3D con matplotlib mostrando la trayectoria completa
- **Vectores informativos**: Muestra vectores de velocidad inicial y gravedad
- **Interfaz de usuario amigable**: Sistema de comandos interactivo con ayuda integrada
- **Valores por defecto**: Permite usar valores predefinidos para facilitar las pruebas

## Fundamentos Físicos

### Ecuaciones del Movimiento

El programa utiliza las ecuaciones del movimiento uniformemente acelerado para calcular la posición del proyectil en cada instante de tiempo.

#### Movimiento en el eje X (horizontal)
El movimiento en X es uniforme (sin aceleración):
```
x(t) = x₀ + vₓ₀ · t
```

#### Movimiento en el eje Y (horizontal)
El movimiento en Y también es uniforme:
```
y(t) = y₀ + vᵧ₀ · t
```

#### Movimiento en el eje Z (vertical)
El movimiento en Z está afectado por la gravedad:
```
z(t) = z₀ + vᵧ₀ · t - ½ · g · t²
```

Donde:
- `x₀, y₀, z₀`: Posición inicial (m)
- `vₓ₀, vᵧ₀, vᵧ₀`: Componentes de la velocidad inicial (m/s)
- `g`: Aceleración gravitatoria (9.8 m/s²)
- `t`: Tiempo (s)

### Cómo se Calculan los Resultados

1. **Entrada de parámetros**: El usuario proporciona la posición inicial, velocidad inicial y tiempo final.

2. **Generación de puntos temporales**: Se crea un array de 200 puntos temporales distribuidos uniformemente desde 0 hasta `t_final` usando `np.linspace(0, t_final, 200)`.

3. **Cálculo de la trayectoria**: Para cada instante de tiempo `t`, se calcula la posición (x, y, z) usando las ecuaciones del movimiento:
   - `x = x₀ + vₓ₀ · t`
   - `y = y₀ + vᵧ₀ · t`
   - `z = z₀ + vᵧ₀ · t - 0.5 · g · t²`

4. **Visualización**: Se grafican todos los puntos calculados para formar la trayectoria completa, junto con:
   - Punto inicial (verde)
   - Punto final (púrpura)
   - Vector de velocidad inicial (rojo)
   - Vector de gravedad (naranja)

## Requisitos

El programa requiere las siguientes librerías de Python:

- **numpy**: Para cálculos numéricos y generación de arrays
- **matplotlib**: Para la visualización 3D de las trayectorias

### Instalación de dependencias

```bash
pip install numpy matplotlib
```

## Uso del Programa

### Ejecución

```bash
python main.py
```

### Comandos Disponibles

Una vez iniciado el programa, puedes usar los siguientes comandos:

- **`calcular`** (o `calc`, `c`): Inicia el cálculo de una nueva trayectoria
- **`help`** (o `h`, `ayuda`): Muestra la ayuda del programa
- **`salir`** (o `exit`, `quit`, `q`): Termina la ejecución del programa

### Ejemplo de Uso

```
> calcular
Posición inicial X (m) (Enter para usar 0): 
Posición inicial Y (m) (Enter para usar 0): 
Posición inicial Z (m) (Enter para usar 0): 
Velocidad inicial en X (m/s) (Enter para usar 5): 
Velocidad inicial en Y (m/s) (Enter para usar 3): 
Velocidad inicial en Z (m/s) (Enter para usar 10): 
Tiempo final (s) (Enter para usar 2.5): 
```

### Parámetros

- **Posición inicial (x₀, y₀, z₀)**: Coordenadas del punto de partida en metros
- **Velocidad inicial (vₓ₀, vᵧ₀, vᵧ₀)**: Componentes de la velocidad inicial en m/s
- **Tiempo final (t_final)**: Duración de la simulación en segundos

## Estructura del Código

### Funciones Principales

#### `posicion_3d(x0, y0, z0, vx0, vy0, vz0, t)`
Calcula la posición del proyectil en un instante de tiempo específico.

**Parámetros:**
- `x0, y0, z0`: Posición inicial
- `vx0, vy0, vz0`: Velocidad inicial
- `t`: Tiempo

**Retorna:** Tupla `(x, y, z)` con la posición en el tiempo `t`

#### `trayectoria_3d(x0, y0, z0, vx0, vy0, vz0, t_final)`
Calcula la trayectoria completa del proyectil desde t=0 hasta t_final.

**Parámetros:**
- `x0, y0, z0`: Posición inicial
- `vx0, vy0, vz0`: Velocidad inicial
- `t_final`: Tiempo final de la simulación

**Retorna:** Tupla `(ts, xs, ys, zs)` con arrays de tiempos y posiciones

#### `graficar(xs, ys, zs, x0, y0, z0, vx0, vy0, vz0, xf, yf, zf)`
Genera la visualización 3D de la trayectoria con todos los elementos informativos.

**Elementos del gráfico:**
- **Línea azul**: Trayectoria completa del proyectil
- **Punto verde**: Posición inicial
- **Punto púrpura**: Posición final
- **Flecha roja**: Vector de velocidad inicial (escalado para visualización)
- **Flecha naranja**: Vector de gravedad (escalado para visualización)

#### `calcular_trayectoria()`
Función interactiva que solicita los parámetros al usuario, calcula la trayectoria y muestra los resultados.

#### `mostrar_ayuda()`
Muestra información detallada sobre el uso del programa.

#### `obtener_valor(mensaje, valor_por_defecto)`
Solicita un valor numérico al usuario con validación y soporte para valores por defecto.

## Ejemplos de Trayectorias

### Ejemplo 1: Tiro vertical hacia arriba
```
Posición inicial: (0, 0, 0) m
Velocidad inicial: (0, 0, 20) m/s
Tiempo final: 4 s
```
Resultado: El proyectil sube y luego cae debido a la gravedad.

### Ejemplo 2: Tiro horizontal
```
Posición inicial: (0, 0, 10) m
Velocidad inicial: (10, 0, 0) m/s
Tiempo final: 2 s
```
Resultado: El proyectil se mueve horizontalmente mientras cae.

### Ejemplo 3: Tiro parabólico completo
```
Posición inicial: (0, 0, 0) m
Velocidad inicial: (5, 3, 10) m/s
Tiempo final: 2.5 s
```
Resultado: Trayectoria parabólica en 3D con movimiento en los tres ejes.

## Limitaciones y Consideraciones

1. **Gravedad constante**: El programa asume una aceleración gravitatoria constante de 9.8 m/s².

2. **Sin resistencia del aire**: No se considera la fricción del aire, por lo que las trayectorias son ideales.

3. **Sin colisiones**: El programa no detecta colisiones con el suelo u otros objetos.

4. **Escalado de vectores**: Los vectores en el gráfico están escalados para mejor visualización y no representan magnitudes exactas.

## Notas Técnicas

- El programa utiliza 200 puntos para generar la trayectoria, proporcionando una curva suave.
- Los vectores se escalan con factores de 0.1 (velocidad) y 0.5 (gravedad) para mejorar la visualización.
- El gráfico 3D utiliza `projection='3d'` de matplotlib para la visualización tridimensional.

## Autor

Programa desarrollado para simulación de movimientos parabólicos en física.

## Licencia

Este proyecto es de uso educativo.

# TP-MF
