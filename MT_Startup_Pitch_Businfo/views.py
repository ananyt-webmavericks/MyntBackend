from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
 
from MT_Startup_Pitch_Businfo.models import BusinfoModel
from MT_Startup_Pitch_Businfo.serializers import BusinfoSerializer
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
            'EMAIL': reverse(BusinfoModel.EMAIL, request=request),
            })
        
        
        
@api_view(['GET', 'POST', 'DELETE'])
def Businessinfo_list(request):
    
    # GET list of signup, POST a new user, DELETE all tutori
  if request.method == 'GET':
         
        businessdets = BusinfoModel.objects.all()
        
        EMAIL = request.GET.get('EMAIL', None)
        if EMAIL is not None:
            businessdets = businessdets.filter(EMAIL__icontains=EMAIL)
        
        businessdets_serializer = BusinfoSerializer(businessdets, many=True)  
        return JsonResponse(businessdets_serializer.data, safe=False)
 
  elif request.method == 'POST':
        # html_content = "<p>That's <strong>the HTML part</strong></p>"
        businessdets_serializer = BusinfoSerializer(data=request.data)
        if  businessdets_serializer.is_valid():
            businessdets_serializer.save()
            return JsonResponse(businessdets_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(businessdets_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  elif request.method == 'DELETE':
        count = BusinfoModel.objects.all().delete()
        return JsonResponse({'message': '{} Pitch Business Model is deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def Businessinfo_detail(request, pk):
    try:
        businessdets = BusinfoModel.objects.get(pk=pk)
    except BusinfoModel.DoesNotExist:
        return JsonResponse({'message': 'Pitch Business Model does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        print("4")
        businessdets_serializer = BusinfoSerializer(businessdets)
        return JsonResponse(businessdets_serializer.data)
    
    elif request.method == 'PUT':
       
        # businessdets_data = JSONParser().parse(request)
        businessdets_serializer = BusinfoSerializer(businessdets, data=request.data)
        
        if  businessdets_serializer.is_valid():
            businessdets_serializer.save()
            return JsonResponse(businessdets_serializer.data)
        return JsonResponse(businessdets_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        print("6")
        businessdets.delete()
        return JsonResponse({'message': 'Pitch Business Model was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
