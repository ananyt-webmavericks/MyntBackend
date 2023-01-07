from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
 
from MT_Investor_Verify_Standards.models import StandardsModel
from MT_Investor_Verify_Standards.serializers import StandardsSerializer
from rest_framework.decorators import api_view


 


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, args, *kwargs):
        return Response({
            'EMAIL': reverse(StandardsModel.EMAIL, request=request),
         })



@api_view(['GET', 'POST', 'DELETE'])
def Standards_list(request):
    # GET list of signup, POST a new user, DELETE all tutori
  if request.method == 'GET':
        standardsinfo = StandardsModel.objects.all()
        EMAIL = request.GET.get('EMAIL', None)
        print("1",EMAIL)
        if EMAIL is not None:
            standardsinfo = standardsinfo.filter(EMAIL__icontains=EMAIL)
        standardsinfo_serializer = StandardsSerializer(standardsinfo, many=True)
        return JsonResponse(standardsinfo_serializer.data, safe=False)



  elif request.method == 'POST':
        standardsinfo_data = JSONParser().parse(request) 
        standardsinfo_serializer = StandardsSerializer(data=standardsinfo_data)
        print("2",standardsinfo_serializer)
        if  standardsinfo_serializer.is_valid():
            standardsinfo_serializer.save()
            return JsonResponse( standardsinfo_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse( standardsinfo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  elif request.method == 'DELETE':
        print("3")
        count =  StandardsModel.objects.all().delete()
        return JsonResponse({'message': '{}  Terms and Conditions were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def  Standards_detail(request, pk):
    try:
        standardsinfo =  StandardsModel.objects.get(pk=pk)
        print("4")
        
    except  StandardsModel.DoesNotExist:
        return JsonResponse({'message': 'The  Terms and Conditions does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        print("5")
        standardsinfo_serializer = StandardsSerializer( standardsinfo)
        return JsonResponse( standardsinfo_serializer.data)
    
    elif request.method == 'PUT': 
        standardsinfo_data = JSONParser().parse(request)
        standardsinfo_serializer =  StandardsSerializer( standardsinfo, data= standardsinfo_data)
        print("6",standardsinfo_serializer)
        if  standardsinfo_serializer.is_valid():
            print("VALID DATA")
            standardsinfo_serializer.save()
            return JsonResponse( standardsinfo_serializer.data)
        return JsonResponse( standardsinfo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        print("7")
        standardsinfo.delete()
        return JsonResponse({'message': ' Terms and Conditions was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
