from django.urls import path
from . import views

urlpatterns = [
    path('one/<int:pk>', views.CountryGetOne.as_view()),
    path('all/', views.CountryList.as_view()),
    path('in/<str:continent>', views.CountryInContinent.as_view()),
    path('from/<int:start>', views.CountryGetFrom.as_view()),
    path('range/<int:start>/<int:end>', views.CountryGetRange.as_view()),

    # admin previlegies.
    path('update/<int:pk>', views.CountryUpdate.as_view()),
    path('delete/<int:pk>', views.CountryDelete.as_view()),
    path('create/', views.CountryCreate.as_view()),
]
