# Algoritmo PSO: Resultados de la ejecución única

## Función objetivo
$$f(x, y) = \sin(x) \cdot e^{(1-\cos(y))^2} + \cos(y) \cdot e^{(1-\sin(x))^2} + (x-y)^2$$

Dominio: $-2\pi \leq x \leq 2\pi$, $-2\pi \leq y \leq 2\pi$. Objetivo: minimizar $f(x,y)$.

## Configuración usada (main.py)
- Población: 30 partículas.
- Iteraciones: 500 (criterio de paro).
- Inercia: $w$ decreciente 0.9 → 0.4.
- Coeficientes: $c_1 = 2.0$ (cognitivo), $c_2 = 2.0$ (social).
- Topologías: `gbest` y `lbest` (vecindario = 3).
- Velocidad máxima: 10% del rango en cada dimensión.
- Inicialización: posiciones y velocidades aleatorias uniformes en el dominio.
- Memoria: $pbest$ por partícula y $gbest$ o $lbest$ según topología; se actualiza en cada iteración.

## Resultados de las corridas (5 por configuración)
- Mejor fitness global hallado: $-106.7645367493$ (ambas topologías).
- Mejor solución reportada: $x = -1.5821421787$, $y = -3.1302468093$, $f(x,y) = -106.7645367493$ (`PSO_gbest_estandar`).
- Estadísticos por configuración (mejor / promedio / desviación):
  - `PSO_gbest_estandar`: -106.7645367493 / -106.7645367493 / 0.0000000000
  - `PSO_lbest_vecindario3`: -106.7645367493 / -106.7645367493 / 0.0000000000

## Convergencia (según salida estándar)
- Ambas topologías convergen antes de la iteración 250 y permanecen estables hasta la 500.
- Ejemplo `gbest`: a partir de iteración ~150 llega a $f \approx -106.7645$ y se mantiene.

## Incisos solicitados (PSO)
- a) Función objetivo: ver sección inicial.
- b) Soluciones iniciales: posiciones y velocidades aleatorias en el dominio; $pbest$ inicial = posición inicial.
- c) Parámetros: $w$ decreciente 0.9→0.4, $c_1=2.0$, $c_2=2.0$; topologías `gbest` y `lbest` (vecindario 3).
- d) Memoria: $pbest$ individual y $gbest$ global (o $lbest$ por vecindario) actualizados cada iteración.
- e) Intensificación/diversificación: $w$ decreciente (más exploración al inicio, más explotación al final); términos cognitivo/social guían hacia $pbest$ y $gbest$/$lbest$; límite de velocidad evita saltos grandes.
- f) Criterio de paro: 500 iteraciones.
- g) Mínimo encontrado: $f = -106.7645367493$ en $x = -1.5821421787$, $y = -3.1302468093$; la distribución final del enjambre se muestra en las gráficas de enjambre.

## Imágenes generadas (en esta carpeta)
- `convergencia_PSO_gbest_estandar.png`
- `convergencia_PSO_lbest_vecindario3.png`
- `comparacion_convergencia.png`
- `enjambre_PSO_gbest_estandar.png`
- `enjambre_PSO_lbest_vecindario3.png`

## Comentarios
- Las dos topologías convergieron al mismo valor con desviación nula en 5 corridas.
- Las gráficas de enjambre muestran concentración de partículas cerca del punto óptimo encontrado.
- Se omite la escritura de JSON; los resultados están en la salida estándar y en las imágenes listadas.
