from django.db import models


# Create your models here.
class Sample2(models.Model):
    quiz = models.CharField(max_length=100, blank=True)


class Quiz(models.Model):
    test = models.ForeignKey(Sample2, related_name='tracks', on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    # body = models.TextField()
    answer = models.IntegerField()
    # subtitle = models.CharField(max_length=144, blank=True)


class Example(models.Model):
    ex = models.ForeignKey(Quiz, related_name='ex', on_delete=models.CASCADE)
    ex_one = models.CharField(max_length=200)
    ex_two = models.CharField(max_length=200)
    ex_three = models.CharField(max_length=200)
    ex_four = models.CharField(max_length=200)


class Commentary(models.Model):
    comm = models.ForeignKey(Quiz, related_name='comm', on_delete=models.CASCADE)
    comm_one = models.CharField(max_length=200)
    comm_two = models.CharField(max_length=200)
    comm_three = models.CharField(max_length=200)
    comm_four = models.CharField(max_length=200)