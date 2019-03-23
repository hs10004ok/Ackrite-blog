from django.shortcuts import render

def index(request):
    return render(request, 'blog/index.html', {})

from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('blog/index.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
