from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
 
from MT_Investor_Kyc.models import KycModel
from MT_Investor_Kyc.serializers import KycSerializer
from rest_framework.decorators import api_view
 


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, args, *kwargs):
        return Response({
            'EMAIL': reverse(KycModel.EMAIL, request=request),
         })



@api_view(['GET', 'POST', 'DELETE'])
def kyc_list(request):
    # GET list of signup, POST a new user, DELETE all tutori
  if request.method == 'GET':
        kycinfo = KycModel.objects.all()
        EMAIL = request.GET.get('EMAIL', None)
        print("1",EMAIL)
        if EMAIL is not None:
            kycinfo = kycinfo.filter(EMAIL__icontains=EMAIL)
        kycinfo_serializer = KycSerializer(kycinfo, many=True)
        return JsonResponse(kycinfo_serializer.data, safe=False)



  elif request.method == 'POST':
        kycinfo_data = JSONParser().parse(request) 
        kycinfo_serializer = KycSerializer(data=kycinfo_data)
        print("2",kycinfo_serializer)
        if  kycinfo_serializer.is_valid():
            kycinfo_serializer.save()
            return JsonResponse( kycinfo_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse( kycinfo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  elif request.method == 'DELETE':
        print("3")
        count =  KycModel.objects.all().delete()
        return JsonResponse({'message': '{}  kycinfo were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def  kyc_detail(request, pk):
    try:
        kycinfo =  KycModel.objects.get(pk=pk)
        print("4")
    except  KycModel.DoesNotExist:
        return JsonResponse({'message': 'The  kycinfo does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        print("5")
        kycinfo_serializer = KycSerializer( kycinfo)
        return JsonResponse( kycinfo_serializer.data)
    elif request.method == 'PUT': 
        kycinfo_data = JSONParser().parse(request)
        kycinfo_serializer =  KycSerializer( kycinfo, data= kycinfo_data)
        print("6",kycinfo_serializer)
        if  kycinfo_serializer.is_valid():
            print("VALID DATA")
            kycinfo_serializer.save()
            return JsonResponse( kycinfo_serializer.data)
        return JsonResponse( kycinfo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        print("7")
        kycinfo.delete()
        return JsonResponse({'message': ' kycinfo was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
