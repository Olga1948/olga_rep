from django.urls import path
from .views import user_create, success_view


urlpatterns = [
    path('create/', user_create, name='user_create'),
    path('success/', success_view, name='success')
]
