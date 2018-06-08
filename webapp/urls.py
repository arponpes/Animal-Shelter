from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('mascotas/', views.AnimalsView.as_view(), name='animals'),
    path('preguntas-frequentes', views.FrequentQuestionsView.as_view(),
         name='frequentQuestions'),
    path('ayuda', views.HelpView.as_view(), name='help'),
    path('contacto', views.ContactView.as_view(), name='contact'),
    re_path(r'^mascota/(?P<slug>[\w-]+)/$', views.AnimalDetail.as_view(),
            name='animal_detail'),
]
