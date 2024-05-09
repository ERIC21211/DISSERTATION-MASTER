from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import UniDetail, UniCourse, UniService, UniContactInfo, UniUserQuery
from django.contrib.auth.models import Group
from authentication.models import CustomUser

@receiver(post_save, sender=CustomUser)
def assign_to_group(sender, instance, created, **kwargs):
    if created:  # Only execute for newly created users
        group_name = "University"  # Specify the name of your group
        group, created = Group.objects.get_or_create(name=group_name)
        instance.groups.add(group)


@receiver(post_save, sender=Group)
def assign_permissions_to_university_group(sender, instance, created, **kwargs):
    if created and instance.name == 'University':
        # Get content types for the specified models
        content_types = ContentType.objects.filter(app_label='unidashboard', model__in=['unidetail', 'unicourse', 'uniservice', 'unicontactinfo', 'uniuserquery'])

        # Get permissions for the content types
        permissions = Permission.objects.filter(content_type__in=content_types)

        # Add permissions to the group
        instance.permissions.add(*permissions)
