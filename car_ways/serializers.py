from rest_framework.serializers import ModelSerializer
from .models import Car, Waybill, Employe


class CarSerializer(ModelSerializer):
    class Meta:
        model = Car


class WaybillSerializer(ModelSerializer):
    class Meta:
        model = Waybill


class EmployeSerializer(ModelSerializer):
    car = CarSerializer()
    waybills = WaybillSerializer(many=True)

    class Meta:
        model = Employe
