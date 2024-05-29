from rest_framework.decorators import api_view
from .serializers import CommitSerializer, ScenarioSerializer
from .models import CommitMessage, Scenario
from rest_framework.response import Response


def ai_function() -> dict:
    result = {"scenario":"Some change has happened", "code":"import random"}
    return result

def rate_message(message:str, scenario:int) -> dict:
    #rating code ....
    return {"rate":9.0, "feedback":"Some gebbirish"}

@api_view(["GET"])
def generate_scenario(request):
    scenario = ai_function()
    instance = Scenario.objects.create(scenario=scenario['scenario'], code=scenario['code'])
    serializer = ScenarioSerializer(instance=instance)
    return Response(serializer.data)

@api_view(["POST"])
def commit_message(request):
    message = request.data 
    serializer = CommitSerializer(data=message)
    if serializer.is_valid(raise_exception=True):
        message = serializer.save()
        result = rate_message(message.commit_message, message.scenario.pk)
        message.rate = result['rate']
        return Response(result)
    return Response({"Error":"bad request"}, status=400)
    