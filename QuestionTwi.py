
# Make a response and here we can see the current thread is mainThread same is for caller
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def signal_receiver(sender, instance, created, **kwargs):
    current_thread = threading.current_thread()
    print(f"Signal receiver running in thread: {current_thread.name}")
    print(f"User created: {created}, Username: {instance.username}")



# Check for currentThread and Print it for request creation or when enpoint get hitted
from django.http import JsonResponse

def create_user_view(request):
    current_thread = threading.current_thread()
    print(f"Request handler running in thread: {current_thread.name}")

    # Create a new user to trigger the signal
    user = User.objects.create(username="test_user")
    return JsonResponse({"message": "User created!"})

# Will make request on create-user endpoint that will trigger create_user_view
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-user/', create_user_view),
]
# config code
from django.apps import AppConfig

class Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = ''

    def ready(self):
        import signals
