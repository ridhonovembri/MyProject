from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        'title':'Employee List',
        'nav':[
            ['/','Home'],
            ['/hremployee/','Index'],
            ['/hremployee/add','Add'],
            ['/hremployee/update','Update'],
            ['/hremployee/delete','Delete'],
        ],
        'banner':'hremployee/img/banner_about.png',
        'app_css':'hremployee/css/styles.css',
    }

    return render(request,'hremployee/index.html',context)

def add(request):
    context = {
        'title':'Employee Add',
        'nav':[
            ['/','Home'],
            ['/hremployee/','Index'],
            ['/hremployee/add','Add'],
            ['/hremployee/update','Update'],
            ['/hremployee/delete','Delete'],
        ],
        'banner':'hremployee/img/banner_about.png',   
        'app_css':'hremployee/css/styles.css',    
    }

    return render(request,'hremployee/index.html',context)

def update(request):
    context = {
        'title':'Employee Update',
        'nav':[
            ['/','Home'],
            ['/hremployee/','Index'],
            ['/hremployee/add','Add'],
            ['/hremployee/update','Update'],
            ['/hremployee/delete','Delete'],
        ],
        'banner':'hremployee/img/banner_about.png',
        'app_css':'hremployee/css/styles.css',
    }

    return render(request,'hremployee/index.html',context)

def delete(request):
    context = {
        'title':'Employee Delete',
        'nav':[
            ['/','Home'],
            ['/hremployee','Index'],
            ['/hremployee/add','Add'],
            ['/hremployee/update','Update'],
            ['/hremployee/delete','Delete'],
        ],
        'banner':'hremployee/img/banner_about.png',
        'app_css':'hremployee/css/styles.css',
    }

    return render(request,'hremployee/index.html',context)