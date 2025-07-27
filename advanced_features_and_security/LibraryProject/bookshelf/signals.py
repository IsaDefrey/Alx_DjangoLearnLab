from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver
from .models import Book

@receiver(post_migrate)
def create_groups_and_permissions(sender, **kwargs):
    if sender.label != 'bookshelf':
        return  # Don't run for other apps

    from django.contrib.auth.models import Group, Permission
    from django.contrib.contenttypes.models import ContentType
    from .models import Book

    content_type = ContentType.objects.get_for_model(Book)

    permissions_map = {
        "Viewers": ["can_view"],
        "Editors": ["can_view", "can_create", "can_edit"],
        "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
    }

    for group_name, perm_codenames in permissions_map.items():
        group, _ = Group.objects.get_or_create(name=group_name)
        for codename in perm_codenames:
            try:
                perm = Permission.objects.get(codename=codename, content_type=content_type)
                group.permissions.add(perm)
            except Permission.DoesNotExist:
                print(f"[WARN] Permission {codename} not found. Try re-running migrate.")
