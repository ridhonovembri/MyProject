from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title':'Department List',
        'nav':[
            ['/','Home'],
            ['/hrdept/','Index'],
            ['/hrdept/add','Add'],
            ['/hrdept/update','Update'],
            ['/hrdept/delete','Delete'],
        ],
        'banner':'hrdept/img/banner_blog.png',
        'app_css':'hrdept/css/styles.css',
    }

    return render(request,'index.html',context)

def add(request):
    context = {
        'title': 'Department Add',
        'nav':[
            ['/','Home'],
            ['/hrdept/','Index'],
            ['/hrdept/add','Add'],
            ['/hrdept/update','Update'],
            ['/hrdept/delete','Delete'],
        ],
        'banner':'hrdept/img/banner_blog.png',
        'app_css':'hrdept/css/styles.css',
    }

    return render(request,'index.html',context)

def update(request):
    context = {
        'title':'Department Update',
        'nav':[
            ['/','Home'],
            ['/hrdept/','Index'],
            ['/hrdept/add','Add'],
            ['/hrdept/update','Update'],
            ['/hrdept/delete','Delete'],
        ],
        'banner':'hrdept/img/banner_blog.png',
        'app_css':'hrdept/css/styles.css',
    }

    return render(request,'index.html',context)

def delete(request):
    context = {
        'title': 'Department Delete',
        'nav':[
            ['/','Home'],
            ['/hrdept','Index'],
            ['/hrdept/add','Add'],
            ['/hrdept/update','Update'],
            ['/hrdept/delete','Delete'],
        ],
        'banner':'hrdept/img/banner_blog.png',
        'app_css':'hrdept/css/styles.css',
    }

    return render(request,'index.html',context)