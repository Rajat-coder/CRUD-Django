  
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from authentication.serializers import *
from  authentication.models import *
from rest_framework import status

class MainView(APIView):
    model=None
    serializer=None

    #For Creating
    def post(self,request):
        output_status=False
        output_detail="Failed"
        res_status=status.HTTP_400_BAD_REQUEST
        data={}
        serializer=self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            output_status=True
            output_detail="Data Created Successfully"
            res_status=status.HTTP_200_OK
        else:
            output_detail=serializer.errors
        context={
            "status":output_status,
            "detail":output_detail,
            "data":serializer.data
        }
        return Response(context,status=res_status)
    
    #For getting data by it
    def get(self,request):
        model_id=request.GET.get("id",None)
        output_status=False
        output_detail="Failed"
        res_status=status.HTTP_400_BAD_REQUEST
        data={}
        model=self.model.objects.filter(pk=model_id).first()
        if model:
            serializer=self.serializer(model)
            serializer=serializer.data
            output_status=True
            output_detail="Success"
            res_status=status.HTTP_200_OK
        else:
            output_detail="Id doesnt exist"
        context={
            "status":output_status,
            "detail":output_detail,
            "data":serializer
        }
        return Response(context,status=res_status)

    #For deleting data
    def delete(self,request):
        model_id=request.GET.get("id",None)
        output_status=False
        output_detail="Failed"
        res_status=status.HTTP_400_BAD_REQUEST
        model=self.model.objects.filter(pk=model_id).first()
        if model:
            model.delete()
            output_status=True
            output_detail="Data Deleted"
            res_status=status.HTTP_200_OK
        else:
            output_detail="Id doesnt exist"
        context={
            "status":output_status,
            "detail":output_detail,
        }
        return Response(context,status=res_status)

    #For getting data by it
    def put(self,request):
        model_id=request.data.get("id",None)
        output_status=False
        output_detail="Failed"
        res_status=status.HTTP_400_BAD_REQUEST
        data={}
        model=self.model.objects.filter(pk=model_id).first()
        if model:
            serializer=self.serializer(model,data=request.data,partial = True)
            if serializer.is_valid():
                serializer.save()
                output_status=True
                output_detail="Data Changed Successfully"
                res_status=status.HTTP_200_OK
            else:
                output_detail=serializer.error
        else:
            output_detail="Id doesnt exist"
        context={
            "status":output_status,
            "detail":output_detail,
            "data":serializer.data
        }
        return Response(context,status=res_status)

    

        



class AudioBookView(MainView):
    model=Audiobook
    serializer=AudiobookSerializer

class SongView(MainView):
    model=Song
    serializer=SongSerializer

class PodcastView(MainView):
    model=Podcast
    serializer=PodcastSerializer

