from django.urls import include, path, re_path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='HomeView'),
    path('frequent-questions', views.FrequentQuestionsView.as_view(),
         name='FrequentQuestions'),
    path('about-us', views.AboutUsView.as_view(), name='AboutUs')
]
