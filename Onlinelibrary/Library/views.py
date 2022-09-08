from re import T
from django.conf import settings
from django.forms import PasswordInput
from django.shortcuts import redirect, render
from django.http import HttpResponse
from Library.models import Student
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'home.html')

#.............................REGISTRATION DATABASE CONNECTION.............................

def regis(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        phone = request.POST['phone']
        email = request.POST['email']
        passw = request.POST['pass']
        cpassw = request.POST['cpass']
        if passw == cpassw:
            student = Student.objects.create(name = name, dob=dob, phone = phone, email = email, password = passw)
            return redirect('login')
        else:
            messages.warning(request,'Confirm password is not match')
            return redirect('regis')
    else:
        return render(request, 'regis.html')

#.............................LOGIN DATABASE CONNECTION.............................

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass']
        if Student.objects.filter(email = email).exists():
            student = Student.objects.get(email = email)
            if password == student.password:
                # messages.info(request, 'Successfully Login')
                return redirect('course')
            else:
                messages.warning(request, 'Password not match')
                return redirect('login')
        else:
            messages.warning(request, 'User not register')
            return redirect('login')
    else:
        return render(request, 'login.html')

#.............................FORGET PASSWORD DATABASE CONNECTION.............................

def forgetpass(request):
    if request.method == 'POST':
        email = request.POST['email']
        npass = request.POST['npass']
        cnpass =request.POST['cnpass']
        if Student.objects.filter(email = email).exists():
            student = Student.objects.get(email = email)
            if npass == cnpass:
                student = Student.objects.update(password = npass)
                return redirect('login')
            else:
                messages.warning(request, 'Confirm password is not match')
                return redirect('forgetpass')
        else:
            messages.warning(request, 'Enter email is not register')
            return redirect('forgetpass')
    else:
        return render(request,'forgetpass.html')


def course(request):
    return render(request, 'course.html')

def classroom(request):
    return render(request, 'classroom.html')

def classroom1(request):
    return render(request, 'classroom1.html')

def intermediate(request):
    return render(request, 'intermediate.html')

def higher(request):
    return render(request, 'higher.html')

def college(request):
    return render(request, 'college.html')

def literature(request):
    return render(request, 'literature.html')

def story(request):
    return render(request, 'story.html')

def indianlaw(request):
    return render(request, 'indianlaw')

def yoga(request):
    return render(request, 'yoga.html')

def spiritual(request):
    return render(request, 'spiritual.html')

def diploma(request):
    return render(request, 'diploma.html')
