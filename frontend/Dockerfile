# Usa la imagen oficial de Node.js
FROM node:18

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos package.json y package-lock.json
COPY package*.json ./

# Instala las dependencias
RUN npm install

# Copia todos los archivos
COPY . .

# Construye la aplicación para producción
RUN npm run build

# Expón el puerto 5173
EXPOSE 5173

# Comando para correr la aplicación
CMD ["npm", "run", "dev"]
