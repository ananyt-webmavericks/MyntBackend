from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from MT_Startup_Banner_Dets.models import BannerModel
from MT_Startup_Banner_Dets.serializers import BannerSerializer
from rest_framework.decorators import api_view
class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, args, *kwargs):
        return Response({
            'BANNER_SNO': reverse(BannerModel.BANNER_SNO, request=request),
            'lastname': reverse(BannerModel.LASTNAME, request=request),
            })
from MT_Startup_Banner_Dets.models import BannerModel
@api_view(['GET', 'POST', 'DELETE'])
def Banner_list(request):
    # GET list of signup, POST a new user, DELETE all tutori
  if request.method == 'GET':
        Banner = BannerModel.objects.all()
        BANNER_SNO = request.GET.get('BANNER_SNO', None)
        if BANNER_SNO is not None:
            Banner = Banner.filter(BANNER_SNO__icontains=BANNER_SNO)
        Banner_serializer = BannerSerializer(Banner, many=True)
        return JsonResponse(Banner_serializer.data, safe=False)
  elif request.method == 'POST':
        Banner_data = JSONParser().parse(request)
        Banner_serializer = BannerSerializer(data=Banner_data)
        if  Banner_serializer.is_valid():
            Banner_serializer.save()
            return JsonResponse( Banner_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse( Banner_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
        count =  BannerModel.objects.all().delete()
        return JsonResponse({'message': '{}  Banner were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
@api_view(['GET', 'PUT', 'DELETE'])
def  Banner_detail(request, pk):
    try:
        Banner =  BannerModel.objects.get(pk=pk)
    except  BannerModel.DoesNotExist:
        return JsonResponse({'message': 'The  Banner does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        Banner_serializer = BannerSerializer( Banner)
        return JsonResponse( Banner_serializer.data)
    elif request.method == 'PUT':
        Banner_data = JSONParser().parse(request)
        Banner_serializer =  BannerSerializer( Banner_data, data= Banner_data)
        if  Banner_serializer.is_valid():
            Banner_serializer.save()
            return JsonResponse( Banner_serializer.data)
        return JsonResponse( Banner_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        Banner.delete()
        return JsonResponse({'message': ' Banner was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
