from rest_framework import serializers
from .models import CommitMessage, Scenario

class CommitSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommitMessage
        fields = "__all__"

class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario
        fields = "__all__"