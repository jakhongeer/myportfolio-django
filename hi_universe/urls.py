from django.urls import path
from hi_universe import views

urlpatterns = [
    path('', views.hi_universe, name='hi_universe'),
]