from django.urls import path
from main_app import views
urlpatterns = [
  path('',views.index,name='index'),
  path('get_index_data',views.get_index_data,name='get_index_data'),
  path('answer/',views.answer,name='answer'),
  path('save_text_answers',views.save_text_answers,name='save_text_answers'),
  path('sub',views.sub,name='sub'),
  path('radio',views.radio,name='radio'),
  path('delete_question_text/<int:num>',views.delete_question_text,name='delete_question_text'),
  path('result',views.result,name='result'),

]
