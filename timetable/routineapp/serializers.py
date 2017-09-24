from rest_framework import serializers
from .models import subject


class subjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = subject
        fields= ('value',)
