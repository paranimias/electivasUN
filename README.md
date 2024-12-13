# Buscador de electivas UN

Este es un buscador CLI de electivas con cupo en la UNAL sede Bogotá para linux, por el momento sólo busca electivas para
toda la universidad y para la sección de asignaturas sólo busca para la carrera de Ciencias de la Computación

## Requerimientos

**Python**

## Uso

### Clonar el repositorio en la carpeta deseada
```bash
git clone https://github.com/paranimias/electivasUN.git
```

### Crear entorno virtual e instalar paquetes necesarios

```bash
cd electivasUN
python -m venv .venv
./.venv/bin/pip install requests
```

### Ejecutar en el entorno virtual

```bash
./.venv/bin/python buscador_electivas.py
```

### Elegir opción 0 para asignaturas
