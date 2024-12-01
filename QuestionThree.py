# receiver code 
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import transaction

@receiver(post_save, sender=User)
def signal_receiver(sender, instance, created, **kwargs):
    if created:
        print("Signal triggered: Creating related profile.")
        # Simulate additional database operation
        try:
            with transaction.atomic():
                raise Exception("Error in signal transaction")
        except Exception as e:
            print(f"Signal exception: {e}")

# create_user_view triggered when endpoint hitted
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db import transaction

def create_user_view(request):
    try:
        with transaction.atomic():
            user = User.objects.create(username="test_user")
            print("User created in transaction.")
            # Simulate an error after the signal is triggered
            raise Exception("Error in caller transaction")
    except Exception as e:
        print(f"View exception: {e}")
    
    return JsonResponse({"message": "Transaction attempted!"})


# url paths
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-user/', create_user_view),
]
