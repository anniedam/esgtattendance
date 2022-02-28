from multiprocessing import AuthenticationError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Entry
from .forms import EntryCreateForm, CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here. 
def home(request):
    title = 'Welcome: This is your home page'
    context = {
        "title": title,
    }
    return render(request, 'main/home.html', context)

def registered(request):
    title = 'List of registered students'
    queryset = Entry.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, 'main/registered.html', context)


def attendance(request):
    title = 'Take attendance of students'
    queryset = Entry.objects.all()
    if request.method == "POST":
        id_list = request.POST.getlist('boxes')
        id_list2 = request.POST.getlist('boxes2')
        id_list3 = request.POST.getlist('boxes3')
        id_list4 = request.POST.getlist('boxes4')
        id_list5 = request.POST.getlist('boxes5')
        id_list6 = request.POST.getlist('boxes6')
        

     

        for x in id_list:
            Entry.objects.filter(pk=int(x)).update(lecture_1=True)
        
        for x in id_list2:
            Entry.objects.filter(pk=int(x)).update(lecture_2=True)

        for x in id_list3:
            Entry.objects.filter(pk=int(x)).update(lecture_3=True)
        
        for x in id_list4:
            Entry.objects.filter(pk=int(x)).update(lecture_4=True)

        for x in id_list5:
            Entry.objects.filter(pk=int(x)).update(lecture_5=True)
        
        for x in id_list6:
            Entry.objects.filter(pk=int(x)).update(lecture_6=True)

        messages.success(request, 'Attendance updated')
        return redirect('/attendance')
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, 'main/attendance.html', context)
    

def add(request):
    form = EntryCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/registered')
    context = {
        "form": form,
        "title": "Add",
    }
    return render(request, 'main/add.html', context)


def delete_items(request, pk):
    queryset = Entry.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('/registered')
    return render(request, 'main/delete_items.html')



def register(request):
   form = CreateUserForm()

   if request.method == 'POST':
       form = CreateUserForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('/loginpage')

   return render(request, 'main/register.html', {'form': form})

def loginpage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/registered')

    context = {}
    return render(request, 'main/loginpage.html', context)


def logout(request):
    title = 'Logged Out'
    context = {
        "title": title,
    }
    return render(request, 'main/logout.html', context)


def calculator(request):
    title = 'Attendance: Calculator'
    context = {
        "title": title,
    }
    return render(request, 'main/calculator.html', context)

def result(request):
    held = int(request.GET["held"])
    attended = int(request.GET["attended"])
    percent = (100/held) * attended

    return render(request, 'main/result.html', { "result": percent })


