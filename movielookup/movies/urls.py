from django.urls import path
from movies import views


urlpatterns = [
    path('', views.HomePageView.as_view())
]
