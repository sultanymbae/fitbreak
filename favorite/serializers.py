from rest_framework import serializers
from .models import Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    '''взаимосвязи между моделью упражнения и пользовательской моделью'''
    users = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Exercise
        fields = 'title description'.split()