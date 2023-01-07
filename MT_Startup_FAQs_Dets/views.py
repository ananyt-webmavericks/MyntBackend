from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from MT_Startup_FAQs_Dets.models import FAQsModel
from MT_Startup_FAQs_Dets.serializers import FAQsSerializer
from rest_framework.decorators import api_view
class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, args, *kwargs):
        return Response({
            'FAQ_SNO': reverse(FAQsModel.FAQ_SNO, request=request),
            'lastname': reverse(FAQsModel.LASTNAME, request=request),
            })
from MT_Startup_FAQs_Dets.models import FAQsModel
@api_view(['GET', 'POST', 'DELETE'])
def FAQs_list(request):
    # GET list of signup, POST a new user, DELETE all tutori
  if request.method == 'GET':
        FAQs = FAQsModel.objects.all()
        FAQ_SNO = request.GET.get('FAQ_SNO', None)
        if FAQ_SNO is not None:
            FAQs = FAQs.filter(FAQ_SNO__icontains=FAQ_SNO)
        FAQs_serializer = FAQsSerializer(FAQs, many=True)
        return JsonResponse(FAQs_serializer.data, safe=False)
  elif request.method == 'POST':
        FAQs_data = JSONParser().parse(request)
        FAQs_serializer = FAQsSerializer(data=FAQs_data)
        if  FAQs_serializer.is_valid():
            FAQs_serializer.save()
            return JsonResponse( FAQs_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse( FAQs_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
        count =  FAQsModel.objects.all().delete()
        return JsonResponse({'message': '{}  FAQs were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
@api_view(['GET', 'PUT', 'DELETE'])
def  FAQs_detail(request, pk):
    try:
        FAQs =  FAQsModel.objects.get(pk=pk)
    except  FAQsModel.DoesNotExist:
        return JsonResponse({'message': 'The  FAQs does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        FAQs_serializer = FAQsSerializer( FAQs)
        return JsonResponse( FAQs_serializer.data)
    elif request.method == 'PUT':
        FAQs_data = JSONParser().parse(request)
        FAQs_serializer =  FAQsSerializer( FAQs_data, data= FAQs_data)
        if  FAQs_serializer.is_valid():
            FAQs_serializer.save()
            return JsonResponse( FAQs_serializer.data)
        return JsonResponse( FAQs_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        FAQs.delete()
        return JsonResponse({'message': ' FAQs was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
