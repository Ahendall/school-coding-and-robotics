from django.urls import path
from . import views

app_name = 'homepage'
urlpatterns = [
	path("", views.index, name="index"),
	path("signup", views.signup, name="signup"),
	path("login", views.login, name="login"),
]