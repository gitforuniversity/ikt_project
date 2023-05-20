from django.shortcuts import render
from home.models import *
# Create your views here.

# Website Navbar Sections

# Website Normal pages.
 
def home(request):
    context = {
        'courses':Course.objects.all(),
        'events':Event.objects.all(),
        'teachers': Teacher.objects.all(),
        'blogs':Blog.objects.all(),
    }

    return render(request=request, template_name='index.html', context=context)

def about(request):
    context = {
        'teachers':Teacher.objects.all(),
    }
    return render(request=request, template_name='about.html', context=context)

def research(request):
    context = {
        'researchs':Research.objects.all()
    }
    return render(request=request, template_name='research.html', context=context)

def scholarship(request):
    context = {
        'scholarships':Scholarship.objects.all()
    }
    return render(request=request, template_name='scholarship.html', context=context)

# Website Single and Normal pages.

def courses(request, slug=None):
    data = Course.objects.all()
    if slug:
        data = Course.objects.filter(category__slug = slug)

    context = {
        'courses':data,
    }
    return render(request=request, template_name='courses.html', context=context)

def course_single(request, slug):
    context = {
        'course':Course.objects.get(slug = slug),
        'data':Course.objects.all(),
    }
    return render(request=request, template_name='course-single.html', context=context)


def events(request):
    context = {
        'events':Event.objects.all()
    }
    return render(request=request, template_name='events.html', context=context)

def event_single(request, slug):
    context = {
        'event': Event.objects.get(slug = slug),
        'data': Event.objects.all()
    }
    return render(request=request, template_name='event-single.html', context=context)


def blogs(request):
    context = {
        'blogs':Blog.objects.all()
    }
    return render(request=request, template_name='blog.html', context=context)

def blog_single(request, slug):
    context = {
        'blog': Blog.objects.get(slug = slug),
        'data': Blog.objects.all()
    }
    return render(request=request, template_name='blog-single.html', context=context)


def notices(request):
    context = {
        'notices':Notice.objects.all()
    }
    return render(request=request, template_name='notice.html', context=context)

def notice_single(request ,slug):
    context = {
        'notice': Notice.objects.get(slug = slug),
        'data': Notice.objects.all()
    }
    return render(request=request, template_name='notice-single.html', context=context)


def teachers(request, slug=None):
    data = Teacher.objects.all()
    if slug:
        data = Teacher.objects.filter(category__slug = slug)

    context = {
        'teachers':data,
    }
    return render(request=request, template_name='teacher.html', context=context)

def teacher_single(request, slug):
    context = {
        'teacher': Teacher.objects.get(slug = slug),
        'data': Course.objects.all()
    }
    return render(request=request, template_name='teacher-single.html', context=context) 




