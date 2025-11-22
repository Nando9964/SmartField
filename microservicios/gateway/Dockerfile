# Usa una imagen base de Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# Expon el puerto en el que la aplicación Flask se ejecutará
EXPOSE 5000

# Define el comando para correr la app
CMD ["python", "gateway.py"]