# Usa una imagen base de Python
FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    libmariadb-dev gcc && \
    apt-get clean

# Instalar el paquete mariadb para Python
RUN pip install mariadb
# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requisitos y los instala
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de la aplicación
COPY app/ .

# Expone el puerto 5000
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]