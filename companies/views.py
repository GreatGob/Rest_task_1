from django.http import Http404

from .models import Company, Employee, Detail
from .serializers import CompanySerializer, EmployeeSerializer, DetailSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class CompanyList(APIView):

    def get(self, request, format= None):
        companies= Company.objects.all()
        serializer= CompanySerializer(companies, many= True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer= CompanySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

class CompanyDetails(APIView):
    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return Http404

    def get(self, request, pk, format= None):
        companies= self.get_object(pk)
        serializer= CompanySerializer(companies, many= True)
        return Response(serializer.data)

    def put(self, request, pk, format= None):
        companies= self.get_object(pk)
        serializer= CompanySerializer(companies, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)  
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format= None):
        companies= self.get_object(pk)
        companies.delete()
        return Response(status.HTTP_204_NO_CONTENT)



class EmployeeList(APIView):
    def get(self, request, format= None):
        employees= EmployeeSerializer.objects.all()
        serializer= EmployeeSerializer(employees, many= True)
        return Response(serializer.data)

    def post(self, request, format= None):
        serializer= EmployeeSerializer(data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

class EmployeeDetails(APIView):
    def get_object(self, pk):
        employees= Employee.objects.get(pk=pk)
        serializer= EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def get(self, request, pk, format= None):
        employees= self.get_object(pk)
        serializer= EmployeeSerializer(employees, many= True)
        return Response(serializer.data)

    def put(self, request, pk, format= None):
        employees= self.get_object(pk)
        serializer= EmployeeSerializer(employees, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)  
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format= None):
        employees= self.get_object(pk)
        employees.delete()
        return Response(status.HTTP_204_NO_CONTENT)


class DetailList(APIView):
    def get(self, request, *args, **kwargs):
        details= Detail.objects.all()
        serializer= DetailSerializer(details, many= True)
        return Response(serializer.data)    

    def post(self, request, *args, **kwargs):
        serializer= DetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)   

class DetailDetail(APIView):
    def get_object(self, pk):
        try:
            return Detail.objects.get(pk=pk)
        except Detail.DoesNotExist:
            raise Http404  
        
    def get(self, request, pk, format= None):
        details= self.get_object(pk)
        serializer= DetailSerializer(details)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        details= self.get_object(pk)
        serializer= DetailSerializer(details, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        details= self.get_object(pk)
        details.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
        
