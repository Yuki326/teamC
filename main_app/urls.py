from django.urls import path
from main_app import views
urlpatterns = [
  path('',views.index,name='index'),
  path('answer/',views.answer,name='answer'),
  path('save_text_answers',views.save_text_answers,name='save_text_answers'),
]
