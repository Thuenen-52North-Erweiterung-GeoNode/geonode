from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import CreateView
from django.core.files.storage import FileSystemStorage

from . import urls
from .database.database import query_dataset, get_column_definitions
from .ingestion.ingest import ingest_zipped_dataset

@require_http_methods(["GET", "POST"])
@csrf_exempt
def index(request):
    if (request.method == "POST"):
        return ingest_dataset(request)
    else:
        return JsonResponse({})

def get_dataset_definition(request, dataset_id):
    return JsonResponse(get_column_definitions(dataset_id=dataset_id), safe=False)

def get_dataset_data(request, dataset_id):
    params = request.GET
    size = extract_int_parameter(params, "size", 50)
    start = extract_int_parameter(params, "start", 0)
    
    f = parse_filters(params)
    s = parse_sorting(params)
   
    return JsonResponse(query_dataset(dataset_id=dataset_id, filters=f, start=start, size=size, sort=s), safe=False)


def extract_int_parameter(params, key, default_value):
    if (key in params and len(params[key]) == 1 and params[key][0].isnumeric()):
            return int(params[key][0])
    return default_value

def parse_filters(params):
    if ("filter" in params):
        filters_arr = params.getlist('filter')
        result = {}
        for f in filters_arr:
            kv = f.strip().split(":")
            result[kv[0]] = kv[1]
        return result

    return None

def parse_sorting(params):
    if ("sort" in params):
        sort = params.getlist('sort')[0].strip()
        kv = sort.split(";")
        asc = True
        if (len(kv) > 1):
            if (kv[1] == "desc"):
                asc = False
        result = {
            "sort": kv[0],
            "ascending": asc
        }
        
        return result

    return None

def ingest_dataset(request):
    
    myfile = request.FILES['file']
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    
    ingested_dataset_id = ingest_zipped_dataset(f"{fs.location}/{filename}")
    return JsonResponse({"id": ingested_dataset_id})

