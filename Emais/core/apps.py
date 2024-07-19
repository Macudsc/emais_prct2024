from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"

# Автоматическое создание групп при миграции базы данных
#from django.apps import AppConfig
#from django.db.models.signals import post_migrate

#def create_default_groups(sender, **kwargs):
#    from django.contrib.auth.models import Group
#    groups = ['patient', 'doctor', 'administrator']
#    for group in groups:
#        Group.objects.get_or_create(name=group)

#class CoreConfig(AppConfig):
#    name = 'core'

#    def ready(self):
#        post_migrate.connect(create_default_groups, sender=self)