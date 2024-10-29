from django.urls import path
from .views import * 

urlpatterns = [
    path('home/', homepage.as_view()),
    path('about/' , AboutPageView.as_view()),
    path('menu/' , MenuPageView.as_view()),
    path('contact/' , ContactPageView.as_view())
]