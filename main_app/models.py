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


VALUE_CHOICES = [
  (1,'とても悪い'),
  (2,'悪い'),
  (3,'普通'),
  (4,'まあまあ'),
  (5,'とても良い')
]
class Question_radio(models.Model):
  content = models.CharField(max_length=100)
  def __str__(self):
    return self.content
 

class Answer_radio(models.Model):
  question_id = models.ForeignKey(Question_radio,on_delete=models.CASCADE)#質問テーブルと紐づけ
  content = models.TextField(verbose_name="種類名",choices=VALUE_CHOICES,blank=True)

