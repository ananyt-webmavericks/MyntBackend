from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from MT_Startup_Pitch_Tractioninfo.models import TractioninfoModel
from MT_Startup_Pitch_Tractioninfo.serializers import TractioninfoSerializer
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
            'EMAIL': reverse(TractioninfoModel.EMAIL, request=request),
            })
        
        
        
@api_view(['GET', 'POST', 'DELETE'])
def Tractioninfo_list(request):
    
    # GET list of signup, POST a new user, DELETE all tutori
  if request.method == 'GET':
         
        transactiondets = TractioninfoModel.objects.all()
        
        EMAIL = request.GET.get('EMAIL', None)
        if EMAIL is not None:
            transactiondets = transactiondets.filter(EMAIL__icontains=EMAIL)
        
        transactiondets_serializer = TractioninfoSerializer(transactiondets, many=True)  
        return JsonResponse(transactiondets_serializer.data, safe=False)
 
  elif request.method == 'POST':
        # html_content = "<p>That's <strong>the HTML part</strong></p>"
        transactiondets_serializer = TractioninfoSerializer(data=request.data)
        if  transactiondets_serializer.is_valid():
            transactiondets_serializer.save()
            return JsonResponse(transactiondets_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(transactiondets_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  elif request.method == 'DELETE':
        count = TractioninfoModel.objects.all().delete()
        return JsonResponse({'message': '{} Pitch Transaction is deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def Tractioninfo_detail(request, pk):
    try:
        transactiondets = TractioninfoModel.objects.get(pk=pk)
    except TractioninfoModel.DoesNotExist:
        return JsonResponse({'message': 'Pitch Transaction does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        print("4")
        transactiondets_serializer = TractioninfoSerializer(transactiondets)
        return JsonResponse(transactiondets_serializer.data)
    
    elif request.method == 'PUT':
       
        # transactiondets_data = JSONParser().parse(request)
        transactiondets_serializer = TractioninfoSerializer(transactiondets, data=request.data)
        
        if  transactiondets_serializer.is_valid():
            transactiondets_serializer.save()
            return JsonResponse(transactiondets_serializer.data)
        return JsonResponse(transactiondets_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        print("6")
        transactiondets.delete()
        return JsonResponse({'message': 'Pitch Transaction was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
