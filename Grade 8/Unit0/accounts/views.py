from django.contrib.auth import authenticate, login, logout
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q
from .forms import SignUpForm

# Create your views here.


def login_view(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse("homepage:index"))

	if request.method == "GET":
		return render(request, 'accounts/login.html')

	else:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse('homepage:index'))
		else:
			return render(request, 'accounts/login.html', {
				'message': 'Invalid login'
			})


def logout_view(request):
	# Clear likedmoviees, dislikedmovies, and genreweightedscore
	request.session['likedMovies'] = []
	request.session['dislikedMovies'] = []
	request.session['genreWeightedScore'] = {}

	logout(request)
	return HttpResponseRedirect(reverse('accounts:login'))
	


def register(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse("homepage:index"))

	if request.method == "GET":
		# Render template with django signupform
		form = SignUpForm()
		return render(request, 'accounts/register.html', {'form': form})
	else:
		# Get form data
		form = SignUpForm(request.POST)
		# Check if form is valid
		if form.is_valid():
			# Save user
			user = form.save()
			# Log user in
			login(request, user)

			# render login page with message "Succecfully registered"
			return render(request, 'accounts/login.html', {
				'message': 'Succecfully registered'
			})

		else:
			# If form is not valid, return to registration page
			return render(request, 'accounts/register.html', {
				'form': form,
				'message': 'Invalid form data'
			})
