from django.urls import path
from . import views


urlpatterns = [
    path("categories", views.CategoriesView.as_view())
]