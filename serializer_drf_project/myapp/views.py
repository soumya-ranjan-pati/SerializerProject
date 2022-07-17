from copy import error
from email import message
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.generic import View
from myapp.serializers import ProductSerializer
from myapp.models import Product
import io

#Insert The Record
class ProductOperation(View):
      def post(self,request):
            byte_data=request.body#will gets to bytes
            stm_data=io.BytesIO(byte_data)#convert byte_data to streamdata
            dict_data=JSONParser().parse(stm_data)#convert stm_data to dictionary
            ps=ProductSerializer(data=dict_data)
            if ps.is_valid():
                  ps.save()
                  message={'message':'product is saved'}

            else:
                  message={'errors':ps.errors}      
            json_data=JSONRenderer().render(message)
            return HttpResponse(json_data,content_type='application/json')            

#Show All The Record
class showall(View):
      def get(self,request):
            ps=Product.objects.all()
            qs=ProductSerializer(ps,many=True)
            json_data=JSONRenderer().render(qs.data)
            return HttpResponse(json_data,content_type='application/json')

#Show Single Record
class singlerecord(View):
      def get(self,request):
            b_data=request.body            
            stream=io.BytesIO(b_data)
            d1=JSONParser().parse(stream)
            product_no=d1.get("product_no",None)
            if product_no:
                  try:
                        res=Product.objects.get(no=product_no)
                        ps=ProductSerializer(res)
                        json_data=JSONRenderer().render(ps.data)
                  except Product.DoesNotExist:
                        message={'error':'Invalid Product Number'}
                        json_data=JSONRenderer().render(message)   
                  return HttpResponse(json_data,content_type='application/json')

            else:
                  message={'errors':'Invalid Product Number'}      
                  json_data=JSONRenderer().render(message)
                  return HttpResponse(json_data,content_type='application/json')

# Update The Record
class Updaterecord(View):
      def put(self,request):
            b_data=request.body
            stream_data=io.BytesIO(b_data)
            d1=JSONParser().parse(stream_data)
            product_no=d1.get("no",None)
            if product_no:
                  try:
                        res=Product.objects.get(no=product_no)
                        ps=ProductSerializer(res,d1,partial=True)
                        if ps.is_valid():
                              ps.save()
                              message={'message':'Product Is Updated'}
                              json_data=JSONRenderer().render(message)
                        else:
                              message={'error':ps.errors}
                              json_data=JSONRenderer().render(message)

                  except Product.DoesNotExist:
                        message={'error':'Invalid Product Number'}
                        json_data=JSONRenderer().render(message) 
            else:
                  message={'error':'provide product Number'}
                  json_data=JSONRenderer().render(message)                       
            return HttpResponse(json_data,content_type='application/json')            

class Deleterecord(View):
      def delete(self,request):
            byte_data=request.body            
            stream_data=io.BytesIO(byte_data)
            d1=JSONParser().parse(stream_data)
            product_no=d1.get("no")
            if product_no:
                  no_of_rows=Product.objects.filter(no=product_no).delete()
                  if no_of_rows[0] !=0:
                        message={'message':'product is deleted'}
                  else:
                        message={'error':'Plz..Check The Product Number'}
            else:
                  message={'error':'Plz...Provide Product Number'}                  
            json_data=JSONRenderer().render(message)
            return HttpResponse(json_data,content_type='application/json')      
