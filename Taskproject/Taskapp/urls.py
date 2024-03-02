from django.urls import path
from .views import PersonAPI, DetailsAPI

urlpatterns = [
    path('add/',PersonAPI.as_view()),
    path('add/<int:pk>/',DetailsAPI.as_view())
]
