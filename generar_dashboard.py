#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
GENERADOR DE DASHBOARD · Metas Sanitarias e IAAPS · CESFAM Tongoy
================================================================================
Lee los CSV de la carpeta datos/ y produce un dashboard HTML autocontenido.

USO:
    python3 generar_dashboard.py

PARA ACTUALIZAR CADA MES:
    1. Abrir datos/mmss_tongoy.csv y datos/iaaps_tongoy.csv
    2. Agregar una fila por indicador con el nuevo corte
    3. Ejecutar este script
    4. Se regenera dashboard.html con la serie extendida automáticamente

PARA CARGAR AÑOS ANTERIORES (2024, 2025):
    Agregar filas con anio=2024 o 2025 y su corte/mes. El eje temporal
    se extiende solo. La proyección usa todos los puntos disponibles.

ESTRUCTURA:
    datos/mmss_tongoy.csv    · serie MMSS (una fila por meta x corte)
    datos/iaaps_tongoy.csv   · serie IAAPS (una fila por indicador x corte)
    datos/catalogo_rem.csv   · procedencia REM (numerador/denominador/celdas)
================================================================================
"""

import csv
import json
import os
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))
DATOS = os.path.join(BASE, 'datos')

MESES_ORDEN = {'enero':1,'febrero':2,'marzo':3,'abril':4,'mayo':5,'junio':6,
               'julio':7,'agosto':8,'septiembre':9,'octubre':10,'noviembre':11,'diciembre':12}

def leer_csv(nombre):
    ruta = os.path.join(DATOS, nombre)
    with open(ruta, encoding='utf-8') as f:
        return list(csv.DictReader(f))

def num(v):
    """Convierte a float manejando vacíos y comas decimales."""
    if v is None or str(v).strip() == '':
        return None
    try:
        return float(str(v).replace(',', '.'))
    except ValueError:
        return None

def clave_temporal(fila):
    """Ordena por año y mes."""
    anio = int(fila['anio'])
    mes = MESES_ORDEN.get(fila['mes'].lower().strip(), 0)
    return anio * 100 + mes

# ---------------------------------------------------------------------------
# 1 · Cargar datos
# ---------------------------------------------------------------------------
mmss = leer_csv('mmss_tongoy.csv')
iaaps = leer_csv('iaaps_tongoy.csv')
catalogo = leer_csv('catalogo_rem.csv')

# Indexar catálogo REM por código
rem_por_codigo = {c['codigo']: c for c in catalogo}

# ---------------------------------------------------------------------------
# 2 · Agrupar en series por indicador
# ---------------------------------------------------------------------------
def construir_series(filas, campo_id, campo_nombre):
    series = {}
    for fila in filas:
        cid = fila[campo_id]
        if cid not in series:
            series[cid] = {
                'id': cid,
                'nombre': fila[campo_nombre],
                'tipo': fila.get('tipo',''),
                'meta_umbral': num(fila.get('meta_umbral')),
                'polaridad': fila.get('polaridad','directa'),
                'puntos': []
            }
        series[cid]['puntos'].append({
            'corte': int(fila['corte']) if fila['corte'] else 0,
            'mes': fila['mes'],
            'anio': int(fila['anio']),
            'orden': clave_temporal(fila),
            'valor': num(fila.get('valor_corte')),
            'global': num(fila.get('global')),
            'comuna': num(fila.get('comuna')),
            'numerador': num(fila.get('numerador')),
            'denominador': num(fila.get('denominador')),
            'brecha': num(fila.get('brecha')),
            'estado': fila.get('estado','').strip(),
            'nota': fila.get('nota','').strip(),
        })
    # ordenar puntos temporalmente
    for s in series.values():
        s['puntos'].sort(key=lambda p: p['orden'])
    return series

series_mmss = construir_series(mmss, 'meta', 'indicador')
series_iaaps = construir_series(iaaps, 'indicador', 'nombre')

# ---------------------------------------------------------------------------
# 3 · Cálculos de seguimiento: tendencia, delta, proyección
# ---------------------------------------------------------------------------
def calcular_tendencia(puntos):
    """
    Tendencia sobre los valores no nulos.
    Devuelve dirección (mejora/estable/retroceso), delta último tramo,
    y proyección lineal simple al siguiente corte.
    """
    vals = [(p['orden'], p['valor']) for p in puntos if p['valor'] is not None]
    if len(vals) < 2:
        return {'direccion':'sindato','delta':None,'pendiente':None,'proyeccion':None}

    # delta último tramo
    delta = vals[-1][1] - vals[-2][1]

    # regresión lineal simple (mínimos cuadrados) sobre índice secuencial
    n = len(vals)
    xs = list(range(n))
    ys = [v[1] for v in vals]
    mx = sum(xs)/n
    my = sum(ys)/n
    denom = sum((x-mx)**2 for x in xs)
    pendiente = (sum((xs[i]-mx)*(ys[i]-my) for i in range(n))/denom) if denom else 0
    intercepto = my - pendiente*mx
    proyeccion = pendiente*n + intercepto  # siguiente punto

    if abs(delta) < 0.5:
        direccion = 'estable'
    elif delta > 0:
        direccion = 'mejora'
    else:
        direccion = 'retroceso'

    return {'direccion':direccion,'delta':round(delta,1),
            'pendiente':round(pendiente,2),'proyeccion':round(proyeccion,1)}

for grupo in (series_mmss, series_iaaps):
    for s in grupo.values():
        s['tendencia'] = calcular_tendencia(s['puntos'])
        # adjuntar REM
        s['rem'] = rem_por_codigo.get(s['id'], {})

# ---------------------------------------------------------------------------
# 4 · Empaquetar para el HTML (JSON embebido)
# ---------------------------------------------------------------------------
payload = {
    'generado': datetime.now().strftime('%d-%m-%Y %H:%M'),
    'mmss': list(series_mmss.values()),
    'iaaps': list(series_iaaps.values()),
    'catalogo': catalogo,
}

# lista ordenada de cortes presentes (para eje X)
todos_ordenes = set()
for grupo in (series_mmss, series_iaaps):
    for s in grupo.values():
        for p in s['puntos']:
            todos_ordenes.add((p['orden'], f"{p['mes'][:3].capitalize()} {str(p['anio'])[2:]}"))
payload['eje_tiempo'] = [{'orden':o,'label':l} for o,l in sorted(todos_ordenes)]

print(f"Series MMSS: {len(series_mmss)}")
print(f"Series IAAPS: {len(series_iaaps)}")
print(f"Cortes en eje temporal: {len(payload['eje_tiempo'])}")
print(f"Indicadores en catálogo REM: {len(catalogo)}")

# Guardar payload para el siguiente paso (construcción del HTML)
with open(os.path.join(BASE, '_payload.json'), 'w', encoding='utf-8') as f:
    json.dump(payload, f, ensure_ascii=False, indent=2)
print("\nPayload guardado en _payload.json")

# ---------------------------------------------------------------------------
# 5 · Construir el HTML (invoca la segunda etapa)
# ---------------------------------------------------------------------------
import subprocess
subprocess.run(['python3', os.path.join(BASE,'construir_html.py')], check=True)
print("\n✓ Dashboard actualizado. Abre dashboard.html en el navegador.")
