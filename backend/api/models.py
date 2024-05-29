from django.db import models

class CommitMessage(models.Model):
    commit_message = models.CharField(max_length=1024)
    scenario = models.ForeignKey("Scenario", on_delete=models.CASCADE)
    rate = models.IntegerField(null=True)


class Scenario(models.Model):
    code = models.CharField(max_length=1024)
    scenario = models.CharField(max_length=1024)
    language = models.CharField(max_length=20)
    project_topic = models.CharField(max_length=1024)
