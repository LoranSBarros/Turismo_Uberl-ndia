from django.urls import path
from . import views

urlpatterns = [
    path('', views.intro, name='intro'),
    path('sabia/', views.sabia, name='sabia'),
    path('siquierolli/', views.siquierolli, name='siquierolli'),
    path('sucupira/', views.sucupira, name='sucupira')
]
