from django.contrib import admin
from unidashboard.models import UniDetail, UniService, UniContactInfo, UniUserQuery, UniCourse
class UniDetailAdmin(admin.ModelAdmin):
    exclude = ('uni',)  # Make the 'uni' field read-only
    
    def save_model(self, request, obj, form, change):
        if not obj.uni_id:  # Check if the uni field is empty
            obj.uni = request.user.profile  # Assign the logged-in user's profile to the uni field
        super().save_model(request, obj, form, change)

admin.site.register(UniDetail, UniDetailAdmin)

class CustomModelAdmin(admin.ModelAdmin):
    exclude = ('uni',)  # Exclude the 'uni' field from the admin form
    
    def save_model(self, request, obj, form, change):
        if not obj.uni_id:  # If 'uni' field is empty
            obj.uni = request.user.profile  # Assign the logged-in user's profile to 'uni'
        super().save_model(request, obj, form, change)

# Define their corresponding admin classes
class UniServiceAdmin(CustomModelAdmin):
    pass

class UniContactInfoAdmin(CustomModelAdmin):
    pass

class UniUserQueryAdmin(CustomModelAdmin):
    pass

class UniCourseQueryAdmin(CustomModelAdmin):
    pass

# Register the models and their admin classes
admin.site.register(UniService, UniServiceAdmin)
admin.site.register(UniContactInfo, UniContactInfoAdmin)
admin.site.register(UniUserQuery, UniUserQueryAdmin)
admin.site.register(UniCourse, UniCourseQueryAdmin)
