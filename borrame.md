# Algoritmo Genético: Resultados de la Ejecución Única

## Función objetivo
$$f(x, y) = \sin(x) \cdot e^{(1-\cos(y))^2} + \cos(y) \cdot e^{(1-\sin(x))^2} + (x-y)^2$$

Dominio: $-2\pi \leq x \leq 2\pi$, $-2\pi \leq y \leq 2\pi$. Objetivo: minimizar $f(x,y)$.

## Configuración utilizada (main.py)
- Población: 50 individuos
- Generaciones: 500
- Cruza: un punto, $p_c = 0.25$
- Mutación: inversión de bits, $p_m = 0.01$
- Selección: ruleta (elitismo de 2 individuos)
- Representación: binaria, 17 bits para $x$ y 17 bits para $y$ (precisión 4 decimales)
- Óptimo numérico de referencia: $x^* = 0.665277$, $y^* = 0.905519$, $f(x^*, y^*) = 1.487019$ (L-BFGS-B)

## Incisos solicitados (según main.py)
- a) Función de aptitud: $\text{aptitud}(x,y)=1/(1+f(x,y))$ para transformar minimización en maximización.
- b) Tamaño de población: 50 individuos (corrida única solicitada).
- c) Representación: cadena binaria, 17 bits para $x$ y 17 bits para $y$ (precisión 4 decimales).
- d) Soluciones iniciales: población aleatoria uniforme sobre los bits.
- e) Selección: ruleta proporcional; elitismo de 2 mejores preservado.
- f) Cruza: un punto con probabilidad $p_c=0.25$; (torneo disponible pero no usado en esta corrida).
- g) Mutación: inversión de bits con probabilidad $p_m=0.01$ por bit.
- h) Criterio de paro: 500 generaciones fijas.
- i) Mejor valor hallado en esta corrida: $f=-0.998422$ en $x=3.113190$, $y=2.540244$; mejor población final reportada abajo.

## Resultado de la ejecución
- Mejor valor hallado: $f(x,y) = -0.998422$
- Coordenadas: $x = 3.113190$, $y = 2.540244$
- Diferencia vs. óptimo numérico de referencia: $|f - f^*| = 2.485441$

Mejores 10 individuos finales (idénticos en esta corrida):

| Rango | x | y | f(x,y) | Aptitud |
|-------|---|---|--------|---------|
| 1-10 | 3.113190 | 2.540244 | -0.998422 | 633.534490 |

## Convergencia observada (salida estándar)
- Gen 100: $f = -0.369287$
- Gen 200: $f = -0.985559$
- Gen 300: $f = -0.998422$
- Gen 400: $f = -0.998422$
- Gen 500: $f = -0.998422$

## Visualizaciones generadas por el main
- `convergencia.png`: evolución del mejor $f(x,y)$ por generación para la corrida única.
- `funcion_3d.png`: superficie 3D de $f(x,y)$ en el dominio especificado.

## Comentarios
- El GA encuentra un mínimo en torno a $f \approx -1$, diferente del óptimo numérico de referencia ($f \approx 1.49$), sugiriendo que la función es multimodal y que el optimizador local converge a otro mínimo.
- Elitismo y la probabilidad de cruza baja mantienen la solución estable tras la generación 300.
