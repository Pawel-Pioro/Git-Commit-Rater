from django.db import models

class CommitMessage(models.Model):
    commit_message = models.CharField(max_length=1024)
    rate = models.CharField(null=True, max_length=500)
    key = models.IntegerField(null=True)

class Scenario(models.Model):
    scenario = models.CharField(max_length=1024)
    language = models.CharField(max_length=20)
    project_topic = models.CharField(max_length=1024)
