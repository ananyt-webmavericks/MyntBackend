from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from Campaign_Press.models import CampPressModel
from Campaign_Press.serializers import CampaignPressSerializer
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
            'EMAIL': reverse(CampPressModel.EMAIL, request=request),
            })
        
        
        
@api_view(['GET', 'POST', 'DELETE'])
def CampaignPress_list(request):
    
    # GET list of signup, POST a new user, DELETE all tutori
  if request.method == 'GET':
         
        pproblemdets = CampPressModel.objects.all()
        
        EMAIL = request.GET.get('EMAIL', None)
        if EMAIL is not None:
            pproblemdets = pproblemdets.filter(EMAIL__icontains=EMAIL)
        
        pproblemdets_serializer = CampaignPressSerializer(pproblemdets, many=True)  
        return JsonResponse(pproblemdets_serializer.data, safe=False)
 
  elif request.method == 'POST':
        # html_content = "<p>That's <strong>the HTML part</strong></p>"
        pproblemdets_serializer = CampaignPressSerializer(data=request.data)
        if  pproblemdets_serializer.is_valid():
            pproblemdets_serializer.save()
            return JsonResponse(pproblemdets_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(pproblemdets_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  elif request.method == 'DELETE':
        count = CampPressModel.objects.all().delete()
        return JsonResponse({'message': '{} Pitch Problem is deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def CampaignPress_detail(request, pk):
    try:
        pproblemdets = CampPressModel.objects.get(pk=pk)
    except CampPressModel.DoesNotExist:
        return JsonResponse({'message': 'Pitch Problem does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        print("4")
        pproblemdets_serializer = CampaignPressSerializer(pproblemdets)
        return JsonResponse(pproblemdets_serializer.data)
    
    elif request.method == 'PUT':
       
        # pproblemdets_data = JSONParser().parse(request)
        pproblemdets_serializer = CampaignPressSerializer(pproblemdets, data=request.data)
        
        if  pproblemdets_serializer.is_valid():
            pproblemdets_serializer.save()
            return JsonResponse(pproblemdets_serializer.data)
        return JsonResponse(pproblemdets_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        print("6")
        pproblemdets.delete()
        return JsonResponse({'message': 'Pitch Problem was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
