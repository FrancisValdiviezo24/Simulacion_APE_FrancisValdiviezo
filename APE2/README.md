# APE 2 - Comparación de modelos de crecimiento poblacional

## 1. Descripción del proyecto

Este proyecto compara cuatro modelos de crecimiento poblacional utilizando los datos entregados en la guía:

```text
[1000, 1100, 1250, 1400, 1600, 1850, 2100]
```

Los modelos implementados son:

- Determinístico: calcula el crecimiento exponencial.
- Discreto: actualiza la población por períodos completos.
- Estocástico: agrega ruido aleatorio al crecimiento.
- Continuo: utiliza el método de Euler con pasos pequeños.

El programa muestra una tabla comparativa y genera dos gráficas para analizar los resultados.

## 2. Tecnologías utilizadas

- Python 3
- NumPy
- Matplotlib

## 3. Instalación

Primero se debe descargar o clonar el repositorio:

```bash
git clone https://github.com/FrancisValdiviezo24/Simulacion_APE_FrancisValdiviezo.git
cd Simulacion_APE_FrancisValdiviezo/APE2
```

### Windows con PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
```

Si PowerShell no permite activar el entorno, se puede ejecutar una vez:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
```

### Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

## 4. Uso

### Windows

```powershell
py main.py
```

### Linux

```bash
python3 main.py
```

La ejecución muestra una tabla con los datos y los resultados de cada modelo. También crea los archivos:

- `comparacion_modelos.png`
- `influencia_tasa.png`

## 5. Configuración

Los datos y parámetros principales se encuentran al inicio de `main.py`:

```python
datos = [1000, 1100, 1250, 1400, 1600, 1850, 2100]
tasa = 0.12
sigma = 50
paso = 0.1
```

- `tasa`: controla el crecimiento o decrecimiento.
- `sigma`: controla la cantidad de ruido del modelo estocástico.
- `paso`: define el tamaño del paso utilizado por Euler.

## 6. Estructura del proyecto

```text
APE2/
├── controller/
│   ├── continuo.py
│   ├── deterministico.py
│   ├── discreto.py
│   ├── estocastico.py
│   └── simulacion.py
├── models/
│   └── resultado.py
├── vista/
│   └── simulacion_vista.py
├── main.py
├── requirements.txt
└── README.md
```

- `controller`: contiene los cálculos de los cuatro modelos y coordina la simulación.
- `models`: guarda los resultados obtenidos.
- `vista`: muestra la tabla y genera las gráficas.
- `main.py`: contiene los datos, configura los parámetros y ejecuta el programa.

## 7. Información adicional

El modelo estocástico utiliza una semilla fija para obtener los mismos resultados en cada ejecución. Esto permite comparar las salidas en Windows y Linux.

Para salir del entorno virtual se utiliza el siguiente comando tanto en Windows como en Linux:

```bash
deactivate
```
