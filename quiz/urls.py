from django.urls import path, include
from rest_framework import routers

from quiz import views
from quiz.views import randomQuiz, helloAPI

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'sample', views.helloViewSet)
router.register(r'quiz', views.QuizViewSet)
router.register(r'example', views.ExampleViewSet)
router.register(r'commentary', views.CommentaryViewSet)

urlpatterns = [
    path("hello/", helloAPI),
    path("<int:id>/", randomQuiz),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]