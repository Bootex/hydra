# Create your views here.
from django.http import HttpResponse
from django.template import loader
import os
from . import models
from .forms import LoginForm
import requests

def index(request):
    latest_todo_list = models.Todolist.objects.order_by('-start_date')[:5]
    context= {'latest_todo_list': latest_todo_list,}
    template = loader.get_template('dash/index.html')
    return HttpResponse(template.render(request=request,context=context))


def login(request):
    template = loader.get_template('dash/pages/login.html')
    form = LoginForm()
    return HttpResponse(template.render(request=request,context={'form':form}))


def login_check(request):
    if request.method == "POST":
        pass
    else:
        pass


def hadoop_status(request):
    template = loader.get_template('dash/pages/hadoop.html')
    result = requests.get('http://127.0.0.1:8000/api/hadoop_status')
    context = {"hadoop_status":result.content}
    return HttpResponse(template.render(request=request, context=context))


def hadoop_info(request):
    template = loader.get_template('dash/pages/hadoop.html')
    result = requests.get('http://127.0.0.1:8000/api/node_status')
    context = {"hadoop_status":result.content}
    return HttpResponse(template.render(request=request, context=context))


def hadoop_nnode_render(request):
    template = loader.get_template('dash/pages/hadoop.html')
    context = {}
    return HttpResponse(template.render(request=request, context=context))


def hadoop_snnode_render(request):
    template = loader.get_template('dash/pages/hadoop.html')
    context = {}
    return HttpResponse(template.render(request=request, context=context))


def hadoop_dnode_render(request):
    template = loader.get_template('dash/pages/hadoop.html')
    context = {}
    return HttpResponse(template.render(request=request, context=context))


def db_status(request):
    template = loader.get_template('dash/pages/database.html')
    logs = requests.get('http://127.0.0.1:8000/api/db_status')
    context = {"db_logs":logs.text}
    return HttpResponse(template.render(request=request, context=context))


def db_log(request):
    template = loader.get_template('dash/pages/database.html')
    logs = requests.get('http://127.0.0.1:8000/api/db_log')
    context = {"db_logs":logs.content}
    return HttpResponse(template.render(request=request,context=context))


def register(request):
    template = loader.get_template('dash/pages/register.html')
    return HttpResponse(template.render(request=request))


def todo(request):
    template = loader.get_template('dash/index.html')
    return HttpResponse(template.render(request=request))


def get_sysinfo():
    result = ''
    return result


if __name__ == "__main__":
    cpu_cmd = "mpstat | tail -1 | awk '{print 100-$13}'"
    hd_cmd = 'df -lh tail -2'

    cpu_info, hd_info = dict(), dict()

    cpu_info['used'] = os.popen(cpu_cmd).readline()

    print(cpu_info)