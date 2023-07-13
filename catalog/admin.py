from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from rest_framework.authtoken.models import Token
from .models import User


class UserAdmin(BaseUserAdmin):
    # ... Definir tus configuraciones personalizadas para la clase de administración de usuarios

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if change:
            # Si se está editando un usuario existente, no se genera un nuevo token
            return

        # Generar un token de autenticación para el nuevo usuario
        Token.objects.create(user=obj)


admin.site.register(User, UserAdmin)
