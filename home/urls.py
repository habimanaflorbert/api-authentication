from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers
from . import views
from.views import *

rout=routers.DefaultRouter()
rout.register('clients',views.userView)
rout.register('languages',views.languageView)
rout.register('climate',views.climateView)

urlpatterns = [
    # path('', include(rout.urls)),
    path('login/',CustomAuthToken.as_view()),
    path('task-list/', views.taskList, name="task-list"),
    path('task-detail/<int:id>',views.taskDetail, name="task-detail"),
    path('task-create/',views.taskCreate)
    # path('', include('rest_framework.urls', namespace='rest_framework'))
]