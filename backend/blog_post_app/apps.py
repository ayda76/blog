from django.apps import AppConfig


class BlogPostAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog_post_app'
    def ready(self):
        import blog_post_app.api.signals