from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from MT_Startup_Investors_Dets.models import InvestorsDetsModel
from MT_Startup_Investors_Dets.serializers import InvestorsDetsSerializer
from rest_framework.decorators import api_view
class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, args, *kwargs):
        return Response({
            'INVESTOR_SNO': reverse(InvestorsDetsModel.INVESTOR_SNO, request=request),
            'lastname': reverse(InvestorsDetsModel.LASTNAME, request=request),
            })
from MT_Startup_Investors_Dets.models import InvestorsDetsModel
@api_view(['GET', 'POST', 'DELETE'])
def InvestorsDets_list(request):
    # GET list of signup, POST a new user, DELETE all tutori
  if request.method == 'GET':
        InvestorsDets = InvestorsDetsModel.objects.all()
        INVESTOR_SNO = request.GET.get('INVESTOR_SNO', None)
        if INVESTOR_SNO is not None:
            InvestorsDets = InvestorsDets.filter(PITCH_ID_GEN__icontains=INVESTOR_SNO)
        InvestorsDets_serializer = InvestorsDetsSerializer(InvestorsDets, many=True)
        return JsonResponse(InvestorsDets_serializer.data, safe=False)
  elif request.method == 'POST':
        InvestorsDets_data = JSONParser().parse(request)
        InvestorsDets_serializer = InvestorsDetsSerializer(data=InvestorsDets_data)
        if  InvestorsDets_serializer.is_valid():
            InvestorsDets_serializer.save()
            return JsonResponse(InvestorsDets_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(InvestorsDets_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
        count = InvestorsDetsModel.objects.all().delete()
        return JsonResponse({'message': '{} InvestorsDets were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
@api_view(['GET', 'PUT', 'DELETE'])
def InvestorsDets_detail(request, pk):
    try:
       InvestorsDets = InvestorsDetsModel.objects.get(pk=pk)
    except InvestorsDetsModel.DoesNotExist:
        return JsonResponse({'message': 'The InvestorsDets does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        InvestorsDets_serializer =InvestorsDetsSerializer(InvestorsDets)
        return JsonResponse(InvestorsDets_serializer.data)
    elif request.method == 'PUT':
        InvestorsDets_data = JSONParser().parse(request)
        InvestorsDets_serializer = InvestorsDetsSerializer(InvestorsDets_data, data=InvestorsDets_data)
        if InvestorsDets_serializer.is_valid():
            InvestorsDets_serializer.save()
            return JsonResponse(InvestorsDets_serializer.data)
        return JsonResponse(InvestorsDets_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        InvestorsDets.delete()
        return JsonResponse({'message': 'InvestorsDets was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
