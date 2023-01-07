

from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from MT_Investor_Verifiy_Nationality.models import NationalityModel
from MT_Investor_Verifiy_Nationality.serializers import NationalitySerializer
from rest_framework.decorators import api_view 
from MT_Investor_Verifiy_Nationality.models import NationalityModel


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, args, *kwargs):
        return Response({
            'EMAIL': reverse(NationalityModel.EMAIL, request=request),
         })



@api_view(['GET', 'POST', 'DELETE'])
def Nationality_list(request):
    # GET list of signup, POST a new user, DELETE all tutori
  if request.method == 'GET':
        nationalityinfo = NationalityModel.objects.all()
        EMAIL = request.GET.get('EMAIL', None)
        print("1",EMAIL)
        if EMAIL is not None:
            nationalityinfo = nationalityinfo.filter(EMAIL__icontains=EMAIL)
        nationalityinfo_serializer = NationalitySerializer(nationalityinfo, many=True)
        return JsonResponse(nationalityinfo_serializer.data, safe=False)



  elif request.method == 'POST':
        nationalityinfo_data = JSONParser().parse(request) 
        nationalityinfo_serializer = NationalitySerializer(data=nationalityinfo_data)
        print("2",nationalityinfo_serializer)
        if  nationalityinfo_serializer.is_valid():
            nationalityinfo_serializer.save()
            return JsonResponse( nationalityinfo_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse( nationalityinfo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  elif request.method == 'DELETE':
        print("3")
        count =  NationalityModel.objects.all().delete()
        return JsonResponse({'message': '{}  nationalityinfo were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def  Nationality_detail(request, pk):
    try:
        nationalityinfo =  NationalityModel.objects.get(pk=pk)
        print("4")
        
    except  NationalityModel.DoesNotExist:
        return JsonResponse({'message': 'The  nationalityinfo does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        print("5")
        nationalityinfo_serializer = NationalitySerializer( nationalityinfo)
        return JsonResponse( nationalityinfo_serializer.data)
    
    elif request.method == 'PUT': 
        nationalityinfo_data = JSONParser().parse(request)
        nationalityinfo_serializer =  NationalitySerializer( nationalityinfo, data= nationalityinfo_data)
        print("6",nationalityinfo_serializer)
        if  nationalityinfo_serializer.is_valid():
            print("VALID DATA")
            nationalityinfo_serializer.save()
            return JsonResponse( nationalityinfo_serializer.data)
        return JsonResponse( nationalityinfo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        print("7")
        nationalityinfo.delete()
        return JsonResponse({'message': ' nationalityinfo was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
