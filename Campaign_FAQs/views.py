from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from Campaign_FAQs.models import CamFAQsModel
from Campaign_FAQs.serializers import CamFAQsSerializer
from rest_framework.decorators import api_view
from Campaign_FAQs.models import CamFAQsModel
from rest_framework.parsers import MultiPartParser, FormParser


class ApiRoot(generics.GenericAPIView): 
    parser_classes = (MultiPartParser, FormParser)
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'EMAIL': reverse(CamFAQsModel.EMAIL, request=request),
              })
        
        
        
@api_view(['GET', 'POST', 'DELETE'])
def CampFAQ_list(request):
    
    # GET list of signup, POST a new user, DELETE all tutori
  if request.method == 'GET':
       
        campfaqs = CamFAQsModel.objects.all()
        EMAIL = request.GET.get('EMAIL', None)
         
        if  EMAIL is not None:
            campfaqs = campfaqs.filter( EMAIL__icontains= EMAIL)
        CampFAQ_serializer = CamFAQsSerializer(campfaqs, many=True)
        print("1",CampFAQ_serializer.data)
        return JsonResponse(CampFAQ_serializer.data, safe=False)
    
    
  elif request.method == 'POST':
        print(request.data)
        CampFAQ_serializer = CamFAQsSerializer(data=request.data) 
        if  CampFAQ_serializer.is_valid():
            print(CampFAQ_serializer)
            CampFAQ_serializer.save()
            return Response(CampFAQ_serializer.data, status=status.HTTP_201_CREATED)
        return Response(CampFAQ_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  
  elif request.method == 'DELETE':
        print("3")
        count = CamFAQsModel.objects.all().delete()
        return JsonResponse({'message': '{} Campaign FAQs were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def CampFAQ_detail(request, pk):
    try:
        campfaqs = CamFAQsModel.objects.get(pk=pk)
    except CamFAQsModel.DoesNotExist:
        return JsonResponse({'message': 'The Campaign FAQs does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        print("4")
        CampFAQ_serializer = CamFAQsSerializer(campfaqs)
        return JsonResponse(CampFAQ_serializer.data)
    
    elif request.method == 'PUT':
        print("5")
        # CampFAQ_data = JSONParser().parse(request)
        CampFAQ_serializer = CamFAQsSerializer(campfaqs, data=request.data)
        
        if  CampFAQ_serializer.is_valid():
            CampFAQ_serializer.save()
            return JsonResponse(CampFAQ_serializer.data)
        return JsonResponse(CampFAQ_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        print("6")
        campfaqs.delete()
        return JsonResponse({'message': 'Campaign FAQs was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
