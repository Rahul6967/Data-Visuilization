from django.shortcuts import render
from django.http import JsonResponse
from api.models import blackcoffer

def graph(request):
    queryset = blackcoffer.objects.all()
    dct = {
        "end_year": [],
        "intensity": [],
        "sector": [],
        "topic": [],
        "insight": [],
        "url": [],
        "region": [],
        "start_year": [],
        "impact": [],
        "added": [],
        "published": [],
        "country": [],
        "relevance": [],
        "pestle": [],
        "source": [],
        "title": [],
        "likelihood": [],
    }
    for item in queryset:
        dct['end_year'].append(item.end_year)
        dct['intensity'].append(item.intensity)
        dct['sector'].append(item.sector)
        dct['topic'].append(item.topic)
        dct['insight'].append(item.insight)
        dct['url'].append(item.url)
        dct['region'].append(item.region)
        dct['start_year'].append(item.start_year)
        dct['impact'].append(item.impact)
        dct['added'].append(item.added)
        dct['published'].append(item.published)
        dct['country'].append(item.country)
        dct['relevance'].append(item.relevance)
        dct['pestle'].append(item.pestle)
        dct['source'].append(item.source)
        dct['title'].append(item.title)
        dct['likelihood'].append(item.likelihood)

    return JsonResponse(dct)


def table(request):
    queryset=blackcoffer.objects.all()
    dct={
        "chart":[]
    }
    for item in queryset:
        chart_item={
        "end_year": item.end_year,
        "intensity": item.intensity,
        "sector": item.sector,
        "topic": item.topic,
        "insight": item.insight,
        "url": item.url,
        "region": item.region,
        "start_year": item.start_year,
        "impact": item.impact,
        "added": item.added,
        "published": item.published,
        "country": item.country,
        "relevance": item.relevance,
        "pestle": item.pestle,
        "source": item.source,
        "title": item.title,
        "likelihood": item.likelihood,
        }
        dct['chart'].append(chart_item)
    return JsonResponse(dct)