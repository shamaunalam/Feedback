from django.urls import path
from . import views
urlpatterns = [
    path('',views.Login,name='login'),
    path('getfeedback/<str:pk>',views.getFeedback,name='submitfeedback'),
    path('logout',views.Logout,name='logout'),
    path('oops',views.oops,name='oops'),
]
