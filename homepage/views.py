from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import BlogForm, CalendarForm, ListForm, LoginForm, RegisterForm
from django.utils import timezone
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    ''' homepage view '''
    club_list = Club.objects.all()
    notice_list = Notice.objects.order_by('-pub_date')
    manual_list = Manual.objects.order_by('-pub_date')
    
    a = List.objects.none()
    b = Calendar.objects.none()
    for club in club_list:
        l = club.list.all()
        if l.exists():
            a = a.union(l, all=True)
        c = club.calendar.all()
        if c.exists():
            b = b.union(c, all=True)
    
    if a.exists():
        a = a.order_by('due_date')
    if b.exists():
        b = b.order_by('start_day')
    
    c = []
    i, j = 0, 0
    while True:
        if i == len(a):
            c.extend(b[j:])
            break
        elif j == len(b):
            c.extend(a[i:])
            break

        if a[i].due_date >= b[j].start_day:
            c.append(b[j])
            j += 1
        elif a[i].due_date < b[j].start_day:
            c.append(a[i])
            i += 1

    content = { "clubs": club_list,
                "notices": notice_list,
                "manuals": manual_list,
                "festivals": c}

    return render(request,'homepage/home.html', content)

def notice(request, id):
    ''' manual view '''
    notice = get_object_or_404(Notice, id=id)
    contents = {"content": notice}
    return render(request, 'homepage/posting.html', contents)

def manual(request, id):
    ''' manual view '''
    manual = get_object_or_404(Manual, id=id)
    contents = {"content": manual}
    return render(request, 'homepage/posting.html', contents)

def club_main(request, club_id):
    ''' club main page '''
    club = get_object_or_404(Club, pk=club_id)
    blog_page = request.GET.get("blog_page")
    blog_list = club.blog.all().order_by('-update_date')
    blog_paginator = Paginator(blog_list, 5)
    blog_obj = blog_paginator.get_page(blog_page)
    calendar_page = request.GET.get("calendar_page")
    calendar_list = club.calendar.all().order_by('start_day')
    calendar_paginator = Paginator(calendar_list, 2)
    calendar_obj = calendar_paginator.get_page(calendar_page)
    list_page = request.GET.get("list_page")
    list_list = club.list.all().order_by('due_date')
    list_paginator = Paginator(list_list, 2)
    list_obj = list_paginator.get_page(list_page)
    context = {'club' : club, 'blog_list' : blog_obj, 'calendar_list' : calendar_obj, 'list_list' : list_obj}
    return render(request, 'club/club_main.html', context)

def blog(request, club_id, blog_id):
    ''' club blog page '''
    blog = get_object_or_404(Blog, id=blog_id) # 왜 되는지 모르겠는데 그냥 되네, 이해해보자
    blog.view_count += 1
    blog.save()
    context = {'blog' : blog}
    return render(request, 'club/blog_detail.html', context)

def blog_create(request, club_id):
    ''''''
    club = get_object_or_404(Club, pk=club_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.update_date = timezone.now()
            blog.club = club
            blog.save()
            return redirect('club_main', club_id=club.id)
    else:
        form = BlogForm()
    context = {'form' : form}
    return render(request, 'club/blog_form.html', context)

def blog_modify(request, club_id, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('club_main', club_id=club_id)
    else:
        form = BlogForm(instance=blog)
    context = {'form': form}
    return render(request, 'club/blog_form.html', context)

def blog_delete(request, club_id, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    return redirect('club_main', club_id=club_id)

def calendar_create(request, club_id):
    club = get_object_or_404(Club, pk=club_id)
    if request.method == 'POST':
        form = CalendarForm(request.POST)
        if form.is_valid():
            calendar = form.save(commit=False)
            calendar.club = club
            calendar.save()
            return redirect('club_main', club_id=club.id)
    else:
        form = CalendarForm()
    context = {'form' : form}
    return render(request, 'club/calendar_form.html', context)

def calendar_modify(request, club_id, calendar_id):
    calendar = get_object_or_404(Calendar, pk=calendar_id)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=calendar)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('club_main', club_id=club_id)
    else:
        form = CalendarForm(instance=calendar)
    context = {'form': form}
    return render(request, 'club/calendar_form.html', context)

def calendar_delete(request, club_id, calendar_id):
    calendar = get_object_or_404(Calendar, pk=calendar_id)
    calendar.delete()
    return redirect('club_main', club_id=club_id)

def list_create(request, club_id):
    club = get_object_or_404(Club, pk=club_id)
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            list = form.save(commit=False)
            list.club = club
            list.save()
            return redirect('club_main', club_id=club.id)
    else:
        form = ListForm()
    context = {'form' : form}
    return render(request, 'club/list_form.html', context)

def list_modify(request, club_id, list_id):
    list = get_object_or_404(List, pk=list_id)
    if request.method == "POST":
        form = ListForm(request.POST, instance=list)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('club_main', club_id=club_id)
    else:
        form = ListForm(instance=list)
    context = {'form': form}
    return render(request, 'club/list_form.html', context)

def list_delete(request, club_id, list_id):
    list = get_object_or_404(List, pk=list_id)
    list.delete()
    return redirect('club_main', club_id=club_id)


def register(request):
    register_form = RegisterForm()
    context = {'forms' : register_form} 
    
    if request.method == 'GET':    
        return render(request, 'user/register.html', context)
    
    elif request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if(register_form.is_valid()) :
            user = User (
                user_id = register_form.user_id,
                user_pw = register_form.user_pw,
                user_name = register_form.user_name,
                user_email = register_form.user_email
            )
            user.save()
            return redirect('/')
        else :
            context['forms'] = register_form
        return render(request, 'user/register.html', context)


def login(request):
    loginform = LoginForm()
    context = {'forms' : loginform} 
    
    if request.method == 'GET':    
        return render(request, 'user/login.html', context)
    
    elif request.method == 'POST':
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            return redirect('home')
        else :
            context['forms'] = loginform
            if loginform.errors:
                context['error'] = ''
                for value in loginform.errors.values():
                    for v in value:
                        context['error'] += v + '\n'
        return render(request, 'user/login.html', context)