from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import urls
from .database.database import query_dataset


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_dataset_data(request, dataset_id):
    return JsonResponse(query_dataset(dataset_id=dataset_id), safe=False)