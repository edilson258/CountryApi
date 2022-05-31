from django.urls import path
from . import views

urlpatterns = [
    path('one/<int:pk>', views.CountryGetOne.as_view()),
    path('all/', views.CountryList.as_view()),
    path('update/<int:pk>', views.CountryUpdate.as_view()),
    path('delete/<int:pk>', views.CountryDelete.as_view()),
    path('create/', views.CountryCreate.as_view()),
]
