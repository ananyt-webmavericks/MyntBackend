from django.shortcuts import render
from django.http.response import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from Campaign_Investors.models import CamInvestorModel
from Campaign_Investors.serializers import CamInvestorSerializer
from rest_framework.decorators import api_view
from Campaign_Investors.models import CamInvestorModel
from rest_framework.parsers import MultiPartParser, FormParser

from Campaign_Banner.models import CampaignBannerModel
from Campaign_Press.models import CampPressModel
from Campaign_FAQs.models import CamFAQsModel
from Campaign_Banner.serializers import CampaignBannerSerializer
from Campaign_Press.serializers import CampaignPressSerializer
from Campaign_FAQs.serializers import CamFAQsSerializer
from MT_Startup_Companyinfo.models import CompanyinfoModel
from MT_Startup_Companyinfo.serializers import CompanyinfoSerializer
from Campaign_Analystics.models import CampaignAnalyticsModel
from Campaign_Analystics.serializers import CamAnalyticsSerializer
from MT_Startup_Teaminfo.models import TeaminfoModel
from MT_Startup_Teaminfo.serializers import TeaminfoSerializer


class ApiRoot(generics.GenericAPIView): 
    parser_classes = (MultiPartParser, FormParser)
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'EMAIL': reverse(CamInvestorModel.EMAIL, request=request),
              })
        
        
        
