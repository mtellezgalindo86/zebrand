# Usamos una imagen base de Python
FROM python:3.9

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los archivos de requerimientos y los instalamos
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiamos el código fuente de la aplicación al contenedor
COPY . .

# Exponemos el puerto que usará la aplicación
EXPOSE 8000

RUN python manage.py migrate
RUN echo "from django.contrib.auth import get_user_model; User = get_user_model(); user = User.objects.create_superuser('admin', 'admin@example.com', 'admin'); from rest_framework.authtoken.models import Token; Token.objects.create(user=user)" | python manage.py shell

# Ejecutamos el comando para iniciar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
