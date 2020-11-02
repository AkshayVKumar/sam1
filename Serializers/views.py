from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from Serializers.models import SampleModel
from Serializers.serializers import HelloSerializer

# Create your views here.
class HelloAPIView(APIView):
    serializer_class=HelloSerializer
    """The get method is responsible for handling the get requests"""

    def get(self,request,pk=None,format=None):
        #always response should be in the form of dictionary
        if pk==None:
            data=SampleModel.objects.values()
        else:
            data=SampleModel.objects.filter(id=pk).values()#will give you all the data in dictionary format
        return Response({'message':"Welcome to First Api demo",'request_type':'Get','data':data})

    def post(self,request,format=None):
        serializer_class_instance=self.serializer_class(data=request.data)
        if serializer_class_instance.is_valid():
            data=serializer_class_instance.validated_data
            usr=SampleModel.objects.get_or_create(name=data['name'],email=data['email'],gender=data['gender'])
        return Response({'message':"Welcome to First Api demo",'request_type':'POST','data':data})

    # def put(self,request,format=None):
    #     serializer_class_instance=self.serializer_class(data=request.data)
    #     if serializer_class_instance.is_valid():
    #         data=serializer_class_instance.validated_data
    #     return Response({'message':"Welcome to First Api demo",'request_type':'Put','data':data})

    # def patch(self,request,format=None):
    #     serializer_class_instance=self.serializer_class(data=request.data)
    #     if serializer_class_instance.is_valid():
    #         data=serializer_class_instance.validated_data
    #     return Response({'message':"Welcome to First Api demo",'request_type':'Patch','data':data})

    # def delete(self,request,format=None):
    #     return Response({'message':"Welcome to First Api demo",'request_type':'Delete'})