@api_view(['GET', 'POST', 'DELETE'])
def CampInvestor_list(request):
    
    # GET list of signup, POST a new user, DELETE all tutori
  if request.method == 'GET':
       
        campinvest = CamInvestorModel.objects.all()
        EMAIL = request.GET.get('EMAIL', None)
         
        if  EMAIL is not None:
            campinvest = campinvest.filter( EMAIL__icontains= EMAIL)
        CampInvestor_serializer = CamInvestorSerializer(campinvest, many=True)
        print("1",CampInvestor_serializer.data)
        return JsonResponse(CampInvestor_serializer.data, safe=False)
    
    
  elif request.method == 'POST':
        print(request.data)
        CampInvestor_serializer = CamInvestorSerializer(data=request.data) 
        if  CampInvestor_serializer.is_valid():
            print(CampInvestor_serializer)
            CampInvestor_serializer.save()
            return Response(CampInvestor_serializer.data, status=status.HTTP_201_CREATED)
        return Response(CampInvestor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  
  elif request.method == 'DELETE':
        print("3")
        count = CamInvestorModel.objects.all().delete()
        return JsonResponse({'message': '{} Campaign Investor were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def CampInvestor_detail(request, pk):
    try:
        campinvest = CamInvestorModel.objects.get(pk=pk)
    except CamInvestorModel.DoesNotExist:
        return JsonResponse({'message': 'The Campaign Investor does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        print("4")
        CampInvestor_serializer = CamInvestorSerializer(campinvest)
        return JsonResponse(CampInvestor_serializer.data)
    
    elif request.method == 'PUT':
        print("5")
        # CampInvestor_data = JSONParser().parse(request)
        CampInvestor_serializer = CamInvestorSerializer(campinvest, data=request.data)
        
        if  CampInvestor_serializer.is_valid():
            CampInvestor_serializer.save()
            return JsonResponse(CampInvestor_serializer.data)
        return JsonResponse(CampInvestor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        print("6")
        campinvest.delete()
        return JsonResponse({'message': 'Campaign Investor was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

# from Campaign_Banner.serializers import CampaignBannerSerializer
# from Campaign_Press.serializers import CampaignPressSerializer
# from Campaign_FAQs.serializers import CamFAQsSerializer
from itertools import chain
@api_view(['GET', 'PUT', 'DELETE'])
def CampaignAll_list(request):
    
    # GET list of signup, POST a new user, DELETE all tutori
  if request.method == 'GET': 
        caminfo =  CompanyinfoModel.objects.all()
        teaminfo = TeaminfoModel.objects.all()
        campinvest = CamInvestorModel.objects.all()
        campban = CampaignBannerModel.objects.all()
        camppress = CampPressModel.objects.all()
        campfaqs = CamFAQsModel.objects.all()
        campAnalystics =CampaignAnalyticsModel.objects.all()
        
        
        EMAIL = request.GET.get('EMAIL', None)
         
        if  EMAIL is not None:
            caminfo = caminfo.filter(EMAIL__icontains= EMAIL)
            campinvest = campinvest.filter( EMAIL__icontains= EMAIL)
            campban = campban.filter( EMAIL__icontains= EMAIL)
            camppress = camppress.filter( EMAIL__icontains= EMAIL)
            campfaqs = campfaqs.filter( EMAIL__icontains= EMAIL)
            campAnalystics = campAnalystics.filter( EMAIL__icontains= EMAIL)
            teaminfo = teaminfo.filter( EMAIL__icontains= EMAIL)
            
            
        Company_info_Serializer = CompanyinfoSerializer(caminfo, many=True)
        CampInvestor_serializer = CamInvestorSerializer(campinvest, many=True)
        Campbanner_serializer = CampaignBannerSerializer(campban, many=True)
        CampPress_serializer = CampaignPressSerializer(camppress, many=True)
        CampFAQs_serializer = CamFAQsSerializer(campfaqs, many=True)
        Cam_Analytics_Serializer = CamAnalyticsSerializer(campAnalystics, many=True)
        Team_info_Serializer=TeaminfoSerializer(teaminfo, many=True)
         
        
        # print(CampInvestor_serializer.data)
        context = { 
                    'COMPANY_INFO': Company_info_Serializer.data,
                    'TEAM_INFO':Team_info_Serializer.data,
                    'CAMPAIGN_BANNER': Campbanner_serializer.data,
                    'CAMPAIGN_PRESS': CampPress_serializer.data,
                    'CAMPAIGN_FAQS': CampFAQs_serializer.data,
                    'CAMPAIGN_INVEST': CampInvestor_serializer.data,
                    'CAMPAIGN_ANALYTICS':Cam_Analytics_Serializer.data
                    
                 }
         
        return JsonResponse(context,
                        content_type="application/json",
                        status=status.HTTP_200_OK)   
      
      
      
      
@api_view(['GET', 'PUT', 'DELETE'])
def CampaignAll_Details(request):
    
    # GET list of signup, POST a new user, DELETE all tutori
  if request.method == 'GET': 
        caminfo =  CompanyinfoModel.objects.all()
        teaminfo = TeaminfoModel.objects.all()
        campinvest = CamInvestorModel.objects.all()
        campban = CampaignBannerModel.objects.all()
        camppress = CampPressModel.objects.all()
        campfaqs = CamFAQsModel.objects.all()
        campAnalystics =CampaignAnalyticsModel.objects.all()
        
        
        MODULE = request.GET.get('MODULE', None)
         
        if  MODULE is not None:
            caminfo = caminfo.filter(MODULE__icontains= MODULE)
            campinvest = campinvest.filter( MODULE__icontains= MODULE)
            campban = campban.filter( MODULE__icontains= MODULE)
            camppress = camppress.filter( MODULE__icontains= MODULE)
            campfaqs = campfaqs.filter( MODULE__icontains= MODULE)
            campAnalystics = campAnalystics.filter( MODULE__icontains= MODULE)
            teaminfo = teaminfo.filter( MODULE__icontains= MODULE)
            
            
        Company_info_Serializer = CompanyinfoSerializer(caminfo, many=True)
        CampInvestor_serializer = CamInvestorSerializer(campinvest, many=True)
        Campbanner_serializer = CampaignBannerSerializer(campban, many=True)
        CampPress_serializer = CampaignPressSerializer(camppress, many=True)
        CampFAQs_serializer = CamFAQsSerializer(campfaqs, many=True)
        Cam_Analytics_Serializer = CamAnalyticsSerializer(campAnalystics, many=True)
        Team_info_Serializer=TeaminfoSerializer(teaminfo, many=True)
         
        
        # print(CampInvestor_serializer.data)
        context = { 
                    'COMPANY_INFO': Company_info_Serializer.data,
                    'TEAM_INFO':Team_info_Serializer.data,
                    'CAMPAIGN_BANNER': Campbanner_serializer.data,
                    'CAMPAIGN_PRESS': CampPress_serializer.data,
                    'CAMPAIGN_FAQS': CampFAQs_serializer.data,
                    'CAMPAIGN_INVEST': CampInvestor_serializer.data,
                    'CAMPAIGN_ANALYTICS':Cam_Analytics_Serializer.data
                    
                 }
         
        return JsonResponse(context,
                        content_type="application/json",
                        status=status.HTTP_200_OK)   
      