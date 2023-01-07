from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
 
from MT_Investor_Choose_Sector.models import Choose_SectorModel
from MT_Investor_Choose_Sector.serializers import Choose_SectorSerializer
from rest_framework.decorators import api_view


 


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, args, *kwargs):
        return Response({
            'EMAIL': reverse(Choose_SectorModel.EMAIL, request=request),
         })



@api_view(['GET', 'POST', 'DELETE'])
def Choose_Sector_list(request):
    # GET list of signup, POST a new user, DELETE all tutori
  if request.method == 'GET':
        sectorsinfo = Choose_SectorModel.objects.all()
        EMAIL = request.GET.get('EMAIL', None)
        print("1",EMAIL)
        if EMAIL is not None:
            sectorsinfo = sectorsinfo.filter(EMAIL__icontains=EMAIL)
        sectorsinfo_serializer = Choose_SectorSerializer(sectorsinfo, many=True)
        return JsonResponse(sectorsinfo_serializer.data, safe=False)



  elif request.method == 'POST':
        sectorsinfo_data = JSONParser().parse(request) 
        sectorsinfo_serializer = Choose_SectorSerializer(data=sectorsinfo_data)
        print("2",sectorsinfo_serializer)
        if  sectorsinfo_serializer.is_valid():
            sectorsinfo_serializer.save()
            return JsonResponse( sectorsinfo_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse( sectorsinfo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  elif request.method == 'DELETE':
        print("3")
        count =  Choose_SectorModel.objects.all().delete()
        return JsonResponse({'message': '{}  Terms and Conditions were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def  Choose_Sector_detail(request, pk):
    try:
        sectorsinfo =  Choose_SectorModel.objects.get(pk=pk)
        print("4")
        
    except  Choose_SectorModel.DoesNotExist:
        return JsonResponse({'message': 'The  Terms and Conditions does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        print("5")
        sectorsinfo_serializer = Choose_SectorSerializer( sectorsinfo)
        return JsonResponse( sectorsinfo_serializer.data)
    
    elif request.method == 'PUT': 
        sectorsinfo_data = JSONParser().parse(request)
        sectorsinfo_serializer =  Choose_SectorSerializer( sectorsinfo, data= sectorsinfo_data)
        print("6",sectorsinfo_serializer)
        if  sectorsinfo_serializer.is_valid():
            print("VALID DATA")
            sectorsinfo_serializer.save()
            return JsonResponse( sectorsinfo_serializer.data)
        return JsonResponse( sectorsinfo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        print("7")
        sectorsinfo.delete()
        return JsonResponse({'message': ' Terms and Conditions was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
