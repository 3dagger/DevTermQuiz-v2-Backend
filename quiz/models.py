from django.db import models

# Create your models here.
class Sample2(models.Model):
    quiz = models.CharField(max_length=100, blank=True)


class Quiz(models.Model):
    test = models.ForeignKey(Sample2, related_name='tracks', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    answer = models.IntegerField()
    subtitle = models.CharField(max_length=144, blank=True)

    def __str__(self):
        return f"{self.test}"