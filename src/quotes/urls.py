from django.urls import path
from .views import AuthorList, AuthorDetails,QuoteList, QuoteDetails
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("authors/",AuthorList.as_view(),name="authors"),
    path("authors/<int:pk>/",AuthorDetails.as_view(),name="author"),
    path("quotes/",QuoteList.as_view(),name="quotes"),
    path("quotes/<int:pk>/",QuoteDetails.as_view(),name="quote"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
