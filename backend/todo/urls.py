from django.urls import path,include
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register(r'tasks' , views.TodoView , 'task')
urlpatterns = [
    path('api/',include(router.urls)),
]
