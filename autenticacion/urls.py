from django.urls import path
from .views import RegistroView, LoginView

urlpatterns = [
  path('login', LoginView.as_view()),
  path('registro', RegistroView.as_view())
]