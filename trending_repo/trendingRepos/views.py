from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import datetime

@api_view(['GET'])
def trend_language(request):
    result= {}
    date = datetime.date.today() + datetime.timedelta(-30)
    response = requests.get('https://api.github.com/search/repositories?q=created:{}&sort=stars&order=desc&per_page=100'.format(date))
    items = response.json()['items']
    for item in items:
        lang= item["language"]
        if(lang is None):continue
        if lang in result:
            result[lang]["num_of_repos"]= result[lang]["num_of_repos"] + 1
            result[lang]["repos"].append(item["url"])
        else:
            result[lang] = {"num_of_repos":1, "repos":[item["url"]]}

    return Response(result)
