from rest_framework import serializers
from django.contrib.auth.models import User, Group
from quiz.models import Quiz


# class ExampleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Example
#         fields = ('firstExample', 'secondExample', 'thirdExample', 'fourthExample',)
#
#
# class CommentarySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Commentary
#         fields = ('firstCommentary', 'secondCommentary', 'thirdCommentary', 'fourthCommentary',)


class QuizSerializer(serializers.ModelSerializer):
    # ex = ExampleSerializer(many=True)
    # comm = CommentarySerializer(many=True)

    class Meta:
        model = Quiz
        # fields = ('question', 'answer', 'ex', 'comm',)
        fields = '__all__'


# class SampleSerializer(serializers.ModelSerializer):
#     tracks = QuizSerializer(many=True)
#
#     class Meta:
#         model = Sample2
#         fields = ('tracks',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
