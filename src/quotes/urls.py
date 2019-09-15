from django.urls import path
from .views import AuthorList, AuthorDetails,QuoteList, QuoteDetails
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("authors/",AuthorList.as_view()),
    path("authors/<int:pk>/",AuthorDetails.as_view()),
    path("quotes/",QuoteList.as_view()),
    path("quotes/<int:pk>/",QuoteDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
