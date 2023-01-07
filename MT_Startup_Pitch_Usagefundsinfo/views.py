from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from MT_Startup_Pitch_Usagefundsinfo.models import UsagefundsinfoModel
from MT_Startup_Pitch_Usagefundsinfo.serializers import UsagefundsinfoSerializer
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
            'EMAIL': reverse(UsagefundsinfoModel.EMAIL, request=request),
            })
        
        
        
@api_view(['GET', 'POST', 'DELETE'])
def Usagefundsinfo_list(request):
    
    # GET list of signup, POST a new user, DELETE all tutori
  if request.method == 'GET':
         
        usagedets = UsagefundsinfoModel.objects.all()
        
        EMAIL = request.GET.get('EMAIL', None)
        if EMAIL is not None:
            usagedets = usagedets.filter(EMAIL__icontains=EMAIL)
        
        usagedets_serializer = UsagefundsinfoSerializer(usagedets, many=True)  
        return JsonResponse(usagedets_serializer.data, safe=False)
 
  elif request.method == 'POST':
        # html_content = "<p>That's <strong>the HTML part</strong></p>"
        usagedets_serializer = UsagefundsinfoSerializer(data=request.data)
        if  usagedets_serializer.is_valid():
            usagedets_serializer.save()
            return JsonResponse(usagedets_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(usagedets_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  elif request.method == 'DELETE':
        count = UsagefundsinfoModel.objects.all().delete()
        return JsonResponse({'message': '{} Pitch Usage is deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def Usagefundsinfo_detail(request, pk):
    try:
        usagedets = UsagefundsinfoModel.objects.get(pk=pk)
    except UsagefundsinfoModel.DoesNotExist:
        return JsonResponse({'message': 'Pitch Usage does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        print("4")
        usagedets_serializer = UsagefundsinfoSerializer(usagedets)
        return JsonResponse(usagedets_serializer.data)
    
    elif request.method == 'PUT':
       
        # usagedets_data = JSONParser().parse(request)
        usagedets_serializer = UsagefundsinfoSerializer(usagedets, data=request.data)
        
        if  usagedets_serializer.is_valid():
            usagedets_serializer.save()
            return JsonResponse(usagedets_serializer.data)
        return JsonResponse(usagedets_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        print("6")
        usagedets.delete()
        return JsonResponse({'message': 'Pitch Usage was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
