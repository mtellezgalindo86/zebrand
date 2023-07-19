#
from django.shortcuts import render

def profile_view(request):
    # Lógica de la vista
    token = request.user.auth_token.key

    context = {
        'user': request.user,
        'token': token
    }

    return render(request, 'profile.html', context)
#