# Imagen base optimizada
FROM jupyter/scipy-notebook:python-3.11

# Cambiar a root para instalar dependencias del sistema
USER root

# Instalar cliente PostgreSQL y utilidades
RUN apt-get update && apt-get install -y \
    postgresql-client \
    vim \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Volver al usuario por defecto de Jupyter
USER ${NB_UID}

# Copiar requirements
COPY requirements.txt /tmp/requirements.txt

# Instalar dependencias Python
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Configurar directorio de trabajo
WORKDIR /home/jovyan/work

# Exponer puerto
EXPOSE 8888
