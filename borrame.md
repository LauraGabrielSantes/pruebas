# Búsqueda Dispersa (Scatter Search) – Ejercicio 3

## Resumen de ejecución
- Instancia: 38 ciudades (`38.txt`)
- Corridas: 5
- Mejor costo: 6659.9067
- Peor costo: 6659.9067
- Promedio: 6659.9067
- Desviación estándar: 0.0000
- Mediana: 6659.9067
- Mejor corrida: 1 (mismo valor en todas)
- Mejor permutación (IDs):
```
[16, 18, 19, 17, 11, 12, 9, 8, 7, 6, 5, 3, 4, 2, 1, 10, 14, 21, 29, 30, 32,
 35, 37, 38, 33, 34, 36, 31, 27, 28, 24, 22, 25, 26, 23, 20, 15, 13]
```
- Imágenes generadas: `costos_por_corrida.png`, `mejor_tour_visualizacion.png`

## Respuestas a incisos
**a. Big Set**
- Generado con `tam_poblacion=80`.
- Construcción por ciudad inicial: para cada ciudad se arma un tour con **Nearest Neighbor (NN)** y luego se mejora con **2-opt**. Si se requieren más individuos, se añaden tours aleatorios (`shuffle`) también refinados con 2-opt.
- Todas las soluciones son factibles y diversas por la variación de ciudad inicial y el barajado.

**b. Manejo de infactibilidad**
- No se producen recorridos infactibles: NN siempre construye tours válidos (todas las ciudades, sin repetir) y 2-opt preserva factibilidad. No se requiere reparación.

**c. Método de mejora**
- **2-opt** como búsqueda local para cada individuo inicial y para soluciones combinadas.
- Mejora adicional mediante **path relinking** (ver inciso g) seguido de 2-opt para pulir el tour resultante.

**d. Actualización del RefSet**
- RefSet mezcla calidad y diversidad.
- Cuando aparece una nueva solución: si mejora al peor costo o supera un umbral de diversidad respecto al RefSet, reemplaza al peor elemento. Así se mantiene el equilibrio entre buena calidad y heterogeneidad.

**e. Tamaño y composición del RefSet**
- Base: `tam_refset=12`, con variación aleatoria ±2 por corrida (mínimo 6, máximo mitad de la población).
- Se arma con la mitad de mejores costos (calidad) y la mitad más diversas (distancia de aristas respecto a las ya incluidas).

**f. Generador de subconjuntos**
- Se forman todos los pares (i, j) del RefSet para combinarlos (estrategia all-pairs). En estancamiento se reinyecta diversidad antes de seguir combinando.

**g. Método de combinación**
- **Path relinking** entre dos tours: se toma un tour guía y se van corrigiendo posiciones del tour origen hacia el guía, aplicando 2-opt después de cada ajuste; se conserva el mejor costo encontrado en el camino.

**h. Criterio de paro**
- Estancamiento: `max_estancamiento=10` iteraciones sin mejora global.
- Límite adicional: `max_iter=150` para acotar tiempo.
- Con estos límites el proceso termina en ~3 minutos en esta máquina.

**i. Costos por corrida y mejor permutación**
- Corridas (5): todos con costo 6659.9067 → rango = 0.0, std = 0.0.
- Mejor solución: misma permutación en todas las corridas (lista arriba).

## Notas sobre resultados
- La instancia presenta un óptimo local muy estable: con las configuraciones actuales todas las corridas convergen al mismo valor.
- Para buscar más diversidad se podría bajar población y estancamiento, o aumentar aleatoriedad en la generación inicial y en path relinking, pero se priorizó estabilidad y tiempos contenidos.
