from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from Campaign_Banner.models import CampaignBannerModel
from Campaign_Banner.serializers import CampaignBannerSerializer
from rest_framework.decorators import api_view 
from rest_framework.parsers import MultiPartParser, FormParser
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail 
from django.http import HttpResponse 
from Campaign_Investors.models import CamInvestorModel
from Campaign_Press.models import CampPressModel
from Campaign_FAQs.models import CamFAQsModel




class ApiRoot(generics.GenericAPIView): 
    parser_classes = (MultiPartParser, FormParser)
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'EMAIL': reverse(CampaignBannerModel.EMAIL, request=request),
            })
        
        
        
@api_view(['GET', 'POST', 'DELETE'])
def CamBan_list(request):
    
    # GET list of signup, POST a new user, DELETE all tutori
  if request.method == 'GET':
         
        campbandets = CampaignBannerModel.objects.all()
        
        EMAIL = request.GET.get('EMAIL', None)
        if EMAIL is not None:
            campbandets = campbandets.filter(EMAIL__icontains=EMAIL)
        
        campbandets_serializer = CampaignBannerSerializer(campbandets, many=True)  
        return JsonResponse(campbandets_serializer.data, safe=False)
 
  elif request.method == 'POST':
        # html_content = "<p>That's <strong>the HTML part</strong></p>"
        campbandets_serializer = CampaignBannerSerializer(data=request.data)
        if  campbandets_serializer.is_valid():
            campbandets_serializer.save()
            return JsonResponse(campbandets_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(campbandets_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  elif request.method == 'DELETE':
        count = CampaignBannerModel.objects.all().delete()
        return JsonResponse({'message': '{} Campaign Banner is deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def CamBan_detail(request, pk):
    try:
        campbandets = CampaignBannerModel.objects.get(pk=pk)
    except CampaignBannerModel.DoesNotExist:
        return JsonResponse({'message': 'Campaign Banner does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        print("4")
        campbandets_serializer = CampaignBannerSerializer(campbandets)
        return JsonResponse(campbandets_serializer.data)
    
    elif request.method == 'PUT':
       
        # campbandets_data = JSONParser().parse(request)
        campbandets_serializer = CampaignBannerSerializer(campbandets, data=request.data)
        
        if  campbandets_serializer.is_valid():
            campbandets_serializer.save()
            return JsonResponse(campbandets_serializer.data)
        return JsonResponse(campbandets_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        print("6")
        campbandets.delete()
        return JsonResponse({'message': 'Campaign Banner was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)




 
@api_view(['GET', 'PUT', 'DELETE'])
def CamDelete(request): 
    MODULE = request.GET.get('MODULE', None)
    print(MODULE)
    if MODULE is not None:
        campbandets = campbandets.filter(MODULE__icontains=MODULE)
    try:
        campbandets = CampaignBannerModel.objects.get(MODULE=id)
        campinvest = CamInvestorModel.objects.get(MODULE=id)
        camppress = CampPressModel.objects.get(MODULE=id)
        campfaqs = CamFAQsModel.objects.get(MODULE=id)
    except CampaignBannerModel.DoesNotExist:
        return JsonResponse({'message': 'Campaign does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE': 
        campbandets.delete()
        campinvest.delete()
        camppress.delete()
        campfaqs.delete()
        return JsonResponse({'message': 'All Campaign was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)