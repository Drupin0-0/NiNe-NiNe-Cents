import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import UserProfile  # Importa o seu novo modelo de perfil

@csrf_exempt
def home_view(request):
    return render(request, 'home.html')

@csrf_exempt
def userprofile_view(request):
    
    if request.method == 'POST':
        try:
            # Transforma o JSON do Bruno em dicionário Python
            data = json.loads(request.body)
            
            # 1. Cria primeiro o Usuário Base (obrigatório)
            new_user = User.objects.create_user(
                username=data.get('username'),
                password=data.get('password'),
                email=data.get('email', '')
            )
            
            # 2. Cria o Perfil vinculado a esse usuário que acabou de ser criado
            # Nota: Como a foto (picture) envolve envio de arquivos binários, pelo Bruno
            # enviando JSON puro a gente geralmente deixa como None ou lida depois.
            new_profile = UserProfile.objects.create(
                user=new_user,
                birthdate=data.get('birthdate')  # Formato esperado do Bruno: "YYYY-MM-DD"
            )
            
            return JsonResponse({
                'message': 'Usuário e Perfil criados com sucesso!',
                'user_id': new_user.id,
                'profile_id': new_profile.id,
                'username': new_user.username
            }, status=201)
            
        except Exception as e:
            return JsonResponse({'error': f'Dados inválidos ou erro no servidor: {str(e)}'}, status=400)

    elif request.method == 'GET':
        try:
            # Em vez de buscar só o User, buscamos os UserProfiles
            # O select_related('user') serve para o Django trazer os dados do usuário 
            # de uma vez só do banco, deixando a API muito mais rápida!
            profiles = UserProfile.objects.select_related('user').all()
            
            profiles_list = []
            for p in profiles:
                profiles_list.append({
                    'id': p.id,
                    'username': p.user.username,  # Puxando o dado do User associado
                    'email': p.user.email,        # Puxando o dado do User associado
                    'birthdate': p.birthdate.strftime('%Y-%m-%d') if p.birthdate else None,
                    'picture': p.picture.url if p.picture else None, # URL da imagem se houver
                    'created_at': p.created_at.strftime('%Y-%m-%d %H:%M:%S')  # Formata a data/hora bonitinho
                })
                
            return JsonResponse(profiles_list, safe=False, status=200)
            
        except Exception as e:
            return JsonResponse({'error': f'Erro ao buscar perfis: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Método não permitido'}, status=405)