from django.urls import path
from . import views

urlpatterns = [
    path('', views.DiplomaListView.as_view(), name='diploma_list'),
    path('diploma/<int:pk>/', views.DiplomaDetailView.as_view(), name='diploma_detail'),
    path('diploma/add/', views.DiplomaCreateView.as_view(), name='diploma_add'),
    path('diploma/<int:pk>/edit/', views.DiplomaUpdateView.as_view(), name='diploma_edit'),
    path('diploma/<int:pk>/delete/', views.DiplomaDeleteView.as_view(), name='diploma_delete'),
]
