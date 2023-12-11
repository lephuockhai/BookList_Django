from django.urls import path
from . import views

urlpatterns = [
    path('menu-items/', views.menu_items),
    path('single-items/<int:id>', views.single_items),
]