from rest_framework import serializers
from django.contrib.auth.models import User, Group
from quiz.models import Quiz, VersionCheck


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class VersionCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = VersionCheck
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
