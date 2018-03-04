from rest_framework import serializers
from .models import Foo
from django.contrib.auth.models import User


class FooSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Foo
        fields = ('bar', )
