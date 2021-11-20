from django.shortcuts import render
from django.http import HttpResponse
from main_app.forms import QuestionTextForm
from main_app.forms import AnswerTextForm
from django.shortcuts import redirect
from main_app.models import Question_text
from main_app.models import Answer_text


# Create your views here.
def index(request):
  if(request.method == 'POST'):
    content = request.POST['content']
    item = Question_text(content=content) 
    item.save()
    return redirect(to = 'index')
  params={
    'form':QuestionTextForm(),
    'data':Question_text.objects.all()
  }
  return render(request,'index.html',params)

def answer(request):
  if(request.method == 'POST'):
    obj=Answer_text()
    item = AnswerTextForm(request.POST,instance=obj) 
    item.save()
    return redirect(to = 'answer')
  params={
    'form':AnswerTextForm(),
    'data':Answer_text.objects.all(),
    'dataQ':Question_text.objects.all()
  }
  return render(request,'answer.html',params)
  
def createQuestionText(request):
  if(request.method == 'POST'):
      item = QuestionTextForm(request.POST)
      item.save()
      return redirect(to = '')

  return render(request,'index.html')
