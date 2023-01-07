from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from MT_Startup_Companyinfo.models import CompanyinfoModel
from MT_Startup_Companyinfo.serializers import CompanyinfoSerializer
from rest_framework.decorators import api_view 
from MT_Startup_Companyinfo.models import CompanyinfoModel


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, args, *kwargs):
        return Response({
            'EMAIL': reverse(CompanyinfoModel.EMAIL, request=request),
         })



@api_view(['GET', 'POST', 'DELETE'])
def companyinfo_list(request):
    # GET list of signup, POST a new user, DELETE all tutori
  if request.method == 'GET':
        Companyinfo = CompanyinfoModel.objects.all()
        EMAIL = request.GET.get('EMAIL', None)
        print("1",EMAIL)
        if EMAIL is not None:
            Companyinfo = Companyinfo.filter(EMAIL__icontains=EMAIL)
        Companyinfo_serializer = CompanyinfoSerializer(Companyinfo, many=True)
        return JsonResponse(Companyinfo_serializer.data, safe=False)



  elif request.method == 'POST':
        Companyinfo_data = JSONParser().parse(request) 
        Companyinfo_serializer = CompanyinfoSerializer(data=Companyinfo_data)
        print("2",Companyinfo_serializer)
        if  Companyinfo_serializer.is_valid():
            Companyinfo_serializer.save()
            return JsonResponse( Companyinfo_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse( Companyinfo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  elif request.method == 'DELETE':
        print("3")
        count =  CompanyinfoModel.objects.all().delete()
        return JsonResponse({'message': '{}  Companyinfo were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def  companyinfo_details(request, pk):
    try:
        Companyinfo =  CompanyinfoModel.objects.get(pk=pk)
        print("4")
    except  CompanyinfoModel.DoesNotExist:
        return JsonResponse({'message': 'The  Companyinfo does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        print("5")
        Companyinfo_serializer = CompanyinfoSerializer( Companyinfo)
        return JsonResponse( Companyinfo_serializer.data)
    elif request.method == 'PUT': 
        Companyinfo_data = JSONParser().parse(request)
        Companyinfo_serializer =  CompanyinfoSerializer( Companyinfo, data= Companyinfo_data)
        print("6",Companyinfo_serializer)
        if  Companyinfo_serializer.is_valid():
            print("VALID DATA")
            Companyinfo_serializer.save()
            return JsonResponse( Companyinfo_serializer.data)
        return JsonResponse( Companyinfo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        print("7")
        Companyinfo.delete()
        return JsonResponse({'message': ' Companyinfo was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
