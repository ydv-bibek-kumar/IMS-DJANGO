from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from .models import product, productCategory
from .serializers import productserializers, productCategorySerializer
from rest_framework.response import Response

# Create your views here.
class productApiview(ModelViewSet):
    queryset = product.objects.all()
    serializer_class = productserializers


class productCategoryApiView(GenericAPIView):
    queryset = productCategory.objects.all()
    serializer_class = productCategorySerializer

    def get(self,request):
        product_category_objs = self.get_queryset()
        serializer = self.serializer_class(product_category_objs,many=True)
        # serializer.data
        return Response(serializer.data)
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        
class productCategoryDetailApiView(GenericAPIView):
    queryset = productCategory.objects.all()
    serializer_class = productCategorySerializer

    def get(self,request,pk):
        try:
            object = productCategory.objects.get(id=pk)
        except:
              return Response('data not found!')
        serializer = self.serializer_class(object)
        return Response(serializer.data)

    def put(salf,request,pk):

        try:
            object = productCategory.objects.get(id=pk)
        except:
              return Response('data not found!')
        serializer = salf.serializer_class(object,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response ('Data update!')
        else:
            return Response(serializer.errors)
        
        
    def delete(self,request,pk):
        try:
            object = productCategory.objects.get(id=pk)
        except:
              return Response('data not found!')
        object.delete()
        return Response('Data deleted!')
