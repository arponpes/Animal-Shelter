from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='Home'),
    path('frequent-questions', views.FrequentQuestionsView.as_view(),
         name='FrequentQuestions'),
    path('about-us', views.AboutUsView.as_view(), name='AboutUs'),
    path('help', views.HelpView.as_view(), name='Help'),
    path('contact', views.ContactView.as_view(), name='Contact')
]
