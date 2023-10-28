from django.urls import path

from . import views

# uniquely identifies the different urls from the tow index files in the two apps
app_name = "tasks"
urlpatterns = [
    path('', views.index, name='index'),
    path('/add', views.add, name='add')
]
