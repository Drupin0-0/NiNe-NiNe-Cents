import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import UserProfile  

@csrf_exempt
def home_view(request):
    return render(request, 'home.html')

@csrf_exempt
def userprofile_view(request):
    
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            new_user = User.objects.create_user(
                username=data.get('username'),
                password=data.get('password'),
                email=data.get('email', '')
            )
            
            
            new_profile = UserProfile.objects.create(
                user=new_user,
                birthdate=data.get('birthdate')  
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
           
            profiles = UserProfile.objects.select_related('user').all()
            
            profiles_list = []
            for p in profiles:
                profiles_list.append({
                    'id': p.id,
                    'username': p.user.username,  
                    'email': p.user.email,        
                    'birthdate': p.birthdate.strftime('%Y-%m-%d') if p.birthdate else None,
                    'picture': p.picture.url if p.picture else None, 
                    'created_at': p.created_at.strftime('%Y-%m-%d %H:%M:%S')  
                })
                
            return JsonResponse(profiles_list, safe=False, status=200)
            
        except Exception as e:
            return JsonResponse({'error': f'Erro ao buscar perfis: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Método não permitido'}, status=405)