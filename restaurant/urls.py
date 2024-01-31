from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('about/', views.AboutView.as_view()),
    path('menu/', views.MenuView.as_view()),
    path('menu_item/<int:id>', views.MenuItemView.as_view()),
    path('book/', views.BookView.as_view(), name = 'book'),
]
