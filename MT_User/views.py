from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.http import HttpResponse 
from MT_User.models import SignupModel
from MT_User.serializers import SignupSerializer
from rest_framework.decorators import api_view


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'FIRSTNAME': reverse(SignupModel.FIRSTNAME, request=request),
            'LASTNAME': reverse(SignupModel.LASTNAME, request=request),
            'EMAIL': reverse(SignupModel.EMAIL, request=request),
            'PASSWORD': reverse(SignupModel.PASSWORD, request=request),
            'ROLE': reverse(SignupModel.ROLE, request=request),
            })            
      
from MT_User.models import SignupModel
@api_view(['GET', 'POST', 'DELETE'])
def mtuser_list(request):
    # GET list of signup, POST a new user, DELETE all tutori
  if request.method == 'GET':
        signup = SignupModel.objects.all()
        
        FIRSTNAME = request.GET.get('FIRSTNAME', None)
        if FIRSTNAME is not None:
            signup = signup.filter(FIRSTNAME__icontains=FIRSTNAME)
        
        signup_serializer = SignupSerializer(signup, many=True)
        return JsonResponse(signup_serializer.data, safe=False)
 
  elif request.method == 'POST':
        signup_data = JSONParser().parse(request)
        signup_serializer = SignupSerializer(data=signup_data)
        if signup_serializer.is_valid():
            signup_serializer.save()
            return JsonResponse(signup_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(signup_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  elif request.method == 'DELETE':
        count = SignupModel.objects.all().delete()
        return JsonResponse({'message': '{} User were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def mtuser_detail(request, pk):
    try: 
        signup = SignupModel.objects.get(pk=pk) 
    except SignupModel.DoesNotExist: 
        return JsonResponse({'message': 'The User does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        signup_serializer = SignupSerializer(signup) 
        return JsonResponse(signup_serializer.data) 
 
    elif request.method == 'PUT': 
        signup_data = JSONParser().parse(request) 
        signup_serializer = SignupSerializer(signup, data=signup_data) 
        if signup_serializer.is_valid(): 
            signup_serializer.save() 
            return JsonResponse(signup_serializer.data) 
        return JsonResponse(signup_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        signup.delete() 
        return JsonResponse({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST', 'DELETE'])
def userlogin(request):
    if request.method == 'GET':
        signup = SignupModel.objects.all()  
        EMAIL = request.GET.get('EMAIL', None) 
        PASSWORD = request.GET.get('PASSWORD', None)
        mydata = signup.filter(EMAIL=EMAIL,PASSWORD=PASSWORD).values()
        print("mydata",mydata)
        # print(signup.filter(EMAIL=EMAIL,PASSWORD=PASSWORD).values())
        for result in mydata: 
            context={
                "MESSAGE":"Logged in successfully",
                "ROLE":result['ROLE'],
                "EMAIL":result['EMAIL'],
                "FIRSTNAME":result['FIRSTNAME'],
                "MODULE":result['MODULE'],
                "MT_USERID":result['id'],
            } 
            request.session['loguser'] = result['FIRSTNAME'] 
            request.session['logemail'] = result['EMAIL']
            request.session['logrole'] = result['ROLE']
            request.session['logmodule'] = result['MODULE'] 
        if signup.filter(EMAIL=EMAIL) and signup.filter(PASSWORD=PASSWORD): 
            return JsonResponse(context, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({'MESSAGE': 'The User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        

@api_view(['GET', 'POST', 'DELETE'])
def chkEmailExist(request):
    if request.method == 'GET':
        signup = SignupModel.objects.all() 
        EMAIL = request.GET.get('EMAIL', None)  
        if signup.filter(EMAIL__icontains=EMAIL): 
            return JsonResponse({'MESSAGE': 'TRUE'}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({'MESSAGE': 'FALSE'}, status=status.HTTP_404_NOT_FOUND)

def setUserSession(request,mydata):
     for result in mydata:  
        request.session['loguser'] = result['FIRSTNAME'] 
        request.session['logemail'] = result['EMAIL']
        request.session['logrole'] = result['ROLE']
        request.session['logmodule'] = result['MODULE']   
        return HttpResponse("session is set")  
def getsession(request):  
    loggeduser = request.session['loguser']  
    loggedemail = request.session['logemail']  
    loggedrole=request.session['logrole']
    loggedmodule=request.session['logmodule']
    return HttpResponse(loggeduser+" "+loggedemail+""+loggedrole+""+loggedmodule+"");  