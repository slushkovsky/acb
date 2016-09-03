from django.shortcuts import render
from rest_framework import filters
from rest_framework.generics import ListAPIView

from server.serializers import CarSerializer, InstructorSerializer, WaybillSerializer
from server.models import Car, Instructor, Waybill


class CarView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('mark', 'model')


class InstructorView(ListAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('car', )


class WaybillView(ListAPIView):
    queryset = Waybill.objects.all()
    serializer_class = WaybillSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('area', )
