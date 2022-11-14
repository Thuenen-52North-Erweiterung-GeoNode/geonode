from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:dataset_id>', views.get_dataset_data, name='get_dataset_data'),
]