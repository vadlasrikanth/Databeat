from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView
from . import views


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),

	# path('movie-list/', views.movieList, name="movie-list"),
	# path('movie-detail/<str:pk>/', views.movieDetail, name="movie-detail"),
	# path('movie-create/', views.movieCreate, name="movie-create"),
	# path('movie-update/<str:pk>/', views.movieUpdate, name="movie-update"),
	# path('movie-delete/<str:pk>/', views.movieDelete, name="movie-delete"),
]