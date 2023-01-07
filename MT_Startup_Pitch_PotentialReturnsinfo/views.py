from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from MT_Startup_Pitch_PotentialReturnsinfo.models import PotentialReturnsinfoModel
from MT_Startup_Pitch_PotentialReturnsinfo.serializers import PotentialReturnsinfoSerializer
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
            'EMAIL': reverse(PotentialReturnsinfoModel.EMAIL, request=request),
            })
        
        
        
@api_view(['GET', 'POST', 'DELETE'])
def PotentialReturnsinfo_list(request):
    
    # GET list of signup, POST a new user, DELETE all tutori
  if request.method == 'GET':
         
        potentialdets = PotentialReturnsinfoModel.objects.all()
        
        EMAIL = request.GET.get('EMAIL', None)
        if EMAIL is not None:
            potentialdets = potentialdets.filter(EMAIL__icontains=EMAIL)
        
        potentialdets_serializer = PotentialReturnsinfoSerializer(potentialdets, many=True)  
        return JsonResponse(potentialdets_serializer.data, safe=False)
 
  elif request.method == 'POST':
        # html_content = "<p>That's <strong>the HTML part</strong></p>"
        potentialdets_serializer = PotentialReturnsinfoSerializer(data=request.data)
        if  potentialdets_serializer.is_valid():
            potentialdets_serializer.save()
            return JsonResponse(potentialdets_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(potentialdets_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  elif request.method == 'DELETE':
        count = PotentialReturnsinfoModel.objects.all().delete()
        return JsonResponse({'message': '{} Pitch Problem is deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def PotentialReturnsinfo_detail(request, pk):
    try:
        potentialdets = PotentialReturnsinfoModel.objects.get(pk=pk)
    except PotentialReturnsinfoModel.DoesNotExist:
        return JsonResponse({'message': 'Pitch Problem does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        print("4")
        potentialdets_serializer = PotentialReturnsinfoSerializer(potentialdets)
        return JsonResponse(potentialdets_serializer.data)
    
    elif request.method == 'PUT':
       
        # potentialdets_data = JSONParser().parse(request)
        potentialdets_serializer = PotentialReturnsinfoSerializer(potentialdets, data=request.data)
        
        if  potentialdets_serializer.is_valid():
            potentialdets_serializer.save()
            return JsonResponse(potentialdets_serializer.data)
        return JsonResponse(potentialdets_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        print("6")
        potentialdets.delete()
        return JsonResponse({'message': 'Pitch Problem was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
