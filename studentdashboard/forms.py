from django import forms
from authentication.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'profile_picture', 'college', 'university',]

class CourseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_course', 'second_course', 'degree_type',]

class CountryForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nationality', 'country',]