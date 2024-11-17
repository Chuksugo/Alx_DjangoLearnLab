from django.apps import AppConfig


class BookshelfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookshelf'


from django.apps import AppConfig
from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver

class RelationshipAppConfig(AppConfig):
    name = 'relationship_app'

    def ready(self):
        # Assign permissions to groups after migration
        post_migrate.connect(create_groups_permissions, sender=self)

def create_groups_permissions(sender, **kwargs):
    # Create or get groups
    viewer_group, created = Group.objects.get_or_create(name='Viewers')
    editor_group, created = Group.objects.get_or_create(name='Editors')
    admin_group, created = Group.objects.get_or_create(name='Admins')

    # Get permissions
    can_view = Permission.objects.get(codename='can_view')
    can_create = Permission.objects.get(codename='can_create')
    can_edit = Permission.objects.get(codename='can_edit')
    can_delete = Permission.objects.get(codename='can_delete')

    # Assign permissions to groups
    viewer_group.permissions.add(can_view)
    editor_group.permissions.add(can_view, can_create, can_edit)
    admin_group.permissions.add(can_view, can_create, can_edit, can_delete)
