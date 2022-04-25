from django.urls import path

from . import views

urlpatterns = [
    path('upload/score', views.upload_score, name='upload_score'),
    path('ranking/list', views.ranking_list, name='ranking_list')
]