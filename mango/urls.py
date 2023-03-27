from django.urls import path
from . import views

urlpatterns = [
    path("api/v1/mango/", views.MangaAPIView.as_view()),
    path("api/v1/mango/<int:id>/", views.MangaDetailAPIView.as_view()),
]
