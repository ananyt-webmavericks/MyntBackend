from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from MT_Startup_Pitch_Customerinfo.models import CustomerinfoModel
from MT_Startup_Pitch_Customerinfo.serializers import CustomerinfoSerializer
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
            'EMAIL': reverse(CustomerinfoModel.EMAIL, request=request),
            })
        
        
        
@api_view(['GET', 'POST', 'DELETE'])
def Customerinfo_list(request):
    
    # GET list of signup, POST a new user, DELETE all tutori
  if request.method == 'GET':
         
        customerdets = CustomerinfoModel.objects.all()
        
        EMAIL = request.GET.get('EMAIL', None)
        if EMAIL is not None:
            customerdets = customerdets.filter(EMAIL__icontains=EMAIL)
        
        customerdets_serializer = CustomerinfoSerializer(customerdets, many=True)  
        return JsonResponse(customerdets_serializer.data, safe=False)
 
  elif request.method == 'POST':
        # html_content = "<p>That's <strong>the HTML part</strong></p>"
        customerdets_serializer = CustomerinfoSerializer(data=request.data)
        if  customerdets_serializer.is_valid():
            customerdets_serializer.save()
            return JsonResponse(customerdets_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(customerdets_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  elif request.method == 'DELETE':
        count = CustomerinfoModel.objects.all().delete()
        return JsonResponse({'message': '{} Pitch Problem is deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def Customerinfo_detail(request, pk):
    try:
        customerdets = CustomerinfoModel.objects.get(pk=pk)
    except CustomerinfoModel.DoesNotExist:
        return JsonResponse({'message': 'Pitch Problem does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        print("4")
        customerdets_serializer = CustomerinfoSerializer(customerdets)
        return JsonResponse(customerdets_serializer.data)
    
    elif request.method == 'PUT':
       
        # customerdets_data = JSONParser().parse(request)
        customerdets_serializer = CustomerinfoSerializer(customerdets, data=request.data)
        
        if  customerdets_serializer.is_valid():
            customerdets_serializer.save()
            return JsonResponse(customerdets_serializer.data)
        return JsonResponse(customerdets_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        print("6")
        customerdets.delete()
        return JsonResponse({'message': 'Pitch Problem was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
