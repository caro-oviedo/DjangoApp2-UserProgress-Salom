from django.urls import path 
from .views import LevelListView, DetailLevelView, ListProgressView, TricksListView
from . import views 

app_name = 'slalom'
urlpatterns = [
    #path ('', views.index, name='index'),
    path ('', views.LevelListView.as_view(), name='index'),
    path ('level/<int:pk>/', views.DetailLevelView.as_view(), name='level-detail'),
    #path ('trick/<int:pk>/', views.DetailTrickView.as_view(), name='trick-detail'),
    path ('progress/',views.ListProgressView.as_view(), name='progress'),
    path ('trick/<int:trick_id>/', views.trick_detail, name='trick-detail'),
    path ('tricks/',views.TricksListView.as_view(), name='tricks'),
    path('search/', views.search, name='search-tricks'),
    
    
    

    
    
    
    
]
