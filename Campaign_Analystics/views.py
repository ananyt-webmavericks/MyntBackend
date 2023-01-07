from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from Campaign_Analystics.models import CampaignAnalyticsModel
from Campaign_Analystics.serializers import CamAnalyticsSerializer
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
            'EMAIL': reverse(CampaignAnalyticsModel.EMAIL, request=request),
            })
        
        
        
@api_view(['GET', 'POST', 'DELETE'])
def CampAnalytics_list(request):
    
    # GET list of signup, POST a new user, DELETE all tutori
  if request.method == 'GET':
         
        campAnalyticsdets = CampaignAnalyticsModel.objects.all()
        
        EMAIL = request.GET.get('EMAIL', None)
        if EMAIL is not None:
            campAnalyticsdets = campAnalyticsdets.filter(EMAIL__icontains=EMAIL)
        
        campAnalyticsdets_serializer = CamAnalyticsSerializer(campAnalyticsdets, many=True)  
        return JsonResponse(campAnalyticsdets_serializer.data, safe=False)
 
  elif request.method == 'POST':
        # html_content = "<p>That's <strong>the HTML part</strong></p>"
        campAnalyticsdets_serializer = CamAnalyticsSerializer(data=request.data)
        if  campAnalyticsdets_serializer.is_valid():
            campAnalyticsdets_serializer.save()
            return JsonResponse(campAnalyticsdets_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(campAnalyticsdets_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  elif request.method == 'DELETE':
        count = CampaignAnalyticsModel.objects.all().delete()
        return JsonResponse({'message': '{} Campaign Analytics is deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def CampAnalytics_detail(request, pk):
    try:
        campAnalyticsdets = CampaignAnalyticsModel.objects.get(pk=pk)
    except CampaignAnalyticsModel.DoesNotExist:
        return JsonResponse({'message': 'Campaign Analytics does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        print("4")
        campAnalyticsdets_serializer = CamAnalyticsSerializer(campAnalyticsdets)
        return JsonResponse(campAnalyticsdets_serializer.data)
    
    elif request.method == 'PUT':
       
        # campAnalyticsdets_data = JSONParser().parse(request)
        campAnalyticsdets_serializer = CamAnalyticsSerializer(campAnalyticsdets, data=request.data)
        
        if  campAnalyticsdets_serializer.is_valid():
            campAnalyticsdets_serializer.save()
            return JsonResponse(campAnalyticsdets_serializer.data)
        return JsonResponse(campAnalyticsdets_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        print("6")
        campAnalyticsdets.delete()
        return JsonResponse({'message': 'Campaign Analytics was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
