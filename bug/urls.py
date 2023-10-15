from django.urls import path

from . import views

urlpatterns = [
    path("", views.bug, name="bug"),
    path("register_bug/", views.register_bug, name="register_bug"),
    path("list_bug/", views.list_bug, name="list_bug"),
    path('view_bug/<int:id>/', views.view_bug, name='view_bug'),
]