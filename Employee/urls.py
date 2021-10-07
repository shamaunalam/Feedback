from django.urls import path
from . import views
urlpatterns = [
    path('ehome',views.home,name='employee-home'),
]
