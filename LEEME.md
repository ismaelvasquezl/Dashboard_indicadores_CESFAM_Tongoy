# Dashboard de Seguimiento · CESFAM Tongoy

Sistema de seguimiento longitudinal de indicadores Metas Sanitarias e IAAPS.

## Estructura

```
dashboard_tongoy/
├── dashboard.html          ← ABRIR ESTE en el navegador (autocontenido)
├── generar_dashboard.py    ← ejecutar para regenerar tras editar datos
├── construir_html.py       ← motor de render (no se toca)
└── datos/
    ├── mmss_tongoy.csv      ← serie Metas Sanitarias (editable)
    ├── iaaps_tongoy.csv     ← serie IAAPS (editable)
    └── catalogo_rem.csv     ← procedencia REM de cada indicador
```

## Para ver el dashboard AHORA
Abrir `dashboard.html` en Chrome/Edge. Es autocontenido: no necesita internet
salvo para las tipografías. Funciona en escritorio y móvil.

## Para actualizar cada mes (corte nuevo)
1. Abrir `datos/mmss_tongoy.csv` y `datos/iaaps_tongoy.csv` en Excel
2. Agregar UNA fila por indicador con el nuevo corte, respetando las columnas
3. Guardar como CSV (codificación UTF-8)
4. Ejecutar en terminal:  `python3 generar_dashboard.py`
5. Se regenera `dashboard.html` con la serie extendida

## Para cargar años anteriores (2024, 2025)
Agregar filas con `anio=2024` o `2025` y su `corte`/`mes`. El eje temporal
del dashboard se extiende automáticamente y la proyección gana precisión.

## Columnas de los CSV de datos
- `meta`/`indicador`: código (I, IIIA, M3, M91...)
- `tipo`: mensual / anual / semestral
- `corte`: número de corte del año
- `mes`, `anio`: período
- `valor_corte`: % de cumplimiento AL CORTE (el valor principal)
- `global`: % de cumplimiento global (opcional)
- `comuna`: % comunal para comparación (opcional)
- `meta_umbral`: meta del indicador
- `numerador`, `denominador`: recuento REM (alimenta la vista "cómo se construye")
- `brecha`: diferencia al corte (opcional)
- `estado`: cumple / bajo / critico / sindato
- `nota`: salvedad que aparece en el detalle (ej. avance no oficial)
- `polaridad` (solo IAAPS): directa / inversa (M4 es inversa)

## Notas técnicas
- Los indicadores semestrales muestran avances intermedios no oficiales;
  la salvedad aparece en la nota del detalle. Corte formal: junio y diciembre.
- La proyección es regresión lineal simple; es referencial con pocos puntos.
- Meta I DSM julio: salto a 100% por decisión directiva DESAM (anotado).
