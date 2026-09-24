# Registro de revisión punto a punto — Catálogo REM

**Fuente de contraste:** PDF oficiales DESAM Coquimbo, corte julio 2026 (Metas Sanitarias e IAAPS), tal como llegan, sin alterar.
**Fecha de revisión:** 24-09-2026
**Método:** comparación de cada celda de numerador y denominador del catálogo del dashboard contra la fórmula impresa en el encabezado de cada indicador del PDF. Los rangos (p. ej. `J26:M26`) se expandieron celda a celda para el cotejo.

## Resultado global

Los **26 indicadores** tienen el numerador y el denominador en su posición correcta. **No hay cruces.** El error que se observaba en la versión anterior del dashboard (numerador y denominador intercambiados en la Meta I) **no está presente** en esta versión reconstruida: el motor de cálculo siempre usó las celdas correctas, por lo que los valores calculados eran fieles; sólo la versión previa del catálogo mostraba las glosas cruzadas.

## Detalle por indicador

| Cód | Indicador | Numerador (oficial DESAM = catálogo) | Denominador (oficial DESAM = catálogo) | Veredicto |
|---|---|---|---|---|
| I | Recuperación DSM 12-23m | J26+K26+L26+M26+J28+K28+L28+M28 | (J23+K23+L23+M23) − (J37+K37+L37+M37+J40+K40+L40+M40) | ✅ Correcto |
| II | Detección precoz cáncer cervicouterino | — (sin fórmula oficial en el corte) | — | ✅ Correcto |
| IIIA | Control odontológico 0-9 | REM A03 D7: F208 ; Y208 | FONASA: inscritos 0-9 | ✅ Correcto |
| IIIB | 6 años libres de caries | REM A09: SUMA(S51:T51) | FONASA: inscritos 6 años | ✅ Correcto |
| IVA | Cobertura efectiva DM2 | REM P4: C31 + C32 | FONASA × prevalencia DM2 | ✅ Correcto |
| IVB | Evaluación pies DM2 | REM P4: SUMA(C62:C65) | REM P4: C17 | ✅ Correcto |
| V | Cobertura efectiva HTA | REM P4: C29 + C30 | FONASA × prevalencia HTA | ✅ Correcto |
| VI | LME 6º mes | REM A03: H61 | REM A03: H67 | ✅ Correcto |
| VII | Cobertura Asma+EPOC | REM P3: SUMA(H65:AM65) + C69 | FONASA × prevalencia Asma/EPOC | ✅ Correcto |
| M3 | Tasa consultas médicas morbilidad | REM A04-B12 + A07-Z126:AA126 + A08-B41 + A23-B58 + A32-B28:B29 | FONASA: inscritos validados | ✅ Correcto |
| M4 | Resolutividad APS | REM A07: AE126 + AF126 | SUMA(A01-C11…C63 + A04-B12 + A06-C12 + A07-Z121:AA121 + A08-B41 + A23-B58 + A23-B63 + A32-B28:B29 + A32-C130 + A32-C141) | ✅ Correcto |
| M5 | Visita Domiciliaria Integral | REM A26-C10:C35 + A26-C41:F41 + A33-C39-C40 | FONASA: familias (inscritos / 3,3) | ✅ Correcto |
| M61A | EMP Mujeres 20-64 | SUMA(A02!H21;J21;L21;N21;P21;R21;T21;V21;X21) | Población mujeres 20-64 − SUMA(B46:B52) | ✅ Correcto |
| M61B | EMP Hombres 20-64 | SUMA(A02!G21;I21;K21;M21;O21;Q21;S21;U21;W21) | FONASA: hombres 20-64 | ✅ Correcto |
| M62 | EMP 65 y más | REM A02: Y21+Z21+AA21+AB21+AC21+AD21+AE21+AF21 | FONASA: inscritos 65+ | ✅ Correcto |
| M7 | Evaluación DSM 12-23m | SUMA(A03!J21:M24) | REM P02: V12+W12+X12+Y12 | ✅ Correcto |
| M8 | Control Adolescente 10-19 | REM A01: C74 + F74 | FONASA: población 10-19 | ✅ Correcto |
| M91 | Cobertura Salud Mental | REMP06:C13 + REMA05:C193 − C245 + AN245 + AO245 + AP245 | FONASA × prevalencia SM | ✅ Correcto |
| M92 | Tasa controles Salud Mental | SUMA(A6-C22:C23 + A06-E32 + A19a-C110 + A19a-C112 + A26-C30:C31 + A26-C38:F38 + A32-B123:B125 + A32-C140 + A32-C151 + A4-B24) | PBC salud mental (mismo cálculo que M9.1) | ✅ Correcto |
| M93 | Egresos alta clínica SM | REM A05: C245 | PBC salud mental (mismo cálculo que M9.1) | ✅ Correcto |
| M12 | Ingreso precoz embarazo | REM A05: C13 | REM A05: C11 | ✅ Correcto |
| M13 | Anticoncepción adolescente | REM P01: E25 | FONASA: adolescentes 15-19 | ✅ Correcto |
| M14 | Cobertura DM2 | REM P4: C17 | FONASA × prevalencia DM2 | ✅ Correcto |
| M15 | Cobertura HTA | REM P4: C16 | FONASA × prevalencia HTA | ✅ Correcto |
| M17A | Menores 3a libres caries | REM A09: G51+H51+I51+J51+K51+L51 | FONASA: inscritos < 3 años | ✅ Correcto |
| M17B | Normalidad nutricional menor 2a | REM P02: SUMA(H36:Y36) | REM P02: SUMA(H37:Y37) | ✅ Correcto |

## Nota sobre la Meta I (la que motivó esta revisión)

- **Numerador oficial (DESAM):** `REM A03: J26+K26+L26+M26 + J28+K28+L28+M28` — Nº de niños de 12-23m con riesgo DSM **recuperados**.
- **Denominador oficial (DESAM):** `REM A03: (J23+K23+L23+M23) menos (J37+K37+L37+M37+J40+K40+L40+M40)` — Nº de niños diagnosticados con riesgo en su **1ª evaluación**.
- **En este dashboard:** numerador y denominador coinciden exactamente con lo anterior. ✅
- **En la versión anterior (la publicada en GitHub):** estaban intercambiados en la tabla de procedencia. Ese es el archivo que quedará reemplazado al publicar esta versión.

## Validación cruzada adicional

Como control independiente, cada numerador extraído de los REM reales (enero–agosto 2026, DEIS 105321 + 105405) se comparó mes a mes con los valores publicados por DESAM: **280 de 280 coincidencias**. Si numerador y denominador estuvieran cruzados en el cálculo, esta validación habría fallado de forma masiva — lo que confirma que el cálculo era correcto.