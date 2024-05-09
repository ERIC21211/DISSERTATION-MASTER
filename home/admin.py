from django.contrib import admin
from .models import Company, History, Mission, CEO, Product, ContactForm, UserPost

# Define admin classes for each model
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('description',)
    # Customize other admin options as needed

class HistoryAdmin(admin.ModelAdmin):
    list_display = ('description',)
    # Customize other admin options as needed

class MissionAdmin(admin.ModelAdmin):
    list_display = ('description',)
    # Customize other admin options as needed

class CEOAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    # Customize other admin options as needed

class ProductAdmin(admin.ModelAdmin):
    list_display = ('description',)
    # Customize other admin options as needed

class UserQueryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message',)
    # Customize other admin options as needed

# Register models and admin classes
admin.site.register(Company, CompanyAdmin)
admin.site.register(History, HistoryAdmin)
admin.site.register(Mission, MissionAdmin)
admin.site.register(CEO, CEOAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ContactForm, UserQueryAdmin)
admin.site.register(UserPost)
