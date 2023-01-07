from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from MT_Startup_Pitch_Competitioninfo.models import CompetitioninfoModel
from MT_Startup_Pitch_Competitioninfo.serializers import CompetitioninfoSerializer
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
            'EMAIL': reverse(CompetitioninfoModel.EMAIL, request=request),
            })
        
        
        
@api_view(['GET', 'POST', 'DELETE'])
def Competitioninfo_list(request):
    
    # GET list of signup, POST a new user, DELETE all tutori
  if request.method == 'GET':
         
        competitiondets = CompetitioninfoModel.objects.all()
        
        EMAIL = request.GET.get('EMAIL', None)
        if EMAIL is not None:
            competitiondets = competitiondets.filter(EMAIL__icontains=EMAIL)
        
        competitiondets_serializer = CompetitioninfoSerializer(competitiondets, many=True)  
        return JsonResponse(competitiondets_serializer.data, safe=False)
 
  elif request.method == 'POST':
        # html_content = "<p>That's <strong>the HTML part</strong></p>"
        competitiondets_serializer = CompetitioninfoSerializer(data=request.data)
        if  competitiondets_serializer.is_valid():
            competitiondets_serializer.save()
            return JsonResponse(competitiondets_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(competitiondets_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  elif request.method == 'DELETE':
        count = CompetitioninfoModel.objects.all().delete()
        return JsonResponse({'message': '{} Pitch Competition is deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def Competitioninfo_detail(request, pk):
    try:
        competitiondets = CompetitioninfoModel.objects.get(pk=pk)
    except CompetitioninfoModel.DoesNotExist:
        return JsonResponse({'message': 'Pitch Competition does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        print("4")
        competitiondets_serializer = CompetitioninfoSerializer(competitiondets)
        return JsonResponse(competitiondets_serializer.data)
    
    elif request.method == 'PUT':
       
        # competitiondets_data = JSONParser().parse(request)
        competitiondets_serializer = CompetitioninfoSerializer(competitiondets, data=request.data)
        
        if  competitiondets_serializer.is_valid():
            competitiondets_serializer.save()
            return JsonResponse(competitiondets_serializer.data)
        return JsonResponse(competitiondets_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        print("6")
        competitiondets.delete()
        return JsonResponse({'message': 'Pitch Competition was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
