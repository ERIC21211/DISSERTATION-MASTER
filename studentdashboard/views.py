from django.shortcuts import render, redirect, get_object_or_404
from authentication.models import Profile
from .forms import CountryForm, CourseForm, ProfileForm


def student_dashboard(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        context = {
            'user': profile,
        }
    else:
        context = {}
        return redirect('login')
    return render(request, 'student-page.html', context)

def student_name(request):
    # Retrieve the user's profile instance or create a new one if not found
    profile = get_object_or_404(Profile, user=request.user)
    print(profile)
    # Initialize the ProfileForm with the retrieved profile instance
    form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
    print(form)
    
    if request.method == 'POST':
        # If the request method is POST, process the form submission
        if form.is_valid():
            # Save the form data to the database
            try:
                form.save()
                return redirect('studentdashboard')  # Redirect to studentdashboard page after successful form submission
            except Exception as e:
                pass  # Handle any exceptions that occur during form submission
        
    # Render the student-page.html template with the form
    context = {
        'form': form,
        'user': profile,
    }
    return render(request, 'student-page.html', context)

def student_course(request):
    # Retrieve the user's profile instance or create a new one if not found
    profile = get_object_or_404(Profile, user=request.user)
    print(profile)
    # Initialize the ProfileForm with the retrieved profile instance
    form = CourseForm(request.POST or None, request.FILES or None, instance=profile)
    print(form)
    
    if request.method == 'POST':
        # If the request method is POST, process the form submission
        if form.is_valid():
            # Save the form data to the database
            try:
                form.save()
                return redirect('studentdashboard')  # Redirect to studentdashboard page after successful form submission
            except Exception as e:
                pass  # Handle any exceptions that occur during form submission
        
    # Render the student-page.html template with the form
    context = {
        'form': form,
        'user': profile,
    }
    return render(request, 'student-page.html', context)

def student_country(request):
    # Retrieve the user's profile instance or create a new one if not found
    profile = get_object_or_404(Profile, user=request.user)
    print(profile)
    # Initialize the ProfileForm with the retrieved profile instance
    form = CountryForm(request.POST or None, request.FILES or None, instance=profile)
    print(form)
    
    if request.method == 'POST':
        # If the request method is POST, process the form submission
        if form.is_valid():
            # Save the form data to the database
            try:
                form.save()
                return redirect('studentdashboard')  # Redirect to studentdashboard page after successful form submission
            except Exception as e:
                pass  # Handle any exceptions that occur during form submission
        
    # Render the student-page.html template with the form
    context = {
        'form': form,
        'user': profile,
    }
    return render(request, 'student-page.html', context)

