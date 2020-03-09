
from django.urls import path

from . import views

app_name = 'ourprojects'

urlpatterns = [

    path('' , views.projjects , name='projjects'),
    
    path('<int:project_id>/' , views.detail , name='detail'),
]