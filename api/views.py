from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from . import spider

def index(request):
    if request.method == "GET":
        return HttpResponse("Hello API")


def hadoop_status(request):
    if request.method=="GET":
        result = spider.crawl_hadoop_status()
        return HttpResponse(result)


def hadoop_node_status(request):
    result = spider.crawl_hadoop_info()
    return HttpResponse(result)


def db_status(request):
    if request.method == "GET":
        result = spider.crawl_db(target="status")

        return HttpResponse(result)


def db_log(request):
    if request.method == "GET":
        result = spider.crawl_db(target="log")
        return HttpResponse(result)