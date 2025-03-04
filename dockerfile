# Etapa 1: Construcción
FROM continuumio/miniconda3 AS builder

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de configuración de Poetry
COPY pyproject.toml poetry.lock ./

# Instalar Poetry
RUN pip install poetry

# Desactivar la creación de entornos virtuales por parte de Poetry
RUN poetry config virtualenvs.create false

# Instalar las dependencias del proyecto
RUN poetry install --no-dev

# Copiar el código fuente del proyecto
COPY . .

# Etapa 2: Imagen final
FROM continuumio/miniconda3

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el entorno Conda desde la etapa de construcción
COPY --from=builder /opt/conda /opt/conda

# Copiar el código fuente del proyecto desde la etapa de construcción
COPY --from=builder /app /app

# Establecer la variable de entorno PATH
ENV PATH=/opt/conda/bin:$PATH

# Comando por defecto al ejecutar el contenedor
CMD ["python", "src/main.py"]
