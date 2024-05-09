from django.shortcuts import render
from django.contrib.auth.models import Group
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect
from django.urls import reverse
from .models import UniDetail, UniCourse, UniService, UniContactInfo, UniUserQuery

def university_dashboard(request):
    get_user = request.user
    if get_user.is_authenticated:
        about = UniDetail.objects.filter(uni=request.user.profile)
        course = UniCourse.objects.filter(uni=request.user.profile)
        service = UniService.objects.filter(uni=request.user.profile)
        contact = UniContactInfo.objects.filter(uni=request.user.profile)
        university_name = "Your University Name"
        if about:
            university_name = about[0].name
        else:
            university_name = university_name
        context = {
            'abouts': about,
            'course': course,
            'service': service,
            'contact': contact,
            'university_name': university_name
        }
        return render(request, 'university-page.html', context)
    else:
        return redirect(reverse('index'))
    
def university_detail_view(request, id):
    about = UniDetail.objects.filter(pk=id).all()
    get_unidet_id = about[0].uni_id
    course = UniCourse.objects.filter(uni=get_unidet_id).all()
    service = UniService.objects.filter(uni=get_unidet_id)
    contact = UniContactInfo.objects.filter(uni=get_unidet_id)
    university_name = "Your University Name"
    if about:
        university_name = about[0].name
    else:
        university_name = university_name
    context = {
        'abouts': about,
        'course': course,
        'service': service,
        'contact': contact,
        'university_name': university_name
    }
    print(context)
    return render(request, 'university-page.html', context)


# Usage example with redirection if user is not allowed
def admin_panel(request):
    # Check if user is allowed to access this view
    if request.user is not None and request.user.is_staff:
        return redirect(reverse('admin:index'))
    else:
        return redirect(reverse('index'))  # Redirect to the index page if user is not allowed
