
# Zebrand  

**Zebrand** es una aplicación diseñada para administrar productos. Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los productos.  
  
# **Requisitos previos**  
Asegúrate de tener Docker instalado en tu máquina antes de continuar.  
  
**Docker**  
Instalación y ejecución con Docker  

Clona este repositorio en tu máquina local:  

    git clone https://github.com/mtellezgalindo86/zebrand.git 

Accede al directorio del proyecto:  
cd zebrand  

Construye la imagen de Docker utilizando el archivo Dockerfile:  

    docker build -t zebrand .  


Ejecuta un contenedor utilizando la imagen recién creada:  

    docker run -p 8000:8000 zebrand  

La aplicación estará disponible en [http://localhost:8000/.](http://localhost:8000/)  

**Autenticación**  
Para autenticarte en la API, envía una solicitud POST a [http://localhost:8000/api-auth/login/](http://localhost:8000/api-auth/login/) con las siguientes credenciales:  
  

    Usuario: admin  
    Contraseña: admin  

Recibirás un token de autenticación en la respuesta.  
  
**Acceder a los endpoints**  
Utiliza el token de autenticación en el encabezado Authorization de tus solicitudes a los endpoints protegidos. Puedes encontrar una lista de los endpoints disponibles y su documentación en [http://localhost:8000/swagger/](http://localhost:8000/swagger/) o [http://localhost:8000/redoc/](http://localhost:8000/redoc/).

  



