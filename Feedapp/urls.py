from django.urls import path
from . import views
urlpatterns = [
    path('',views.Login,name='login'),
    path('gf',views.getFeedback,name='submitfeedback'),
    path('logout',views.Logout,name='logout'),
]
