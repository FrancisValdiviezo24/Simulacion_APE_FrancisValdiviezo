# APE 1 - Modelo de posibilidad de lluvia

## 1. Descripción del proyecto

Este proyecto implementa un modelo matemático para calcular la posibilidad de lluvia según la humedad, la nubosidad y la temperatura registradas durante el día.

El modelo base utiliza la fórmula:

```text
I = 0.5H + 0.3N + 0.2Tf
```

También se incluye un modelo ajustado que da mayor importancia a la nubosidad:

```text
I = 0.45H + 0.4N + 0.15Tf
```

El programa muestra los resultados en tablas, clasifica la posibilidad de lluvia y genera una gráfica comparativa.

## 2. Tecnologías utilizadas

- Python 3
- Matplotlib

## 3. Instalación

Primero se debe descargar o clonar el repositorio:

```bash
git clone https://github.com/FrancisValdiviezo24/Simulacion_APE_FrancisValdiviezo.git
cd Simulacion_APE_FrancisValdiviezo/APE1
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

La ejecución muestra en consola las tablas del modelo base y del modelo ajustado. También crea el archivo `grafica_lluvia.png` dentro de la carpeta `APE1`.

## 5. Configuración

Los datos de humedad, nubosidad y temperatura se encuentran en la lista `datos` de `main.py`. Se pueden cambiar esos valores para probar otras condiciones climáticas.

## 6. Estructura del proyecto

```text
APE1/
├── controlador/
│   ├── calcular_indice.py
│   ├── calcular_temperatura.py
│   ├── clasificacion.py
│   ├── normalizar.py
│   └── procesamiento.py
├── modelos/
│   ├── clima.py
│   └── resultado.py
├── vista/
│   └── climaVista.py
├── main.py
├── requirements.txt
└── README.md
```

- `controlador`: realiza los cálculos y procesa los datos.
- `modelos`: contiene los datos del clima y sus resultados.
- `vista`: muestra las tablas y genera la gráfica.
- `main.py`: contiene los datos y ejecuta el programa.

## 7. Información adicional

El programa clasifica cada índice en uno de estos estados:

- Sin lluvia
- Baja posibilidad
- Lluvia probable
- Lluvia

Para salir del entorno virtual se utiliza el siguiente comando tanto en Windows como en Linux:

```bash
deactivate
```
