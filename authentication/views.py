from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from authentication.models import CustomUser, Profile
from .forms import CustomUserCreationForm
from django.contrib.auth import logout

def registerStudent(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            full_name = request.POST.get('full_name')
            user_type = 'student'
            user = form.save()
            Profile.objects.create(user=user, full_name=full_name, user_type=user_type)
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'student-register.html', {'form': form})

def registerUniversity(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            full_name = request.POST.get('full_name')
            user_type = 'university'
            user = form.save()
            get_user = CustomUser.objects.get(email=user.email)
            get_user.is_staff = True
            get_user.save()
            Profile.objects.create(user=user, full_name=full_name, user_type=user_type)
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'university-register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        user = authenticate(request, email=email, password=password)
        if user is not None:
            get_user_type = Profile.objects.get(user=user).user_type
            if get_user_type == 'student':
                login(request, user)
                return redirect('studentdashboard')
            elif get_user_type == 'university':
                login(request, user)
                return redirect('unidashboard')
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('index')  # Redirect to the login page after logout

