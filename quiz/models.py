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


class VersionCheck(models.Model):
    android_version = models.CharField(max_length=1000, blank=True)
    android_msg = models.CharField(max_length=1000, blank=True)
    android_status = models.CharField(max_length=1000, blank=True)
    ios_version = models.CharField(max_length=1000, blank=True)
    ios_msg = models.CharField(max_length=1000, blank=True)
    ios_status = models.CharField(max_length=1000, blank=True)
