import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product

@csrf_exempt
def product_register(request):
   
    if request.method == 'POST':
        try:
           
            data = json.loads(request.body)
            
           
            product = Product.objects.create(
                code=data.get('code'),
                name=data.get('name'),
                description=data.get('description', ''),
                qtt=data.get('qtt'),
                unity=data.get('unity'),
                price=data.get('price')
            )
            
            return JsonResponse({
                'message': 'Produto criado com sucesso!',
                'id': product.id
            }, status=201)
            
        except Exception as e:
            return JsonResponse({'error': f'Dados inválidos ou erro no servidor: {str(e)}'}, status=400)

   
    elif request.method == 'GET':
        
        products = Product.objects.all()
        
      
        products_list = []
        for p in products:
            products_list.append({
                'id': p.id,
                'code': p.code,
                'name': p.name,
                'description': p.description,
                'qtt': p.qtt,
                'unity': p.unity,
                'price': float(p.price) # Decimal precisa virar float ou string no JSON
            })
            
        # safe=False é necessário quando enviamos uma LISTA via JsonResponse
        return JsonResponse(products_list, safe=False, status=200)

    return JsonResponse({'error': 'Método não permitido'}, status=405)