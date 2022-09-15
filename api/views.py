from django.shortcuts import render
from owner.models import Books
from rest_framework.views import APIView
from api.serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class BooksView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Books.objects.all()
        serializer=BookSerializer(qs,many=True)
        return Response(serializer.data)
    def post(self,request,*args,**kwargs):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

class BookDetails(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Books.objects.get(id=id)
        serializer=BookSerializer(qs)
        return Response(serializer.data)

    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Books.objects.get(id=id)
        serializer=BookSerializer(instance=qs,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Books.objects.get(id=id)
        qs.delete()
        return Response({"messages":"deleted"},status=status.HTTP_200_OK)
