from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from MT_Startup_Pitchinfo.models import PitchinfoModel
from MT_Startup_Pitchinfo.serializers import PitchinfoSerializer
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser



class ApiRoot(generics.GenericAPIView):
    parser_classes = (MultiPartParser, FormParser)
    name = 'api-root'
    def get(self, request, args, *kwargs):
        return Response({
             'EMAIL': reverse(PitchinfoModel.EMAIL, request=request),
            })
        
        
         
@api_view(['GET', 'POST', 'DELETE'])
def Pitchinfo_list(request):
    # GET list of signup, POST a new user, DELETE all tutori
  if request.method == 'GET':
        Pitchinfo = PitchinfoModel.objects.all()
        EMAIL = request.GET.get('EMAIL', None)
        if EMAIL is not None:
            Pitchinfo = Pitchinfo.filter(EMAIL__icontains=EMAIL)
        Pitchinfo_serializer = PitchinfoSerializer(Pitchinfo, many=True)
        return JsonResponse(Pitchinfo_serializer.data, safe=False)
    
    
    
    
  elif request.method == 'POST':
        # Pitchinfo_data = JSONParser().parse(request)
        Pitchinfo_serializer = PitchinfoSerializer(data=request.data)
        if Pitchinfo_serializer.is_valid():
            Pitchinfo_serializer.save()
            return JsonResponse(Pitchinfo_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(Pitchinfo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  
  elif request.method == 'DELETE':
        count = PitchinfoModel.objects.all().delete()
        return JsonResponse({'message': '{} Pitch Upload documented were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'PUT', 'DELETE'])
def Pitchinfo_detail(request, pk):
    try:
       Pitchinfo = PitchinfoModel.objects.get(pk=pk)
    except PitchinfoModel.DoesNotExist:
        return JsonResponse({'message': 'Pitch Upload documented does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    
    if request.method == 'GET':
        Pitchinfo_serializer =PitchinfoSerializer(Pitchinfo)
        return JsonResponse(Pitchinfo_serializer.data)
    
    
    elif request.method == 'PUT':
        # Pitchinfo_data = JSONParser().parse(request)
        Pitchinfo_serializer = PitchinfoSerializer(Pitchinfo, data=request.data)
        if  Pitchinfo_serializer.is_valid():
            Pitchinfo_serializer.save()
            return JsonResponse(Pitchinfo_serializer.data)
        return JsonResponse(Pitchinfo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    elif request.method == 'DELETE':
        Pitchinfo.delete()
        return JsonResponse({'message': 'Pitchinfo was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
