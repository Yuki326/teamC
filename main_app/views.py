from django.shortcuts import render
from django.http import HttpResponse
from main_app.forms import QuestionTextForm
from main_app.forms import AnswerTextForm
from django.shortcuts import redirect
from main_app.models import Question_text
from main_app.models import Answer_text
from main_app.models import Question_radio
from main_app.models import Answer_radio
from main_app.forms import QuestionRadioForm
from main_app.forms import AnswerRadioForm

# Create your views here.
def index(request):
  if(request.method == 'POST'):
    content = request.POST['content']
    item = Question_text(content=content) 
    item.save()
    return redirect(to = 'index')
  params={
    'form':QuestionTextForm(),
    'data':Question_text.objects.all(),
  }
  return render(request,'index.html',params)

def radio(request):
  if(request.method == 'POST'):
    content = request.POST['content']
    obj = Question_radio(content=content) 
    obj.save()
    return redirect(to = 'radio')
  params={
    'form':QuestionRadioForm(),
    'data':Question_radio.objects.all(),
  }
  return render(request,'radio.html',params)

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

def sub(request):
  if(request.method == 'POST'):
    obj=Answer_radio()
    item = AnswerRadioForm(request.POST,instance=obj) 
    item.save()
    return redirect(to = 'sub')
  params={
    'form':AnswerRadioForm(),
    'data':Answer_radio.objects.all(),
    'dataQ':Question_radio.objects.all()
  }
  return render(request,'sub.html',params)
  


def save_text_answers(request):
    questions = Question_text.objects.all()
    for i in questions:
      if 'answer'+str(i.id) in request.GET:
        answer = request.GET['answer'+str(i.id)]
        question = Question_text.objects.get(id=i.id)
        obj=Answer_text(question_id=question,content=answer)
        obj.save()
    # subject=Subject.objects.get(id=subject_id)
    # #todo 開始日と締め切り日の要素を後で追加する
    # obj = Task(subject_id=subject,name=name,author = request.user,start=start)
    # obj.save()
    return HttpResponse('Hellooooo')