from django.db import models
from django.utils import timezone

# Create your models here.



class Question_text(models.Model):
  content = models.CharField(max_length=100)
  def __str__(self):
    return self.content
 

class Answer_text(models.Model):
  question_id = models.ForeignKey(Question_text,on_delete=models.CASCADE)#質問テーブルと紐づけ
  content = models.CharField(max_length=100)
  #created_at
