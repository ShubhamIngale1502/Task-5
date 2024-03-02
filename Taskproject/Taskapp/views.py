from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import PersonSerializer
from .models import Person
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
import logging

logger = logging.getLogger('mylogger')


class PersonAPI(APIView):
    
    def get(self,request):
        try:
            data = Person.objects.all()
            serializer = PersonSerializer(data, many=True)
            logger.info('Data Festched SuccessFully')
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        except:
            logger.error('Data Featchin error')
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):
        try:
            serializer = PersonSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            logger.info('Data Saved SuccessFully')
            return Response(data=serializer.data, status=status.HTTP_201_CREATED) 
        except:
            logger.error('Error in Data Submitting')
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class DetailsAPI(APIView):
    
    def get(self,request,pk):
        try:
            data = get_object_or_404(Person,pk=pk)
            serializer = PersonSerializer(data)
            logger.info('Data Festched SuccessFully')
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except:
            logger.error('Data Featchin error')
            return Response(data={'details':'Getting Error in featching data'})
        
    def put(self,request,pk):
        try:
            data = get_object_or_404(Person,pk=pk)
            serializer = PersonSerializer(data=request.data, instance=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            logger.info('Data Updated SuccessFully')
            return Response(data=serializer.data,status=status.HTTP_205_RESET_CONTENT)
        except:
            logger.error('Error in data Updating')
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self,request,pk):
        try:
            obj = get_object_or_404(Person,pk=pk)
            serializer = PersonSerializer(data=request.data, instance=obj, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            logger.info('Data Updated SuccessFully')
            return Response(data=serializer.data,status=status.HTTP_206_PARTIAL_CONTENT)
        except Exception as e:
            print(e)
            logger.error('Error in data Updating')
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        data = get_object_or_404(Person,pk=pk)
        data.delete()
        logger.info('Data Deleted  SuccessFully')
        return Response(data=None,status=status.HTTP_204_NO_CONTENT)