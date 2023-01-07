from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from MT_Startup_Pitch_Productinfo.models import ProductinfoModel
from MT_Startup_Pitch_Productinfo.serializers import ProductinfoSerializer
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail 
from django.http import HttpResponse 






class ApiRoot(generics.GenericAPIView): 
    parser_classes = (MultiPartParser, FormParser)
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'EMAIL': reverse(ProductinfoModel.EMAIL, request=request),
            })
        
        
        
@api_view(['GET', 'POST', 'DELETE'])
def Productinfo_list(request):
    
    # GET list of signup, POST a new user, DELETE all tutori
  if request.method == 'GET':
         
        productsdets = ProductinfoModel.objects.all() 
        EMAIL = request.GET.get('EMAIL', None)
        if EMAIL is not None:
            productsdets = productsdets.filter(EMAIL__icontains=EMAIL)
        
        productsdets_serializer = ProductinfoSerializer(productsdets, many=True)  
        return JsonResponse(productsdets_serializer.data, safe=False)
 
  elif request.method == 'POST':
        # html_content = "<p>That's <strong>the HTML part</strong></p>"
        productsdets_serializer = ProductinfoSerializer(data=request.data)
        if  productsdets_serializer.is_valid():
            productsdets_serializer.save()
            return JsonResponse(productsdets_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(productsdets_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  elif request.method == 'DELETE':
        count = ProductinfoModel.objects.all().delete()
        return JsonResponse({'message': '{} Pitch Product is deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def Productinfo_detail(request, pk):
    try:
        productsdets = ProductinfoModel.objects.get(pk=pk)
    except ProductinfoModel.DoesNotExist:
        return JsonResponse({'message': 'Pitch Product does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        print("4")
        productsdets_serializer = ProductinfoSerializer(productsdets)
        return JsonResponse(productsdets_serializer.data)
    
    elif request.method == 'PUT':
       
        # productsdets_data = JSONParser().parse(request)
        productsdets_serializer = ProductinfoSerializer(productsdets, data=request.data)
        
        if  productsdets_serializer.is_valid():
            productsdets_serializer.save()
            return JsonResponse(productsdets_serializer.data)
        return JsonResponse(productsdets_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        print("6")
        productsdets.delete()
        return JsonResponse({'message': 'Pitch Product was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
