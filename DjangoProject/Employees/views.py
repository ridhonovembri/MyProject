from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title':'Employee Management System',
        'nav':[
            ['/','Home'],
            ['hremployee/','Employee'],
            ['hrdept/','Department']
        ],
        'banner':'img/banner_home.png',

    }

    return render(request,'index.html', context)