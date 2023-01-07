from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from MT_Startup_Analystics_TRinfo.models import AnalysticsModel
from MT_Startup_Analystics_TRinfo.serializers import AnalysticsSerializer
from rest_framework.decorators import api_view
class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, args, *kwargs):
        return Response({
            'TR_ANAL_SNO': reverse(AnalysticsModel.TR_ANAL_SNO, request=request),
            'lastname': reverse(AnalysticsModel.LASTNAME, request=request),
            })
from MT_Startup_Analystics_TRinfo.models import AnalysticsModel
@api_view(['GET', 'POST', 'DELETE'])
def Analystics_list(request):
    # GET list of signup, POST a new user, DELETE all tutori
  if request.method == 'GET':
        Analystics = AnalysticsModel.objects.all()
        TR_ANAL_SNO = request.GET.get('TR_ANAL_SNO', None)
        if TR_ANAL_SNO is not None:
            Analystics = Analystics.filter(TR_ANAL_SNO__icontains=TR_ANAL_SNO)
        Analystics_serializer = AnalysticsSerializer(Analystics, many=True)
        return JsonResponse(Analystics_serializer.data, safe=False)
  elif request.method == 'POST':
        Analystics_data = JSONParser().parse(request)
        Analystics_serializer = AnalysticsSerializer(data=Analystics_data)
        if  Analystics_serializer.is_valid():
            Analystics_serializer.save()
            return JsonResponse(Analystics_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(Analystics_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
        count = AnalysticsModel.objects.all().delete()
        return JsonResponse({'message': '{} Analystics were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
@api_view(['GET', 'PUT', 'DELETE'])
def Analystics_detail(request, pk):
    try:
       Analystics = AnalysticsModel.objects.get(pk=pk)
    except AnalysticsModel.DoesNotExist:
        return JsonResponse({'message': 'The Analystics does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        Analystics_serializer =AnalysticsSerializer(Analystics)
        return JsonResponse(Analystics_serializer.data)
    elif request.method == 'PUT':
        Analystics_data = JSONParser().parse(request)
        Analystics_serializer = AnalysticsSerializer(Analystics_data, data=Analystics_data)
        if Analystics_serializer.is_valid():
            Analystics_serializer.save()
            return JsonResponse(Analystics_serializer.data)
        return JsonResponse(Analystics_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        Analystics.delete()
        return JsonResponse({'message': 'Analystics was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
