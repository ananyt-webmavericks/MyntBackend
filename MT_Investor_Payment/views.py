from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
 
from MT_Investor_Payment.models import PaymentModel
from MT_Investor_Payment.serializers import PaymentSerializer
from rest_framework.decorators import api_view


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, args, *kwargs):
        return Response({
            'COMPANY_INVESTED_IN': reverse(PaymentModel.COMPANY_INVESTED_IN, request=request),
            
            })            
      
from MT_Investor_Payment.models import PaymentModel
@api_view(['GET', 'POST', 'DELETE'])
def Payment_list(request):
    # GET list of signup, POST a new user, DELETE all tutori
  if request.method == 'GET':
        payment = PaymentModel.objects.all()
        
        COMPANY_INVESTED_IN = request.GET.get('COMPANY_INVESTED_IN', None)
        if COMPANY_INVESTED_IN is not None:
            payment= payment.filter(INV_BANK_ACC_NUMBER__icontains=COMPANY_INVESTED_IN)
        
        payment_serializer = PaymentSerializer(payment, many=True)
        return JsonResponse(payment_serializer.data, safe=False)
 
  elif request.method == 'POST':
        payment_data = JSONParser().parse(request)
        payment_serializer = PaymentSerializer(data=payment_data)
        if payment_serializer.is_valid():
            payment_serializer.save()
            return JsonResponse(payment_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(payment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  elif request.method == 'DELETE':
        count = PaymentModel.objects.all().delete()
        return JsonResponse({'message': '{} Payment deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def Payment_detail(request, pk):
    try: 
        payment = PaymentModel.objects.get(pk=pk) 
    except PaymentModel.DoesNotExist: 
        return JsonResponse({'message': 'The Payment does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        payment_serializer = PaymentSerializer(payment_serializer) 
        return JsonResponse(payment_serializer.data) 
 
    elif request.method == 'PUT': 
        payment_data = JSONParser().parse(request) 
        payment_serializer = PaymentSerializer(payment_data, data=payment_data) 
        if payment_serializer.is_valid(): 
            payment_serializer.save() 
            return JsonResponse(payment_serializer.data) 
        return JsonResponse(payment_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        payment.delete() 
        return JsonResponse({'message': 'Payment deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)




