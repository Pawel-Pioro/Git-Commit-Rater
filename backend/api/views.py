from rest_framework.decorators import api_view
from .serializers import CommitSerializer, ScenarioSerializer
from .models import CommitMessage, Scenario
from rest_framework.response import Response

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
chrome_options = webdriver.ChromeOptions() 
chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36') 
chrome_options.add_argument('--headless') 
chrome_options.add_argument('--disable-gpu') 
chrome_options.add_argument('--incognito') 

def getAiResponse(prompt): 
    dr = webdriver.Chrome(options=chrome_options) 
    WebDriverWait(dr, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body'))) 
    dr.get("https://www.perplexity.ai/") 

    WebDriverWait(dr, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[placeholder^='Ask anything...']"))) 
    inputElement = dr.find_element(By.CSS_SELECTOR, "[placeholder^='Ask anything...']") 
    inputElement.send_keys(prompt) 
    inputElement.send_keys(Keys.ENTER) 
    WebDriverWait(dr, 40).until(EC.presence_of_element_located((By.XPATH, "//div[text()='Rewrite']"))) 

    all_spans = [] 
    notAllowed = [str(i) for i in range(10)] 
        
    for span in dr.find_elements(By.TAG_NAME, "span"): 
        all_spans.append(span.text) 
    dr.quit() 
    return " ".join(all_spans[6:-7]) 

def ai_function(language, topic):
    prompt = f"Generate a fake scenario where a git change in a code base written in {language} happened about {topic}. Return a few sentences about the scenario and the code. This will be used to ask the user to explain the code change"
    result = getAiResponse(prompt)
    return {"scenario": result}

def rate_message(message:str, scenario) -> dict:
    scenarioObj = Scenario.objects.get(pk=scenario)
    prompt = f"Using the following scenario: {scenarioObj.scenario[:250]} and the following commit message: '{message}', please rate the commit message on a scale of 1 to 10 and provide a short 50 word paragraph on improvement, keep it short and simple"
    result = getAiResponse(prompt)  

    return {"feedback": result}

@api_view(["POST"])
def generate_scenario(request):
    language, topic = request.data['language'], request.data['topic']
    scenario = ai_function(language, topic)
    instance = Scenario.objects.create(scenario=scenario['scenario'])
    serializer = ScenarioSerializer(instance=instance)
    return Response({**serializer.data, "key": instance.pk})

@api_view(["POST"])
def commit_message(request):
    userInput = request.data 
    serializer = CommitSerializer(data=userInput)
    if serializer.is_valid(raise_exception=True):
        message = serializer.save()
        result = rate_message(message.commit_message, message.key)
        message.rate = result['feedback']
        message.save()
        return Response(result)
    return Response({"Error":"bad request"}, status=400)
    