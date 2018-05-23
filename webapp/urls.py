from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('animals/', views.AnimalsView.as_view(), name='animals'),
    path('frequent-questions', views.FrequentQuestionsView.as_view(),
         name='frequentQuestions'),
    path('about-us', views.AboutUsView.as_view(), name='aboutUs'),
    path('help', views.HelpView.as_view(), name='help'),
    path('contact', views.ContactView.as_view(), name='contact'),
    re_path(r'^animal/(?P<pk>\d+)/detail/', views.AnimalDetail.as_view(),
            name='animal_detail'),
]
