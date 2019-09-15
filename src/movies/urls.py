from django.urls import path
from .views import ActorList, ActorDetails, MovieList, MovieDetails
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("actors/", ActorList.as_view()),
    path("actors/<int:pk>/", ActorList.as_view()),
    path("movies/", MovieList.as_view()),
    path("movies/<int:pk>/", MovieDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)