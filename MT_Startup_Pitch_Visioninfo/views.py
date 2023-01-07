from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from MT_Startup_Pitch_Visioninfo.models import VisioninfoModel
from MT_Startup_Pitch_Visioninfo.serializers import VisioninfoSerializer
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
            'EMAIL': reverse(VisioninfoModel.EMAIL, request=request),
            })
        
        
        
@api_view(['GET', 'POST', 'DELETE'])
def Visioninfo_list(request):
    
    # GET list of signup, POST a new user, DELETE all tutori
  if request.method == 'GET':
         
        visiondets = VisioninfoModel.objects.all()
        
        EMAIL = request.GET.get('EMAIL', None)
        if EMAIL is not None:
            visiondets = visiondets.filter(EMAIL__icontains=EMAIL)
        
        visiondets_serializer = VisioninfoSerializer(visiondets, many=True)  
        return JsonResponse(visiondets_serializer.data, safe=False)
 
  elif request.method == 'POST':
        # html_content = "<p>That's <strong>the HTML part</strong></p>"
        visiondets_serializer = VisioninfoSerializer(data=request.data)
        if  visiondets_serializer.is_valid():
            visiondets_serializer.save()
            return JsonResponse(visiondets_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(visiondets_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  elif request.method == 'DELETE':
        count = VisioninfoModel.objects.all().delete()
        return JsonResponse({'message': '{} Pitch Vision is deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def Visioninfo_detail(request, pk):
    try:
        visiondets = VisioninfoModel.objects.get(pk=pk)
    except VisioninfoModel.DoesNotExist:
        return JsonResponse({'message': 'Pitch Vision does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        print("4")
        visiondets_serializer = VisioninfoSerializer(visiondets)
        return JsonResponse(visiondets_serializer.data)
    
    elif request.method == 'PUT':
       
        # visiondets_data = JSONParser().parse(request)
        visiondets_serializer = VisioninfoSerializer(visiondets, data=request.data)
        
        if  visiondets_serializer.is_valid():
            visiondets_serializer.save()
            return JsonResponse(visiondets_serializer.data)
        return JsonResponse(visiondets_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        print("6")
        visiondets.delete()
        return JsonResponse({'message': 'Pitch Vision was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
