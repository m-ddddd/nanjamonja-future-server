from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=100)
    highest_score = models.IntegerField(default=0)
    participant_count = models.IntegerField(default=0)


class Character(models.Model):
    content = models.BinaryField(max_length=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Parts(models.Model):
    content = models.BinaryField(max_length=None)
    parts_type = models.IntegerField()
