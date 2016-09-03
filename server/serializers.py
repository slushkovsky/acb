from rest_framework.serializers import ModelSerializer
from .models import Car, Waybill, Instructor


class CarSerializer(ModelSerializer):
    class Meta:
        model = Car


class WaybillSerializer(ModelSerializer):
    class Meta:
        model = Waybill


class InstructorSerializer(ModelSerializer):
    class Meta:
        model = Instructor
        
    car = CarSerializer()
    waybills = WaybillSerializer(many=True)

