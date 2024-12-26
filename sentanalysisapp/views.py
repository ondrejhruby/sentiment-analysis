from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.templatetags.static import static
from .sentimentanalysis import analyze_sentiment
import json

def analyze_page(request):
    context = {
        'happy_image_url': static('images/happy.png'),
        'neutral_image_url': static('images/neutral.png'),
        'sad_image_url': static('images/sad.png')
    }
    return render(request, 'sentanalysisapp/analyze.html', context)

@csrf_exempt
def analyze_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        text = data['text']
        sentiment_scores = analyze_sentiment(text)
        response = {'sentiment_scores': sentiment_scores}
        return JsonResponse(response)