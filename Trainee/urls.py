from django.urls import path
from . import views
urlpatterns = [
    path('thome',views.home,name='trainee-home'),
]
