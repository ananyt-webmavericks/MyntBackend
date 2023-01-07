from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from MT_Startup_Teaminfo.models import TeaminfoModel
from MT_Startup_Teaminfo.serializers import TeaminfoSerializer
from rest_framework.decorators import api_view
from MT_Startup_Teaminfo.models import TeaminfoModel
from rest_framework.parsers import MultiPartParser, FormParser


class ApiRoot(generics.GenericAPIView): 
    parser_classes = (MultiPartParser, FormParser)
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'EMAIL': reverse(TeaminfoModel.EMAIL, request=request),
            'TEAM_SNO': reverse(TeaminfoModel.TEAM_SNO, request=request), 
            'TEAM_MEMBER_NAME': reverse(TeaminfoModel.TEAM_MEMBER_NAME, request=request), 
            'TEAM_MEMBER_POSITION': reverse(TeaminfoModel.TEAM_MEMBER_POSITION, request=request), 
            'FB_LINK': reverse(TeaminfoModel.FB_LINK, request=request), 
            'INSTA_LINK': reverse(TeaminfoModel.INSTA_LINK, request=request), 
            'LINKEDIN_LINK': reverse(TeaminfoModel.LINKEDIN_LINK, request=request), 
            'TEAM_BIO': reverse(TeaminfoModel.TEAM_BIO, request=request), 
            'PROFILE_PIC': reverse(TeaminfoModel.PROFILE_PIC, request=request), 
            })
        
        
        
@api_view(['GET', 'POST', 'DELETE'])
def Teaminfo_list(request):
    
    # GET list of signup, POST a new user, DELETE all tutori
  if request.method == 'GET':
       
        teaminfo = TeaminfoModel.objects.all()
        EMAIL = request.GET.get('EMAIL', None)
         
        if  EMAIL is not None:
            teaminfo = teaminfo.filter( EMAIL__icontains= EMAIL)
        teaminfo_serializer = TeaminfoSerializer(teaminfo, many=True)
        print("1",teaminfo_serializer.data)
        return JsonResponse(teaminfo_serializer.data, safe=False)
    
    
  elif request.method == 'POST':
        teaminfo_serializer = TeaminfoSerializer(data=request.data) 
        if  teaminfo_serializer.is_valid():
            teaminfo_serializer.save()
            return Response(teaminfo_serializer.data, status=status.HTTP_201_CREATED)
        return Response(teaminfo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  
  elif request.method == 'DELETE':
        print("3")
        count = TeaminfoModel.objects.all().delete()
        return JsonResponse({'message': '{} Team Info were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def Teaminfo_detail(request, pk):
    try:
        teaminfo = TeaminfoModel.objects.get(pk=pk)
    except TeaminfoModel.DoesNotExist:
        return JsonResponse({'message': 'The Team Info does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        print("4")
        teaminfo_serializer = TeaminfoSerializer(teaminfo)
        return JsonResponse(teaminfo_serializer.data)
    
    elif request.method == 'PUT':
        print("5")
        # teaminfo_data = JSONParser().parse(request)
        teaminfo_serializer = TeaminfoSerializer(teaminfo, data=request.data)
        
        if  teaminfo_serializer.is_valid():
            teaminfo_serializer.save()
            return JsonResponse(teaminfo_serializer.data)
        return JsonResponse(teaminfo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        print("6")
        teaminfo.delete()
        return JsonResponse({'message': 'Team Info was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
