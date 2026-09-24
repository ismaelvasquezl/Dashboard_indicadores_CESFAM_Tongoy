# Dashboard de Indicadores · CESFAM Tongoy
### Metas Sanitarias (Ley 19.813) e IAAPS (COMGES 1.12)

Sistema que calcula los indicadores **directamente desde los REM** (Registros
Estadísticos Mensuales) del establecimiento y del per cápita FONASA, replicando
el método de corte de DESAM Coquimbo. Consolida **CESFAM Tongoy (105321)** +
**P.S.R. Guanaqueros (105405)**.

---

## 1. Qué necesita instalado (una sola vez)

- **Python 3** — descárguelo de https://www.python.org
  Durante la instalación, **marque la casilla "Add Python to PATH"**.
- La librería `openpyxl` se instala sola la primera vez que corre el `.bat`.

No necesita internet, ni servidor, ni cuenta. Todo ocurre en su computador.

---

## 2. Actualización mensual (el uso normal)

**Paso 1.** Dentro de la carpeta del sistema hay una carpeta llamada `REM_2026`.
Deje ahí los REM del mes, tal como los descarga, sin renombrar:

```
REM_2026/
├── 105321A01.xlsm  … 105321A08.xlsm   (Serie A, Tongoy, un archivo por mes)
├── 105405A01.xlsm  … 105405A08.xlsm   (Serie A, Guanaqueros)
├── 105321P06.xlsm  y  105405P06.xlsm  (Serie P, censo de junio)
└── Percapita_Tongoy_2026.xlsx         (per cápita FONASA del año)
```
Puede tener los REM en subcarpetas (ej. `Tongoy 105321/`); el sistema los
encuentra igual.

**Paso 2.** Doble clic en **`ACTUALIZAR.bat`**.
El sistema lee los archivos, verifica cada celda, calcula todos los indicadores
y abre el dashboard.

**Paso 3.** Antes de publicar, revise la pestaña **VALIDACIÓN** del dashboard:
- que los archivos leídos sean los correctos,
- que no haya alertas en rojo,
- que las diferencias con DESAM (si las hay) tengan explicación.

Eso es todo. No se transcribe ninguna cifra a mano.

---

## 3. Publicar en la web (GitHub Pages)

El `.bat` deja una copia lista llamada **`index.html`**. Súbala a su
repositorio (junto a `presentacion_dashboard.html` si quiere actualizar también
la presentación). La página queda en:
`https://ismaelvasquezl.github.io/Dashboard_indicadores_CESFAM_Tongoy/`

---

## 4. Cambio de año (una vez al año)

Los REM cambian de formato entre años y las filas se mueven. Para que el sistema
siga encontrando cada dato:

**Paso 1.** Cree una carpeta `REM_2027` (con el año que corresponda) y deje ahí
los REM del año nuevo.

**Paso 2.** Doble clic en **`MAPEAR_NUEVO_ANIO.bat`**. Escriba el año nuevo
(2027) y el año base a comparar (2026).

**Paso 3.** El sistema busca cada dato por su **etiqueta de fila** (no por su
posición) y le muestra un informe:
- `SIN_CAMBIO` — la fila sigue en el mismo lugar.
- `PROPUESTO` — la fila se movió; el sistema propone la nueva posición.
- `NO_ENCONTRADA` — la etiqueta cambió; hay que revisarla a mano.

Nada se aplica solo. Usted revisa y confirma.

**Paso 4.** Si cambian las **metas** del año, edítelas en
`config/indicadores_2026.json` (cree la versión del año nuevo). Están marcadas
como valores editables.

---

## 5. Cómo se calcula cada indicador

Cada indicador se calcula así:

- **Numerador y denominador** salen de las celdas REM exactas (ver pestaña
  CATÁLOGO REM del dashboard, con la fórmula y la fila de origen de cada dato).
- **Cumplimiento al corte** replica el método DESAM: la meta anual se prorratea
  al mes de corte y se compara con lo realizado acumulado, con tope en 100%.
- **Estado**: cumple ≥ 90% al corte · bajo meta 60–89,9% · crítico < 60%.
  (Editable en `config/indicadores_2026.json`.)

Los indicadores de cobertura crónica (DM2, HTA, Asma+EPOC) usan denominador por
**prevalencia FONASA** (tramos etarios del per cápita). Los de salud mental usan
la población bajo control del censo P6 más el movimiento del mes.

**Dos casos que conviene saber:**
- DESAM informa algunos indicadores (LME, ingreso de embarazo) **solo con
  Tongoy**. Este sistema los **consolida** con Guanaqueros, así que pueden diferir
  levemente de la cifra comunal. La pestaña VALIDACIÓN lo explica caso por caso.
- La **Meta II** (cáncer cervicouterino) aparece como *pendiente*: los cortes
  DESAM recibidos no traen su fórmula oficial.

---

## 6. Estructura de archivos

```
Dashboard_Tongoy/
├── ACTUALIZAR.bat              ← doble clic cada mes
├── MAPEAR_NUEVO_ANIO.bat       ← doble clic al cambiar de año
├── dashboard.html              ← el tablero (se regenera solo)
├── index.html                  ← copia para publicar en la web
├── presentacion_dashboard.html ← presentación del proyecto
├── REM_2026/                   ← deje aquí los REM y el per cápita
├── config/                     ← metas, prevalencias, mapa de celdas (editable)
│   ├── indicadores_2026.json
│   ├── mapa_rem_2026.json
│   └── ...
├── datos/                      ← resultados y registros (se regeneran)
│   ├── validacion.json
│   ├── REGISTRO_REVISION_CATALOGO_REM.md
│   └── ...
└── (scripts .py)               ← el motor; no hace falta tocarlos
```

---

## 7. Si algo sale mal

- **"No se encontró Python"** → instálelo y marque "Add Python to PATH".
- **"No existe la carpeta REM_2026"** → créela junto al `.bat` y deje ahí los REM.
- **"Falta 105405A08.xlsm"** → falta un REM de un mes; agréguelo a la carpeta.
- **Un archivo con el contenido que no coincide con su nombre** → revise que no
  haya guardado, por ejemplo, el REM de julio con el nombre de agosto.
- El contenedor de cálculo es su propio PC: si borra un script, vuelva a
  descomprimir el paquete original.

---

*Sistema desarrollado por la Unidad de Bioestadística · CESFAM Tongoy · 2026.
Datos oficiales DESAM Coquimbo; el sistema aporta el ordenamiento, el cálculo
reproducible y la trazabilidad REM.*
