from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from MT_Startup_Pressinfo.models import PressinfoModel
from MT_Startup_Pressinfo.serializers import PressinfoSerializer
from rest_framework.decorators import api_view
class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, args, *kwargs):
        return Response({
            'MTUSER_ID': reverse(PressinfoModel.PRESS_SNO, request=request),
            'lastname': reverse(PressinfoModel.LASTNAME, request=request),
            })
from MT_Startup_Pressinfo.models import PressinfoModel
@api_view(['GET', 'POST', 'DELETE'])
def Pressinfo_list(request):
    # GET list of signup, POST a new user, DELETE all tutori
  if request.method == 'GET':
        Pressinfo = PressinfoModel.objects.all()
        PRESS_SNO = request.GET.get('PRESS_SNO', None)
        if PRESS_SNO is not None:
            Pressinfo = Pressinfo.filter(FIRSTNAME__icontains=PRESS_SNO)
        Pressinfo_serializer = PressinfoSerializer(Pressinfo, many=True)
        return JsonResponse(Pressinfo_serializer.data, safe=False)
  elif request.method == 'POST':
        Pressinfo_data = JSONParser().parse(request)
        Pressinfo_serializer = PressinfoSerializer(data=Pressinfo_data)
        if Pressinfo_serializer.is_valid():
            Pressinfo_serializer.save()
            return JsonResponse(Pressinfo_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(Pressinfo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
        count = PressinfoModel.objects.all().delete()
        return JsonResponse({'message': '{} Pressinfo were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
@api_view(['GET', 'PUT', 'DELETE'])
def Pressinfo_detail(request, pk):
    try:
        Pressinfo = PressinfoModel.objects.get(pk=pk)
    except PressinfoModel.DoesNotExist:
        return JsonResponse({'message': 'The Pressinfo does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        Pressinfo_serializer = PressinfoSerializer(Pressinfo)
        return JsonResponse(Pressinfo_serializer.data)
    elif request.method == 'PUT':
        Pressinfo_data = JSONParser().parse(request)
        Pressinfo_serializer = PressinfoSerializer(Pressinfo_data, data=Pressinfo_data)
        if Pressinfo_serializer.is_valid():
            Pressinfo_serializer.save()
            return JsonResponse(Pressinfo_serializer.data)
        return JsonResponse(Pressinfo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        Pressinfo.delete()
        return JsonResponse({'message': 'Pressinfo was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
