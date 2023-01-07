from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from MT_Startup_Agreements.models import AgreementsModel
from MT_Startup_Agreements.serializers import AgreementsSerializer
from rest_framework.decorators import api_view
class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, args, *kwargs):
        return Response({
            'ESIGN_DOC': reverse(AgreementsModel.ESIGN_DOC, request=request),
            'lastname': reverse(AgreementsModel.LASTNAME, request=request),
            })
from MT_Startup_Agreements.models import AgreementsModel
@api_view(['GET', 'POST', 'DELETE'])
def Agreements_list(request):
    # GET list of signup, POST a new user, DELETE all tutori
  if request.method == 'GET':
        Agreements = AgreementsModel.objects.all()
        ESIGN_DOC = request.GET.get('ESIGN_DOC', None)
        if ESIGN_DOC is not None:
            Agreements = Agreements.filter(ESIGN_DOC__icontains=ESIGN_DOC)
        Agreements_serializer = AgreementsSerializer(Agreements, many=True)
        return JsonResponse(Agreements_serializer.data, safe=False)
  elif request.method == 'POST':
        Agreements_data = JSONParser().parse(request)
        Agreements_serializer = AgreementsSerializer(data=Agreements_data)
        if  Agreements_serializer.is_valid():
            Agreements_serializer.save()
            return JsonResponse(Agreements_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(Agreements_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
        count = AgreementsModel.objects.all().delete()
        return JsonResponse({'message': '{} Agreements were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
@api_view(['GET', 'PUT', 'DELETE'])
def Agreements_detail(request, pk):
    try:
       Agreements = AgreementsModel.objects.get(pk=pk)
    except AgreementsModel.DoesNotExist:
        return JsonResponse({'message': 'The Agreements does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        Agreements_serializer =AgreementsSerializer(Agreements)
        return JsonResponse(Agreements_serializer.data)
    elif request.method == 'PUT':
        Agreements_data = JSONParser().parse(request)
        Agreements_serializer = AgreementsSerializer(Agreements_data, data=Agreements_data)
        if Agreements_serializer.is_valid():
            Agreements_serializer.save()
            return JsonResponse(Agreements_serializer.data)
        return JsonResponse(Agreements_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        Agreements.delete()
        return JsonResponse({'message': 'Agreements was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
