from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from MT_Raise.models import RaiseModel
from MT_Raise.serializers import RaiseSerializer
from rest_framework.decorators import api_view 
from rest_framework.parsers import MultiPartParser, FormParser
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail 
from django.http import HttpResponse 






class ApiRoot(generics.GenericAPIView): 
    parser_classes = (MultiPartParser, FormParser)
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'EMAIL': reverse(RaiseModel.EMAIL, request=request),
            'RAISE_NAME': reverse(RaiseModel.RAISE_NAME, request=request), 
            'RAISE_EMAIL': reverse(RaiseModel.RAISE_EMAIL, request=request), 
            'RAISE_FOUNDER_URL1': reverse(RaiseModel.RAISE_FOUNDER_URL1, request=request), 
            'RAISE_FOUNDER_URL2': reverse(RaiseModel.RAISE_FOUNDER_URL2, request=request), 
            'RAISE_COMPANY_NAME': reverse(RaiseModel.RAISE_COMPANY_NAME, request=request), 
            'RAISE_COM_LINKPAGE': reverse(RaiseModel.RAISE_COM_LINKPAGE, request=request), 
            'RAISE_WEBSITE': reverse(RaiseModel.RAISE_WEBSITE, request=request), 
            'RAISE_FUNDRAISING': reverse(RaiseModel.RAISE_FUNDRAISING, request=request), 
            'RAISE_PROD_DESC': reverse(RaiseModel.RAISE_PROD_DESC, request=request), 
            'RAISE_TRACTION': reverse(RaiseModel.RAISE_TRACTION, request=request), 
            'RAISE_REVENUE': reverse(RaiseModel.RAISE_REVENUE, request=request), 
            'RAISE_TEAM': reverse(RaiseModel.RAISE_TEAM, request=request), 
            'RAISE_COMROUND': reverse(RaiseModel.RAISE_COMROUND, request=request), 
            'RAISE_MTRIGHTS': reverse(RaiseModel.RAISE_MTRIGHTS, request=request), 
            'RAISE_EXIST_COM': reverse(RaiseModel.RAISE_EXIST_COM, request=request), 
            'RAISE_PRIVATEROUND': reverse(RaiseModel.RAISE_PRIVATEROUND, request=request), 
            'RAISE_UPLOAD_DOC': reverse(RaiseModel.RAISE_UPLOAD_DOC, request=request), 
            'STATUS': reverse(RaiseModel.STATUS, request=request), 
            'COMMENTS': reverse(RaiseModel.COMMENTS, request=request), 
            'DESCRIPTION': reverse(RaiseModel.DESCRIPTION, request=request), 
            'CREATED_USER': reverse(RaiseModel.CREATED_USER, request=request), 
            'CREATED_DATE': reverse(RaiseModel.CREATED_DATE, request=request), 
            'MODIFIED_USER': reverse(RaiseModel.MODIFIED_USER, request=request), 
            'MODIFIED_DATE': reverse(RaiseModel.MODIFIED_DATE, request=request) 
            })
        
        
        
@api_view(['GET', 'POST', 'DELETE'])
def Raise_list(request):
    
    # GET list of signup, POST a new user, DELETE all tutori
  if request.method == 'GET':
         
        raisedets = RaiseModel.objects.all()
        
        EMAIL = request.GET.get('EMAIL', None)
        if EMAIL is not None:
            raisedets = raisedets.filter(EMAIL__icontains=EMAIL)
        
        raise_serializer = RaiseSerializer(raisedets, many=True)  
        return JsonResponse(raise_serializer.data, safe=False)
 
  elif request.method == 'POST':
        # html_content = "<p>That's <strong>the HTML part</strong></p>"
        print(request.GET.get('EMAIL', None))
        raise_serializer = RaiseSerializer(data=request.data)
        if  raise_serializer.is_valid():
            raise_serializer.save()
            # EMAIL = request.POST.get('EMAIL', None) 
            # html_content = "<h1>Hi<strong>,We have received your application!</strong></h1>"
            # send_mail('Myntinvest:Application To Raise Capital',html_content,settings.EMAIL_HOST_USER,[EMAIL,settings.EMAIL_HOST_USER],fail_silently=False)  
            return JsonResponse(raise_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(raise_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  elif request.method == 'DELETE':
        count = RaiseModel.objects.all().delete()
        return JsonResponse({'message': '{} Application deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def Raise_detail(request, pk):
    try:
        raisedets = RaiseModel.objects.get(pk=pk)
    except RaiseModel.DoesNotExist:
        return JsonResponse({'message': 'The Application does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        print("4")
        raisedets_serializer = RaiseSerializer(raisedets)
        return JsonResponse(raisedets_serializer.data)
    
    elif request.method == 'PUT':
       
        # raisedets_data = JSONParser().parse(request)
        raisedets_serializer = RaiseSerializer(raisedets, data=request.data)
        
        if  raisedets_serializer.is_valid():
            raisedets_serializer.save()
            return JsonResponse(raisedets_serializer.data)
        return JsonResponse(raisedets_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        print("6")
        raisedets.delete()
        return JsonResponse({'message': 'Application was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
