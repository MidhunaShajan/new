from django.contrib import messages, auth
from django.shortcuts import render, redirect

# Create your views here.
# myapp/views.py
from django.shortcuts import render
from .forms import RegistrationForm, RegistrationForm1
from .models import Department, Course

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Process the form data as needed (e.g., saving to a database)
            # Redirect to a success page or perform other actions
            # messages.info(request,'Registration Completed')
            return render(request, 'success.html')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

def get_courses(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).order_by('name')
    return render(request, 'course_dropdown_list.html', {'courses': courses})
def home(request):
    return render(request,'home.html')
def firstregister(request):
    if request.method == 'POST':
        form1 = RegistrationForm1(request.POST)
        if form1.is_valid():
            form1.save()
            # Redirect to a success page or login page.
            return redirect('login')
    else:
        form1 = RegistrationForm1()

    return render(request, 'firstregister.html', {'form': form1})
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('new')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    return render(request,'login.html')
def new(request):
    return render(request,'new.html')
def logout(request):
    auth.logout(request)
    return redirect('/')