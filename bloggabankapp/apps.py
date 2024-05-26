from django.apps import AppConfig


class BloggabankappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bloggabankapp'

    def ready(self):
    	import bloggabankapp.signals
