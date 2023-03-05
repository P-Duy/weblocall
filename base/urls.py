from django.urls import path
from . import views




#code
urlpatterns = [
    path('',views.home,name='home'),
]

