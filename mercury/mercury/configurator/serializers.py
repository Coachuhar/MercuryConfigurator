from .models import System_lens_medium, System_lens_135, Component, Formula
from rest_framework import serializers



class MediumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = System_lens_medium
        fields = "__all__"
        


class System_135Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = System_lens_135
        fields = '__all__'


class ComponentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Component
        fields = '__all__'

class FormulaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Formula
        fields = '__all__'
       