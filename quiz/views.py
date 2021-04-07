import random

from django.contrib.auth.models import User, Group
from rest_framework import permissions, viewsets

from .models import Quiz, Sample2, Example, Commentary
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import QuizSerializer, UserSerializer, GroupSerializer, SampleSerializer, ExampleSerializer, \
    CommentarySerializer


# Create your views here.

@api_view(['GET'])
def helloAPI(request):
    sample = Sample2.objects.filter()
    serializer = SampleSerializer(sample, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def randomQuiz(request, id):
    totalQuizs = Quiz.objects.all()
    randomQuizs = random.sample(list(totalQuizs), id)
    serializer = QuizSerializer(randomQuizs, many=True)
    return Response(serializer.data)


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.filter().order_by('?')[:4]
    serializer_class = QuizSerializer


class helloViewSet(viewsets.ModelViewSet):
    queryset = Sample2.objects.all()
    serializer_class = SampleSerializer


class ExampleViewSet(viewsets.ModelViewSet):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer


class CommentaryViewSet(viewsets.ModelViewSet):
    queryset = Commentary.objects.all()
    serializer_class = CommentarySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
