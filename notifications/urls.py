from django.urls import path
from .views import NotificationViewSet

urlpatterns = [
    path('create/', NotificationViewSet.as_view({'post': 'create'}), name='create-notification'),
]
