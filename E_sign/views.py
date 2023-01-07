from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from E_sign.models import E_SignModel
from E_sign.serializers import ESignSerializer
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
            })
        
        
        
@api_view(['GET', 'POST', 'DELETE'])
def ESign_list(request):
    
    # GET list of signup, POST a new user, DELETE all tutori
  if request.method == 'GET':
         
        raisedets = E_SignModel.objects.all()
        
        EMAIL = request.GET.get('EMAIL', None)
        if EMAIL is not None:
            raisedets = raisedets.filter(EMAIL__icontains=EMAIL)
        
        raise_serializer = ESignSerializer(raisedets, many=True)  
        return JsonResponse(raise_serializer.data, safe=False)
 
  elif request.method == 'POST': 
        raise_serializer = ESignSerializer(data=request.data)
        if  raise_serializer.is_valid():
            raise_serializer.save() 
            return JsonResponse(raise_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(raise_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  elif request.method == 'DELETE':
        count = E_SignModel.objects.all().delete()
        return JsonResponse({'message': '{} E-Sign Document deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def ESign_details(request, pk):
    try:
        raisedets = E_SignModel.objects.get(pk=pk)
    except E_SignModel.DoesNotExist:
        return JsonResponse({'message': 'The E-Sign Document does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        print("4")
        raisedets_serializer = ESignSerializer(raisedets)
        return JsonResponse(raisedets_serializer.data)
    
    elif request.method == 'PUT':
       
        # raisedets_data = JSONParser().parse(request)
        raisedets_serializer = ESignSerializer(raisedets, data=request.data)
        
        if  raisedets_serializer.is_valid():
            raisedets_serializer.save()
            return JsonResponse(raisedets_serializer.data)
        return JsonResponse(raisedets_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        print("6")
        raisedets.delete()
        return JsonResponse({'message': 'E-Sign Document was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
