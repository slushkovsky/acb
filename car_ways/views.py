from rest_framework import filters
from .models import Car, Employe, Waybill
from .serializers import CarSerializer, EmployeSerializer, WaybillSerializer
from rest_framework.generics import ListAPIView


class CarView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('mark', 'model')


class EmployeView(ListAPIView):
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('car', )


class WaybillView(ListAPIView):
    queryset = Waybill.objects.all()
    serializer_class = WaybillSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('area', )
