from django.db import models


# Create your models here.
# class Sample2(models.Model):
#     quiz = models.CharField(max_length=100, blank=True)


class Quiz(models.Model):
    # example = models.ForeignKey(Sample2, related_name='tracks', on_delete=models.CASCADE)
    question = models.CharField(max_length=500)
    answer = models.IntegerField()
    firstExample = models.CharField(max_length=2000, blank=True)
    secondExample = models.CharField(max_length=2000, blank=True)
    thirdExample = models.CharField(max_length=2000, blank=True)
    fourthExample = models.CharField(max_length=2000, blank=True)
    firstCommentary = models.CharField(max_length=2000, blank=True)
    secondCommentary = models.CharField(max_length=2000, blank=True)
    thirdCommentary = models.CharField(max_length=2000, blank=True)
    fourthCommentary = models.CharField(max_length=2000, blank=True)


# class Example(models.Model):
#     ex = models.ForeignKey(Quiz, related_name='ex', on_delete=models.CASCADE)
#     firstExample = models.CharField(max_length=2000, blank=True)
#     secondExample = models.CharField(max_length=2000, blank=True)
#     thirdExample = models.CharField(max_length=2000, blank=True)
#     fourthExample = models.CharField(max_length=2000, blank=True)
#
#
# class Commentary(models.Model):
#     comm = models.ForeignKey(Quiz, related_name='comm', on_delete=models.CASCADE)
#     firstCommentary = models.CharField(max_length=2000, blank=True)
#     secondCommentary = models.CharField(max_length=2000, blank=True)
#     thirdCommentary = models.CharField(max_length=2000, blank=True)
#     fourthCommentary = models.CharField(max_length=2000, blank=True)