from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from MT_Startup_Pitch_Solution.models import SolutionModel
from MT_Startup_Pitch_Solution.serializers import SolutionSerializer
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
            'EMAIL': reverse(SolutionModel.EMAIL, request=request),
            })
        
        
        
@api_view(['GET', 'POST', 'DELETE'])
def Solution_list(request):
    
    # GET list of signup, POST a new user, DELETE all tutori
  if request.method == 'GET':
         
        solutiondets = SolutionModel.objects.all()
        
        EMAIL = request.GET.get('EMAIL', None)
        if EMAIL is not None:
            solutiondets = solutiondets.filter(EMAIL__icontains=EMAIL)
        
        solutiondets_serializer = SolutionSerializer(solutiondets, many=True)  
        return JsonResponse(solutiondets_serializer.data, safe=False)
 
  elif request.method == 'POST': 
        solutiondets_serializer = SolutionSerializer(data=request.data)
        if  solutiondets_serializer.is_valid():
            solutiondets_serializer.save()
            return JsonResponse(solutiondets_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(solutiondets_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  elif request.method == 'DELETE':
        count = SolutionModel.objects.all().delete()
        return JsonResponse({'message': '{} Pitch Solution is deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def Solution_detail(request, pk):
    try:
        solutiondets = SolutionModel.objects.get(pk=pk)
    except SolutionModel.DoesNotExist:
        return JsonResponse({'message': 'Pitch Solution does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        print("4")
        solutiondets_serializer = SolutionSerializer(solutiondets)
        return JsonResponse(solutiondets_serializer.data)
    
    elif request.method == 'PUT':
       
        # solutiondets_data = JSONParser().parse(request)
        solutiondets_serializer = SolutionSerializer(solutiondets, data=request.data)
        
        if  solutiondets_serializer.is_valid():
            solutiondets_serializer.save()
            return JsonResponse(solutiondets_serializer.data)
        return JsonResponse(solutiondets_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        print("6")
        solutiondets.delete()
        return JsonResponse({'message': 'Pitch Solution  was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
