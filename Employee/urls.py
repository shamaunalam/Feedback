from django.urls import path
from . import views
urlpatterns = [
    path('ehome',views.home,name='employee-home'),
    path('EmpFeedback/<str:pk>',views.ViewConsolidatedFeedback,name='view-consolidated'),
    path('bulkCreate',views.RegisterBulkStudents,name='bulkcreate')
]
